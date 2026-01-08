from flask import Flask, render_template, request, jsonify, session
from flask_cors import CORS
import google.generativeai as genai
import os
from datetime import datetime
import json
import re

app = Flask(__name__)
app.secret_key = os.urandom(24)
CORS(app)

# Configure Gemini API
genai.configure(api_key="GOOGLE_API_KEY")

model = genai.GenerativeModel("gemini-2.5-flash")

# Health categories
HEALTH_CATEGORIES = {
    "general": "General health advice and wellness tips",
    "nutrition": "Diet planning, nutrition advice, meal suggestions",
    "fitness": "Exercise routines, workout plans, fitness tips",
    "mental": "Mental health, stress management, mindfulness",
    "symptoms": "Symptom analysis and recommendations",
    "chronic": "Chronic condition management",
    "sleep": "Sleep hygiene and improvement tips",
    "emergency": "Emergency guidance and when to seek help"
}

# Initialize conversation history in session
@app.before_request
def initialize_session():
    if 'conversation_history' not in session:
        session['conversation_history'] = []
    if 'user_profile' not in session:
        session['user_profile'] = {
            'age': None,
            'gender': None,
            'weight': None,
            'height': None,
            'conditions': [],
            'allergies': [],
            'medications': []
        }

@app.route('/')
def index():
    return render_template('index.html', categories=HEALTH_CATEGORIES)

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message', '')
        category = data.get('category', 'general')
        update_profile = data.get('update_profile', False)
        
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
        
        if update_profile and 'profile_data' in data:
            update_user_profile(data['profile_data'])
        
        context = prepare_context(category, user_message)
        
        prompt = f"""You are a professional, empathetic, and knowledgeable Personal Health Assistant.
        
        {context}
        
        User's message: {user_message}
        
        Please provide:
        1. Clear, evidence-based health advice
        2. Specific recommendations when appropriate
        3. Safety precautions and disclaimers
        4. Suggestions for when to consult a healthcare professional
        5. Encouraging and supportive tone
        
        IMPORTANT: Always include a disclaimer that you are an AI assistant and not a substitute for professional medical advice.
        
        Format your response with clear headings, bullet points for lists, and emphasize important points with **bold text**."""
        
        response = model.generate_content(prompt)
        
        conversation_entry = {
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'user': user_message,
            'assistant': response.text,
            'category': category
        }
        
        session['conversation_history'].append(conversation_entry)
        session.modified = True
        
        extracted_info = extract_profile_info(user_message)
        if extracted_info:
            return jsonify({
                'response': response.text,
                'suggest_profile_update': True,
                'extracted_info': extracted_info
            })
        
        return jsonify({
            'response': response.text,
            'suggest_profile_update': False
        })
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/save_profile', methods=['POST'])
def save_profile():
    try:
        data = request.json
        update_user_profile(data)
        return jsonify({'success': True, 'message': 'Profile updated successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get_conversation_history', methods=['GET'])
def get_conversation_history():
    return jsonify(session.get('conversation_history', []))

@app.route('/clear_history', methods=['POST'])
def clear_history():
    session['conversation_history'] = []
    session.modified = True
    return jsonify({'success': True})

@app.route('/get_health_tips', methods=['GET'])
def get_health_tips():
    category = request.args.get('category', 'general')
    
    prompt = f"""Provide 3-5 actionable health tips for {category} category.
    Format as a numbered list with clear, practical advice."""
    
    try:
        response = model.generate_content(prompt)
        return jsonify({'tips': response.text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/analyze_symptoms', methods=['POST'])
def analyze_symptoms():
    data = request.json
    symptoms = data.get('symptoms', '')
    
    prompt = f"""User reports these symptoms: {symptoms}
    
    Please provide:
    1. Possible conditions these symptoms might indicate
    2. Immediate actions to take
    3. When to seek emergency care
    4. Home remedies that might help
    5. Questions to ask a healthcare provider
    
    Remember to emphasize that this is not a diagnosis and professional medical evaluation is essential."""
    
    try:
        response = model.generate_content(prompt)
        
        conversation_entry = {
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'user': f"Symptom analysis request: {symptoms}",
            'assistant': response.text,
            'category': 'symptoms'
        }
        
        session['conversation_history'].append(conversation_entry)
        session.modified = True
        
        return jsonify({'analysis': response.text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def prepare_context(category, user_message):
    user_profile = session.get('user_profile', {})
    
    context = f"""
    User Profile (if available):
    - Age: {user_profile.get('age', 'Not specified')}
    - Gender: {user_profile.get('gender', 'Not specified')}
    - Weight: {user_profile.get('weight', 'Not specified')}
    - Height: {user_profile.get('height', 'Not specified')}
    - Medical Conditions: {', '.join(user_profile.get('conditions', [])) or 'Not specified'}
    - Allergies: {', '.join(user_profile.get('allergies', [])) or 'Not specified'}
    - Medications: {', '.join(user_profile.get('medications', [])) or 'Not specified'}
    
    Health Category: {category}
    Category Description: {HEALTH_CATEGORIES.get(category, 'General health advice')}
    """
    
    return context

def update_user_profile(profile_data):
    session['user_profile'].update({
        'age': profile_data.get('age', session['user_profile'].get('age')),
        'gender': profile_data.get('gender', session['user_profile'].get('gender')),
        'weight': profile_data.get('weight', session['user_profile'].get('weight')),
        'height': profile_data.get('height', session['user_profile'].get('height')),
        'conditions': profile_data.get('conditions', session['user_profile'].get('conditions')),
        'allergies': profile_data.get('allergies', session['user_profile'].get('allergies')),
        'medications': profile_data.get('medications', session['user_profile'].get('medications'))
    })
    session.modified = True

def extract_profile_info(message):
    patterns = {
        'age': r'(\d+)\s*(?:years? old|yo|age)',
        'weight': r'(\d+)\s*(?:kg|kilos|kilograms?|pounds?|lbs)',
        'height': r'(\d+\'?\d*)\s*(?:cm|meters?|\'|ft|feet)',
    }
    
    extracted = {}
    for key, pattern in patterns.items():
        match = re.search(pattern, message.lower())
        if match:
            extracted[key] = match.group(1)
    
    return extracted if extracted else None

if __name__ == '__main__':
    app.run(debug=True, port=5000)

