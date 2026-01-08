# AI Personal Health Assistant

A **web-based AI Personal Health Assistant** that provides friendly, evidence-based health guidance across multiple categories such as general wellness, nutrition, fitness, mental health, symptoms, and more. Built with **Python**, **Flask**, and **Google Gemini API**, this assistant can interact with users, analyze symptoms, suggest tips, and maintain a personalized user profile.

---

## 🌟 Features

- **Chat Interface**: Conversational AI assistant with user-friendly chat bubbles.  
- **Health Categories**: General, Nutrition, Fitness, Mental, Symptoms, Chronic, Sleep, Emergency.  
- **Symptom Analysis**: Analyze user-reported symptoms and provide guidance.    
- **Clear Chat Option**: Reset chat history with one click.  
- **Responsive Design**: Mobile and desktop-friendly interface.  
- **Safety Disclaimer**: Reminds users this is AI guidance, not a substitute for professional medical advice.  

---

## 🛠 Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript  
- **Backend**: Python, Flask  
- **AI**: Google Gemini API (`gemini-2.5-flash` model)  
- **Session Management**: Flask session  
- **CORS Support**: `flask-cors`  

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
