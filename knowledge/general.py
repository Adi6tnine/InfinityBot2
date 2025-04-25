"""
General knowledge module for InfinityBot
Contains basic information and facts
"""

import re

# Generic knowledge dictionary
knowledge = {
    "infinity bot": "I am InfinityBot, a smart chatbot that works like ChatGPT but with both offline knowledge and web search capabilities. I can answer questions, provide information, and help with various topics.",
    "who are you": "I am InfinityBot, a smart chatbot designed to provide helpful information and answers to your questions. I have a built-in knowledge base and can also search the web for information when needed.",
    "what can you do": "I can answer questions about various topics including science, technology, geography, and more. I can tell jokes, provide current date and time information, and search the web for information I don't have in my knowledge base.",
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there! How can I assist you?",
    "bye": "Goodbye! Feel free to chat again whenever you have questions.",
    "thank you": "You're welcome! I'm glad I could help.",
    "thanks": "You're welcome! Let me know if you need anything else.",
    "help": "I'm here to help answer your questions. You can ask me about various topics, request a joke, or inquire about specific information. What would you like to know?",
    "weather": "I don't have real-time weather capabilities, but you can check your local weather on websites like weather.com or accuweather.com.",
    "how are you": "I'm functioning well, thank you for asking! How can I assist you today?",
    "good morning": "Good morning! How can I help you start your day?",
    "good afternoon": "Good afternoon! What can I help you with today?",
    "good evening": "Good evening! How may I assist you tonight?",
    "favorite color": "As an AI, I don't have personal preferences, but I find all colors fascinating in their own way!",
    "infinity": "Infinity represents something without any limit, and is often denoted by the symbol ∞. The concept is used in mathematics, physics, and philosophy to describe sequences, series, and other concepts that are boundless.",
    "who made you": "I was created by ADARSH. He designed and developed me to be a smart AI assistant that can help answer questions and provide information.",
    "who is your creator": "My creator is ADARSH. He designed and built me to assist users with information and answers.",
    "who created you": "I was created by ADARSH. He's the brilliant mind behind my development and capabilities.",
    "your developer": "I was developed by ADARSH, who built me to be a helpful AI assistant."
}

def get_response(query):
    """
    Check if the query matches any knowledge entry
    Returns the corresponding answer or None if no match
    """
    # Convert query to lowercase for case-insensitive matching
    query_lower = query.lower()
    
    # Exact match check
    for key, value in knowledge.items():
        if key in query_lower:
            return value
    
    # Keyword matching
    for key, value in knowledge.items():
        # Split the key into individual words
        keywords = key.split()
        # Check if all keywords are in the query
        if all(keyword in query_lower for keyword in keywords):
            return value
    
    # No match found
    return None
