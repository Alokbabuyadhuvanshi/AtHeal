import google.generativeai as genai
from django.conf import settings
import logging



logger = logging.getLogger(__name__)

class MedicalAssistantAI:
    def __init__(self):
    # Initialize the AI model
        genai.configure(api_key= settings.GEMINI_API_KEY)
        self.model = genai.GenerativeModel(settings.GEMINI_MODEL)

        # Define the system prompt with the medical assistant guidelines
        self.system_prompt = """
                            You are an AI-powered Medical Assistant designed to provide empathetic, responsible, and accurate health guidance to users. Your goal is to support users by offering general health information, symptom explanations, and self-care advice while ensuring safety and ethical medical guidance.

                            ⚠️ Important: You must NOT provide a definitive diagnosis, prescribe medication, or act as a substitute for a medical professional. Instead, focus on:
                            - Educating users on possible causes of symptoms.
                            - Suggesting general wellness and over-the-counter remedies.
                            - Recommending when to seek urgent medical attention.

                            Guidelines for Interaction:
                            - Be empathetic & supportive: Show concern for the user's well-being. Use reassuring language.
                            - Ask follow-up questions: If symptoms are unclear, gather more details before responding.
                            - Provide simple, clear explanations: Avoid complex medical jargon—explain in plain terms.
                            - Offer general health tips only: Provide advice on hydration, rest, mild pain relief, etc.
                            - Know when to escalate: If symptoms indicate a potential emergency, immediately advise contacting a doctor or emergency services.
                            - Ensure privacy & safety: Never ask for or store personal medical records.

                            Escalation Triggers (When to Seek a Doctor or ER):
                            If a user reports any of the following, immediately recommend they see a doctor or call emergency services:
                            - Chest pain or difficulty breathing
                            - High fever (above 103°F / 39.5°C)
                            - Severe headache with vision loss
                            - Numbness, confusion, slurred speech (possible stroke symptoms)
                            - Severe allergic reaction (swelling, difficulty breathing)
                            - Persistent vomiting, dehydration, or blood in vomit
                            - Mental health crisis (suicidal thoughts, panic attacks)
                            """

    def get_conversation_history_format(self, messages):
        """Format conversation history for Gemini API"""
        formatted_messages = []
        
        # ADD SYSTEM PROMPT AS THE FIRST MESSAGE
        formatted_messages.append({
                    "role": "system", 
                    "content": [{"text":self.system_prompt}]
                    })

        # Add conversation history
        for message in messages:
            if isinstance(message, dict):
                # For guest users stored in session
                role = "user" if message["role"] == "user" else "model"
                formatted_messages.append({
                    "role": role,
                    "parts": [{"text": message["content"]}]
                })
            else:
                # For authenticated users with Message objects
                role = "user" if message.role == "user" else "model"
                formatted_messages.append({
                    "role": role,
                    "parts": [{"text": message.content}]
                })
                
        return formatted_messages


    def generate_response(self, conversation_history):
        """Generate a response using the Gemini AI model"""
        try:
            # Start with system prompt
            messages = [
                {"role": "model", "parts": [{"text": self.system_prompt}]}
            ]
            
            # Add conversation history
            for message in conversation_history:
                if isinstance(message, dict):
                    # For guest users
                    role = "user" if message["role"] == "user" else "model"
                    content = message["content"]
                else:
                    # For authenticated users
                    role = "user" if message.role == "user" else "model"
                    content = message.content
                
                messages.append({"role": role, "parts": [{"text": content}]})
            
            # Extract the last user message for sending
            last_message = None
            if messages and messages[-1]["role"] == "user":
                last_message = messages[-1]["parts"][0]["text"]
                messages = messages[:-1]  # Remove last message from history
            else:
                # If the last message isn't from user, return an error
                return "Error: Missing user message at the end of conversation."
            
            # Start chat with history
            chat = self.model.start_chat(history=messages)
            
            # Send message and get response
            response = chat.send_message(
                last_message,
                generation_config={
                    "temperature": 0.2,
                    "top_p": 0.95,
                    "top_k": 40,
                    "max_output_tokens": 1024,
                }
            )
            
            return response.text
        
        except Exception as e:
            logger.error(f"Error generating response from Gemini: {str(e)}")
            return f"I'm sorry, I'm having trouble processing your request. Please try again later or contact support if the issue persists. (Error: {str(e)})"

