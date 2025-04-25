# Infinity AI Chatbot - Project Documentation

## Project Overview
Infinity AI is a sophisticated chatbot that functions like ChatGPT with an elegant UI, offline knowledge base, and web search capabilities. The project has been designed to provide accurate and helpful information through a modern, responsive interface without requiring external paid API services.

## Technology Stack

### Backend
- **Python 3.11**: Core programming language
- **Flask**: Web framework for handling HTTP requests and serving the application
- **Gunicorn**: WSGI HTTP Server for production deployment
- **SQLAlchemy**: ORM for any database operations (for potential future extensions)

### Knowledge and Search
- **Trafilatura**: For extracting text content from HTML websites
- **BeautifulSoup4**: For parsing HTML and extracting data from web pages
- **Requests**: For making HTTP requests to external services
- **Wikipedia**: Python library to access and parse Wikipedia data

### Frontend
- **HTML5/CSS3**: Structure and styling
- **JavaScript (ES6+)**: Client-side interactivity
- **Bootstrap**: Framework for responsive design elements
- **Font Awesome**: For icons and visual elements
- **Particles.js**: For background particle effects
- **Google Fonts (Poppins)**: Typography

## Architecture

### Main Components
1. **Flask Application (`main.py`, `app.py`)**: Entry point and core application logic
2. **Knowledge Modules (`knowledge/`)**: Modular system for storing offline knowledge
   - General knowledge (`general.py`)
   - Date and time information (`datetime_info.py`)
   - Technology information (`technology.py`)
   - Geography information (`geography.py`)
   - Science information (`science.py`)
   - India-specific information (`india.py`)
   - Jokes module (`jokes.py`)
3. **Web Search Utilities (`utils/web_search.py`)**: Functions for searching the web when local knowledge is insufficient
4. **UI Templates (`templates/`)**: HTML templates for the user interface
5. **Static Resources (`static/`)**: CSS, JavaScript, and assets

### Key Features
- **Modular Knowledge System**: Easily extensible with new knowledge domains
- **Fallback Web Search**: Uses Wikipedia and web scraping when local knowledge is not available
- **Responsive UI**: Works on desktop and mobile devices
- **Dark/Light Mode**: Theme toggle for user preference
- **Typing Animation**: Realistic typing animation for bot responses
- **Chat History**: Maintains conversation context within a session
- **New Chat**: Option to start a fresh conversation

## Information Flow
1. User sends a message through the UI
2. The message is sent to the server via AJAX
3. The server processes the message through these steps:
   - Check if the query matches any entry in the knowledge modules
   - If no match, fall back to web search (Wikipedia and general web search)
   - Generate and format a response
4. The response is sent back to the client
5. The UI displays the response with a realistic typing animation

## UI Components
- **Sidebar**: Contains app title, new chat button, theme toggle, and version info
- **Chat Window**: Displays the conversation history
- **Input Area**: For user to type and send messages
- **Typing Indicator**: Visual feedback when the AI is "thinking"

## Deployment
The application is designed to be deployed on Render.com:
- Uses Gunicorn as the WSGI server
- Configured to serve on port 5000
- Includes proper error handling for production use

## Extension Points
The application is designed to be easily extended with:
- Additional knowledge modules by creating new Python files in the knowledge/ directory
- Database integration using Flask-SQLalchemy (already included)
- User authentication (can be added with Flask-Login)
- More advanced web search capabilities
- API integrations with external services

## Project Maintenance
To maintain and update the project:
1. **Adding knowledge**: Create or update Python files in the knowledge/ directory
2. **UI changes**: Modify the HTML templates and CSS files
3. **Adding functionality**: Extend the app.py file with new routes and features

## Version Information
- Current Version: Infinity AI V1.0.0
- Creator: ADARSH