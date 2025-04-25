import os
import json
import logging
import datetime
from flask import Flask, render_template, request, jsonify
from utils.web_search import search_web, search_wikipedia
from knowledge import (
    general, science, technology, geography, 
    india, jokes, datetime_info
)

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "infinity_bot_secret_key")

# Chat history
chat_history = []

# Knowledge modules list
knowledge_modules = [
    general, science, technology, geography, 
    india, jokes, datetime_info
]

def get_current_time():
    """Get formatted current time"""
    now = datetime.datetime.now()
    return now.strftime("%H:%M")

def search_knowledge_base(query):
    """Search through all knowledge modules for an answer"""
    
    # Check all knowledge modules
    for module in knowledge_modules:
        response = module.get_response(query)
        if response:
            return response
    
    return None

def generate_fallback_response(query):
    """Generate a fallback response when no direct answer is found"""
    
    # Template responses
    templates = [
        "That's an interesting question about {topic}. Let me share what I know...",
        "Regarding {topic}, I can tell you that...",
        "When it comes to {topic}, there are a few things to consider...",
        "I understand you're asking about {topic}. Here's what I can tell you...",
        "Let me provide some information about {topic}..."
    ]
    
    # Extract topic from query (simple approach)
    words = query.split()
    if len(words) > 3:
        topic = " ".join(words[1:4])
    else:
        topic = query
    
    # Get Wikipedia info if possible
    wiki_result = search_wikipedia(query)
    if wiki_result:
        import random
        prefix = random.choice(templates).format(topic=topic)
        return f"{prefix} {wiki_result}"
    
    # If no Wikipedia result, try web search
    web_result = search_web(query)
    if web_result:
        import random
        prefix = random.choice(templates).format(topic=topic)
        return f"{prefix} {web_result}"
    
    # Ultimate fallback
    return "I don't have specific information about that topic yet, but I'm constantly learning. Could you try asking in a different way or about another subject?"

@app.route('/')
def index():
    """Render the main chat interface"""
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """Process incoming chat messages"""
    data = request.json
    user_message = data.get('message', '').strip()
    
    if not user_message:
        return jsonify({
            'message': 'Please enter a message',
            'time': get_current_time()
        })
    
    # Add user message to chat history
    chat_history.append({
        'role': 'user',
        'content': user_message,
        'time': get_current_time()
    })
    
    # Log the incoming request
    logger.debug(f"Received message: {user_message}")
    
    # Get current time info if asked
    if any(word in user_message.lower() for word in ['time', 'date', 'day', 'today']):
        time_response = datetime_info.get_current_datetime_info(user_message)
        if time_response:
            bot_response = time_response
            logger.debug(f"Time/date response: {bot_response}")
            chat_history.append({
                'role': 'assistant',
                'content': bot_response,
                'time': get_current_time()
            })
            return jsonify({
                'message': bot_response,
                'time': get_current_time()
            })
    
    # Check for jokes
    if 'joke' in user_message.lower():
        joke = jokes.get_random_joke()
        if joke:
            logger.debug(f"Joke response: {joke}")
            chat_history.append({
                'role': 'assistant',
                'content': joke,
                'time': get_current_time()
            })
            return jsonify({
                'message': joke,
                'time': get_current_time()
            })
    
    # Search knowledge base
    knowledge_response = search_knowledge_base(user_message)
    
    if knowledge_response:
        logger.debug(f"Knowledge base response: {knowledge_response}")
        bot_response = knowledge_response
    else:
        # Try fallback response
        logger.debug("No direct knowledge found, generating fallback response")
        bot_response = generate_fallback_response(user_message)
    
    # Add bot response to chat history
    chat_history.append({
        'role': 'assistant',
        'content': bot_response,
        'time': get_current_time()
    })
    
    # Keep chat history manageable (maximum 50 messages)
    if len(chat_history) > 50:
        chat_history.pop(0)
    
    return jsonify({
        'message': bot_response,
        'time': get_current_time()
    })

@app.route('/api/suggestions', methods=['GET'])
def get_suggestions():
    """Return a list of suggested prompts"""
    suggestions = [
        "Tell me a joke",
        "What is artificial intelligence?",
        "Facts about India",
        "What's the current time?",
        "How does the solar system work?",
        "Tell me about quantum computing",
        "What are the major cities in Europe?"
    ]
    return jsonify({'suggestions': suggestions})

@app.route('/api/history', methods=['GET'])
def get_history():
    """Return chat history"""
    return jsonify({'history': chat_history})

# Configure port for Render deployment
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
