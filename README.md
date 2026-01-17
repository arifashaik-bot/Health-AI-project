# 🩺 AI Personal Health Assistant

The **AI Personal Health Assistant** is a smart web application designed to provide friendly, personalized, and evidence-based health guidance. Users can chat with the AI assistant, track basic health information, analyze symptoms, receive wellness tips, and explore multiple health categories — all in one intuitive platform.

This project is built using **Python (Flask)** for the backend and integrates **Google Gemini AI** for generating intelligent responses. The frontend has been enhanced with attractive UI/UX for a more engaging experience.

---

## 🌐 Live Demo

👉 Try the live app here:  
**https://c-users-shaik-arifa-onedrive-deskto.vercel.app/**

---

## ✨ Key Features

- 💬 **AI Chat Assistant** – interactive conversational support  
- 🩻 **Symptom Analysis** – analyze symptoms and provide guidance  
- 🍎 **Health Categories**
  - General Health  
  - Nutrition and Diet  
  - Fitness and Exercise  
  - Mental Health  
  - Chronic Conditions  
  - Sleep Health  
  - Emergency Guidance  

- 👤 **User Profile Support**
  - Age, gender, height, weight  
  - Allergies, conditions, medications  

- 📝 **Conversation History** stored during session  
- 🧠 **Actionable Health Tips** generated dynamically  
- 🧹 **Clear Chat Option**  
- 📱 **Responsive & Beautiful UI**  
- ⚠️ **Built-in Medical Disclaimer**

---

## 🛠 Tech Stack

- **Frontend:** HTML5, CSS3, JavaScript  
- **Backend:** Python, Flask  
- **AI Model:** Google Gemini  
- **API Integration:** `google-generativeai`  
- **Styling:** Custom CSS (responsive, modern UI)  
- **Session Handling:** Flask session  
- **CORS:** flask-cors
  
---

## 🚀 Setup and Usage


1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd Health-AI-project
   ```
2. **Check Python Version**:
   ```bash
   python --version
   ```   
3. **Install Required Python Packages**:
   ```bash
   pip install flask flask-cors google-generativeai
   ```
4. **Configure Google Gemini API Key**:
    Get your **Google Gemini API key** from **Google AI Studio**.
    Open the `app.py` file in your project.
    Replace the API key line with your own key:
   ```bash
   genai.configure(api_key="YOUR_GEMINI_API_KEY")
   ```  
5. **Run the Flask Server**:
   ```bash
   python app.py
   ```
6. **Access the Application**:
    Open your browser and go to http://127.0.0.1:5000/

