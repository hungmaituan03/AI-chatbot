from openai import OpenAI
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import os

# Load API key securely
OpenAI.api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])  # Allow frontend origin

@app.route('/chat', methods=['POST'])
@cross_origin(automatic_options=True)
def chat():
    try:
        user_input = request.json.get('message', '').strip()
        if not user_input:
            return jsonify({'error': 'No message provided'}), 400

        # Use chat completion (correct API call)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}],
            max_tokens=150
        )

        return jsonify({'response': response.choices[0].message.content.strip()})

    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
