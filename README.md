

---


# 🩺 AtHeal — AI-Powered Telemedicine Platform

[Live Demo](https://atheal.onrender.com) • [Developer](https://github.com/Alokbabuyadhuvanshi)

AtHeal is an AI-integrated telemedicine web application that enables patients to consult with doctors remotely. It streamlines healthcare access through secure video consultations, intelligent symptom assessment, and a sleek 3D interface for enhanced user engagement.

---

## 🚀 Features

### 🔬 AI Health Assistant
- Assists users with their health-related problems through intelligent conversation.
- Uses NLP to analyze user input and provide initial guidance or symptom insights.
- Offers a supportive, AI-driven experience to help users understand potential health issues before consulting a doctor.

### 🎥 Secure Video Consultation
- Enables real-time video calls between doctors and patients
- Ensures 95%+ stable connection rate
- Authentication and access control for session privacy

### 🔐 User Authentication
- Secure login/signup for both patients and doctors
- Role-based access control

### 🧑‍⚕️ Doctor & Patient Dashboards
- Doctor dashboard: View appointments, patient details, join consultations
- Patient dashboard: Book appointments, receive AI health analysis

### 🌀 3D Frontend with Spline API
- Integrated interactive 3D elements for a modern, engaging UI
- Enhances usability and visual appeal

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript, Spline API
- **Backend:** Django
- **Database:** SQLite (can be configured for MySQL/PostgreSQL)
- **Authentication:** Django AllAuth / custom auth
- **APIs:** Custom REST endpoints for communication and data access
- **Deployment:** Render

---

## 📸 Screenshots

![Screenshot 2025-04-24 195322](https://github.com/user-attachments/assets/2c1a4f69-992a-4b05-a8c5-6b8252aa19ad)
![Screenshot 2025-04-24 194553](https://github.com/user-attachments/assets/b526f1f1-d6f0-4ab3-8e59-86604d3cc5f0)




---

## ⚙️ Installation & Setup

```bash
# Clone the repo
git clone https://github.com/Alokbabuyadhuvanshi/AtHeal.git
cd AtHeal

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the server
python manage.py runserver
```

---

## 📂 Folder Structure

```bash
Atheal/
    ├──Telemedition/
    |      ├── appointment/          # Appointment scheduling and booking logic
    |      ├── Doctor/               # Doctor-side functionality and views
    |      ├── Helio/                # Handles user authentication (login, logout, registration)
    |      ├── media/                # Uploaded media (e.g. prescriptions, reports)
    |      ├── medical_assistant/    # AI assistant handling health-related queries
    |      ├── Patient/              # Patient-specific views and models
    |      ├── static/               # Static files (CSS, JavaScript, images)
    |      ├── templates/            # HTML templates for rendering UI
    |      ├── Telemedition/         # Core Django project settings and URLs      
    |      ├── db.sqlite3            # SQLite database (default for dev)
    |      ├── manage.py             # Django project manager
    ├── requirements.txt             # Python dependencies

```

---

## 🧠 Future Improvements

- Add prescription upload and download features
- Real-time chat alongside video calls
- Patient health history tracker
- Integrate multilingual support for a wider audience

---

## 🤝 Contribution

Feel free to fork the repository and submit pull requests. If you'd like to contribute significantly, open an issue to discuss your ideas.

---

## 📬 Contact

**Developer:** Alok Babu  
📧 [alokbabuyadhuvanshi@gmail.com](mailto:alokbabuyadhuvanshi@gmail.com)  
🔗 [LinkedIn](https://linkedin.com/in/alok-babu) • [GitHub](https://github.com/Alokbabuyadhuvanshi)

---

## 📄 License
```

---

Let me know if you want me to generate sample screenshots or icons for this `README` too!
