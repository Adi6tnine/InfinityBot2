document.addEventListener('DOMContentLoaded', function() {
    // DOM Elements
    const chatMessages = document.getElementById('chat-messages');
    const messageForm = document.getElementById('message-form');
    const messageInput = document.getElementById('message-input');
    const sendButton = document.getElementById('send-button');
    const themeToggle = document.getElementById('theme-toggle');
    const welcomeScreen = document.getElementById('welcome-screen');
    const newChatButton = document.getElementById('new-chat');
    const suggestions = document.querySelectorAll('.suggestion');
    const typingIndicator = document.getElementById('typing-indicator');
    
    // Variables
    let isFirstMessage = true;
    let typingTimeout;
    
    // Initialize theme from local storage or default to dark mode
    function initializeTheme() {
        const savedTheme = localStorage.getItem('theme') || 'dark';
        document.body.className = savedTheme + '-mode';
        themeToggle.checked = savedTheme === 'dark';
    }
    
    // Toggle theme between light and dark
    function toggleTheme() {
        const isDarkMode = themeToggle.checked;
        const newTheme = isDarkMode ? 'dark' : 'light';
        document.body.className = newTheme + '-mode';
        localStorage.setItem('theme', newTheme);
    }
    
    // Auto-resize textarea as user types
    function autoResizeTextarea() {
        messageInput.style.height = 'auto';
        messageInput.style.height = (messageInput.scrollHeight > 200 ? 200 : messageInput.scrollHeight) + 'px';
    }
    
    // Show typing indicator
    function showTypingIndicator() {
        typingIndicator.classList.remove('hidden');
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
    
    // Hide typing indicator
    function hideTypingIndicator() {
        typingIndicator.classList.add('hidden');
    }
    
    // Format message content (handle markdown-like formatting)
    function formatMessageContent(content) {
        // Convert line breaks to <br>
        let formatted = content.replace(/\n/g, '<br>');
        
        // Handle code blocks with ```
        formatted = formatted.replace(/```([\s\S]*?)```/g, '<pre>$1</pre>');
        
        // Handle inline code with `
        formatted = formatted.replace(/`([^`]+)`/g, '<code>$1</code>');
        
        // Handle bold with ** or __
        formatted = formatted.replace(/(\*\*|__)(.*?)\1/g, '<strong>$2</strong>');
        
        // Handle italics with * or _
        formatted = formatted.replace(/(\*|_)(.*?)\1/g, '<em>$2</em>');
        
        return formatted;
    }
    
    // Add a message to the chat
    function addMessage(content, isUser, time) {
        // Hide welcome screen if visible
        if (isFirstMessage) {
            welcomeScreen.style.display = 'none';
            isFirstMessage = false;
        }
        
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${isUser ? 'user-message' : 'bot-message'}`;
        
        const formattedContent = isUser ? content : formatMessageContent(content);
        
        messageDiv.innerHTML = `
            <div class="message-content">${formattedContent}</div>
            <div class="message-time">${time}</div>
        `;
        
        chatMessages.appendChild(messageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
    
    // Simulate typing effect for bot messages
    function simulateTyping(message, time) {
        const minTypingTime = 500;  // Minimum typing time in ms
        const typingSpeed = 20;     // Characters per second
        
        // Calculate a realistic typing time based on message length
        const messageLength = message.length;
        const calculatedTime = Math.max(minTypingTime, messageLength * typingSpeed);
        
        // Cap typing time to be between 500ms and it 3.5s
        const typingTime = Math.min(3500, calculatedTime);
        
        showTypingIndicator();
        
        // Clear any existing typing timeout
        if (typingTimeout) {
            clearTimeout(typingTimeout);
        }
        
        // Set new timeout to show the message after typing effect
        typingTimeout = setTimeout(() => {
            hideTypingIndicator();
            addMessage(message, false, time);
        }, typingTime);
    }
    
    // Send a message to the server and get a response
    async function sendMessage(message) {
        try {
            const response = await fetch('/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message })
            });
            
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            
            const data = await response.json();
            simulateTyping(data.message, data.time);
        } catch (error) {
            console.error('Error sending message:', error);
            hideTypingIndicator();
            addMessage('Sorry, I encountered an error processing your message. Please try again.', false, new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }));
        }
    }
    
    // Load chat history if available
    async function loadChatHistory() {
        try {
            const response = await fetch('/api/history');
            if (!response.ok) {
                return; // If no history or error, just continue with empty chat
            }
            
            const data = await response.json();
            if (data.history && data.history.length > 0) {
                // Hide welcome screen
                welcomeScreen.style.display = 'none';
                isFirstMessage = false;
                
                // Add messages from history
                data.history.forEach(message => {
                    addMessage(message.content, message.role === 'user', message.time);
                });
            }
        } catch (error) {
            console.error('Error loading chat history:', error);
        }
    }
    
    // Start a new chat
    function startNewChat() {
        // Clear chat messages
        chatMessages.innerHTML = '';
        
        // Show welcome screen
        welcomeScreen.style.display = 'flex';
        isFirstMessage = true;
        
        // Clear input field
        messageInput.value = '';
        autoResizeTextarea();
    }
    
    // Load suggestions
    async function loadSuggestions() {
        try {
            const response = await fetch('/api/suggestions');
            if (!response.ok) {
                return;
            }
            
            const data = await response.json();
            if (data.suggestions && data.suggestions.length > 0) {
                // Update the suggestions with the ones from the server
                const suggestionsContainer = document.querySelector('.suggestions');
                suggestionsContainer.innerHTML = '';
                
                data.suggestions.forEach(suggestion => {
                    const div = document.createElement('div');
                    div.className = 'suggestion';
                    div.dataset.text = suggestion;
                    
                    // Add icon based on suggestion content
                    let icon = 'fas fa-comment';
                    if (suggestion.toLowerCase().includes('joke')) {
                        icon = 'far fa-laugh';
                    } else if (suggestion.toLowerCase().includes('time')) {
                        icon = 'far fa-clock';
                    } else if (suggestion.toLowerCase().includes('artificial intelligence')) {
                        icon = 'fas fa-robot';
                    } else if (suggestion.toLowerCase().includes('india')) {
                        icon = 'fas fa-info-circle';
                    } else if (suggestion.toLowerCase().includes('solar')) {
                        icon = 'fas fa-sun';
                    } else if (suggestion.toLowerCase().includes('quantum')) {
                        icon = 'fas fa-microchip';
                    } else if (suggestion.toLowerCase().includes('cities') || suggestion.toLowerCase().includes('europe')) {
                        icon = 'fas fa-globe-europe';
                    }
                    
                    div.innerHTML = `<i class="${icon}"></i> ${suggestion}`;
                    div.addEventListener('click', function() {
                        messageInput.value = this.dataset.text;
                        messageForm.dispatchEvent(new Event('submit'));
                    });
                    
                    suggestionsContainer.appendChild(div);
                });
            }
        } catch (error) {
            console.error('Error loading suggestions:', error);
        }
    }
    
    // Event Listeners
    themeToggle.addEventListener('change', toggleTheme);
    
    messageInput.addEventListener('input', autoResizeTextarea);
    
    messageForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const message = messageInput.value.trim();
        if (!message) return;
        
        const time = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
        addMessage(message, true, time);
        
        messageInput.value = '';
        autoResizeTextarea();
        
        sendMessage(message);
    });
    
    newChatButton.addEventListener('click', startNewChat);
    
    // Setup suggestion clicks
    suggestions.forEach(suggestion => {
        suggestion.addEventListener('click', function() {
            messageInput.value = this.dataset.text;
            messageForm.dispatchEvent(new Event('submit'));
        });
    });
    
    // Press Enter to send message, Shift+Enter for new line
    messageInput.addEventListener('keydown', function(e) {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            if (messageInput.value.trim()) {
                messageForm.dispatchEvent(new Event('submit'));
            }
        }
    });
    
    // Initialize
    initializeTheme();
    autoResizeTextarea();
    loadChatHistory();
    loadSuggestions();
});
