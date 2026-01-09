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

Clone the repository and navigate into the project folder:

```bash
git clone <your-repo-link>
cd <project-folder>
Make sure you have Python 3.8+ installed and check the version:

python --version


Install all required Python packages:

pip install flask flask-cors google-generativeai


Get your Google Gemini API key from Google AI Studio
 and open app.py. Replace the API key line with your key:

genai.configure(api_key="YOUR_GEMINI_API_KEY")


Run the Flask server:

python app.py


Open your browser and go to http://127.0.0.1:5000 to see the AI Personal Health Assistant interface. Select a health category from the dropdown, type your question in the input box, and click Ask to get AI guidance. Chat history will appear in the chat box above, and you can click Clear Chat to reset the conversation. The AI provides structured advice, bullet points, and emphasizes important points in bold, along with a safety disclaimer.
