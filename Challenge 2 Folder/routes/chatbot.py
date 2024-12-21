from flask import Blueprint, request, jsonify
import google.generativeai as genai
import os

# Set up Gemini API key
api_key = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=api_key)

chatbot_bp = Blueprint('chatbot', __name__)

# Chatbot interaction
@chatbot_bp.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    
    if not user_input:
        return jsonify({"error": "Message is required!"}), 400

    try:
        # Generate response using Gemini
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(user_input)
        
        return jsonify({"response": response.text})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
