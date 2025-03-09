from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Conversation, Message
from .services import MedicalAssistantAI
import uuid

class ChatView(TemplateView):
    template_name = 'chat.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get or create session ID
        session_id = self.request.session.get('conversation_id')
        if not session_id:
            session_id = str(uuid.uuid4())
            self.request.session['conversation_id'] = session_id

        if self.request.user.is_authenticated:
            conversation, created = Conversation.objects.get_or_create(
                session_id=session_id,
                defaults={'user': self.request.user}
            )
            messages = conversation.messages.all().order_by('timestamp')

            if created or messages.count() == 0:
                welcome_message = Message.objects.create(
                    conversation=conversation,
                    role='assistant',
                    content=("Hello! I'm your AI Medical Assistant. I can provide general health information "
                    "and guidance, though I'm not a replacement for professional medical advice. "
                    "How can I help you today?")
                )
                messages = [welcome_message]
        else:
            # Retrieve messages from session for guest users
            messages = self.request.session.get('guest_messages', [])

            # If it's a new session, add a welcome message
            if not messages:
                messages.append({
                    'role': 'assistant',
                    'content': ("Hello! I'm your AI Medical Assistant. I can provide general health information "
                    "and guidance, though I'm not a replacement for professional medical advice. "
                    "How can I help you today?")
                })
                self.request.session['guest_messages'] = messages

        context['messages'] = messages
        return context
            
class MessageAPIView(APIView):
    """API endpoint for sending/receiving messages with the AI Medical Assistant"""

    def post(self, request):
        user_message = request.data.get('message', '').strip()
        session_id = request.session.get('conversation_id')

        if not session_id:
            session_id = str(uuid.uuid4())
            request.session['conversation_id'] = session_id

        if not user_message:
            return Response({'error': 'Message cannot be empty'}, status=status.HTTP_400_BAD_REQUEST)

        medical_ai = MedicalAssistantAI()
        
        if request.user.is_authenticated:
            # Store chat in the database for logged-in users
            conversation, _ = Conversation.objects.get_or_create(
                session_id=session_id,
                defaults={'user': request.user}
            )

            Message.objects.create(
                conversation=conversation,
                role='user',
                content=user_message
            )
            
            # Retrieve conversation history
            conversation_history = list(conversation.messages.all().order_by('timestamp'))
            
            # Generate AI response
            ai_response = medical_ai.generate_response(conversation_history)
            
            # Store AI response
            Message.objects.create(
                conversation=conversation,
                role='assistant',
                content=ai_response
            )
        else:
            # Handle guest users with session storage
            conversation_history = request.session.get('guest_messages', [])
            
            # Add user message to history
            conversation_history.append({'role': 'user', 'content': user_message})
            
            # Generate AI response
            ai_response = medical_ai.generate_response(conversation_history)
            
            # Add AI response to history
            conversation_history.append({'role': 'assistant', 'content': ai_response})
            
            # Update session
            request.session['guest_messages'] = conversation_history

        return Response({
            'user_message': user_message,
            'ai_response': ai_response
        })