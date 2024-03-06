from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample responses for the chatbot
responses = {
    "hi": "Hello! How can I assist you?",
    "how are you": "I'm doing well, thank you for asking.",
    "bye": "Goodbye! Have a great day!",
    "default": "I'm sorry, I didn't understand that."
}

# Function to process incoming messages
def process_message(message):
    message = message.lower()
    response = responses.get(message, responses["default"])
    return response

# Route to handle incoming messages
@app.route('/chat', methods=['POST'])
def chat():
    message = request.json.get('message')
    response = process_message(message)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)

