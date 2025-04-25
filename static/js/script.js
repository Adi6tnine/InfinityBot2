document.addEventListener('DOMContentLoaded', function() {
    // DOM Elements
    const chatMessages = document.getElementById('chat-messages');
    const chatForm = document.getElementById('chat-form');
    const userInput = document.getElementById('user-input');
    const themeToggle = document.getElementById('theme-toggle');
    const clearChatBtn = document.getElementById('clear-chat');
    const newChatBtn = document.getElementById('new-chat');
    const toggleSidebarBtn = document.getElementById('toggle-sidebar');
    const sidebar = document.querySelector('.sidebar');
    const chatMain = document.querySelector('.chat-main');
    
    // Set up particles.js
    if (typeof particlesJS !== 'undefined') {
        particlesJS('particles-js', {
            particles: {
                number: { value: 20, density: { enable: true, value_area: 800 } },
                color: { value: '#6c5ce7' },
                shape: { type: 'circle' },
                opacity: { value: 0.3, random: true },
                size: { value: 3, random: true },
                line_linked: { enable: true, distance: 150, color: '#6c5ce7', opacity: 0.2, width: 1 },
                move: { enable: true, speed: 1.5, direction: 'none', random: true, straight: false, out_mode: 'out' }
            },
            interactivity: {
                detect_on: 'canvas',
                events: {
                    onhover: { enable: true, mode: 'grab' },
                    onclick: { enable: true, mode: 'push' },
                    resize: true
                },
                modes: {
                    grab: { distance: 140, line_linked: { opacity: 0.5 } },
                    push: { particles_nb: 3 }
                }
            },
            retina_detect: true
        });
    }
    
    // Toggle sidebar visibility
    function toggleSidebar() {
        // Toggle the sidebar class
        sidebar.classList.toggle('sidebar-hidden');
        
        // Get the chat main element and add or remove the full width class
        document.querySelector('.chat-main').classList.toggle('chat-main-full');
        
        // Update the icon for toggle button
        const icon = toggleSidebarBtn.querySelector('i');
        if (sidebar.classList.contains('sidebar-hidden')) {
            icon.className = 'fas fa-expand';
            toggleSidebarBtn.setAttribute('title', 'Show sidebar');
        } else {
            icon.className = 'fas fa-bars';
            toggleSidebarBtn.setAttribute('title', 'Hide sidebar');
        }
        
        // Save preference in localStorage
        localStorage.setItem('sidebar-visible', !sidebar.classList.contains('sidebar-hidden'));
        
        // Force a window resize event to re-render the UI properly
        window.dispatchEvent(new Event('resize'));
    }
    
    // Initialize sidebar state from localStorage
    function initializeSidebar() {
        const sidebarVisible = localStorage.getItem('sidebar-visible');
        // Default to visible sidebar if no preference saved
        if (sidebarVisible === 'false') {
            toggleSidebar();
        }
    }
    
    // Variables
    let typingTimeout;
    
    // Theme Toggle
    function initializeTheme() {
        const savedTheme = localStorage.getItem('theme') || 'dark';
        document.documentElement.setAttribute('data-bs-theme', savedTheme);
        updateThemeIcon(savedTheme === 'dark');
    }
    
    function updateThemeIcon(isDark) {
        const themeIcon = themeToggle.querySelector('i');
        if (isDark) {
            themeIcon.className = 'fas fa-sun me-2';
        } else {
            themeIcon.className = 'fas fa-moon me-2';
        }
    }
    
    themeToggle.addEventListener('click', function() {
        const currentTheme = document.documentElement.getAttribute('data-bs-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        
        document.documentElement.setAttribute('data-bs-theme', newTheme);
        localStorage.setItem('theme', newTheme);
        updateThemeIcon(newTheme === 'dark');
    });
    
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
    
    // Add welcome message
    function addWelcomeMessage() {
        const time = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
        const messageHtml = `
            <div class="message bot-message">
                <div class="message-bubble bot-bubble">
                    <div>Hello! I'm Infinity AI, your personal assistant. How can I help you today?</div>
                    <div class="message-time">${time}</div>
                </div>
            </div>
        `;
        chatMessages.innerHTML = messageHtml;
    }
    
    // Add a message to the chat
    function addMessage(content, isUser, time) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${isUser ? 'user-message' : 'bot-message'}`;
        
        const formattedContent = isUser ? content : formatMessageContent(content);
        
        messageDiv.innerHTML = `
            <div class="message-bubble ${isUser ? 'user-bubble' : 'bot-bubble'}">
                <div>${formattedContent}</div>
                <div class="message-time">${time}</div>
            </div>
        `;
        
        chatMessages.appendChild(messageDiv);
        scrollToBottom();
    }
    
    function scrollToBottom() {
        const chatContainer = document.getElementById('chat-container');
        chatContainer.scrollTop = chatContainer.scrollHeight;
    }
    
    // Show typing indicator
    function showTypingIndicator() {
        const typingDiv = document.createElement('div');
        typingDiv.id = 'typing-indicator';
        typingDiv.className = 'message bot-message';
        typingDiv.innerHTML = `
            <div class="typing-indicator">
                <span></span>
                <span></span>
                <span></span>
            </div>
        `;
        
        // Remove existing typing indicator if any
        const existingIndicator = document.getElementById('typing-indicator');
        if (existingIndicator) {
            existingIndicator.remove();
        }
        
        chatMessages.appendChild(typingDiv);
        scrollToBottom();
    }
    
    // Hide typing indicator
    function hideTypingIndicator() {
        const typingIndicator = document.getElementById('typing-indicator');
        if (typingIndicator) {
            typingIndicator.remove();
        }
    }
    
    // Simulate typing effect for bot messages
    function simulateTyping(message, time) {
        const minTypingTime = 500;  // Minimum typing time in ms
        const typingSpeed = 20;     // Characters per second
        
        // Calculate a realistic typing time based on message length
        const messageLength = message.length;
        const calculatedTime = Math.max(minTypingTime, messageLength * typingSpeed);
        
        // Cap typing time to be between 500ms and 3.5s
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
            const response = await fetch('/chat', {
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
            simulateTyping(data.response, new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }));
        } catch (error) {
            console.error('Error sending message:', error);
            hideTypingIndicator();
            addMessage('Sorry, I encountered an error processing your message. Please try again.', false, new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }));
        }
    }
    
    // Load chat history if available
    async function loadChatHistory() {
        try {
            const response = await fetch('/get_history');
            if (!response.ok) {
                // If no history, add welcome message
                addWelcomeMessage();
                return;
            }
            
            const data = await response.json();
            if (data.history && data.history.length > 0) {
                // Add messages from history
                data.history.forEach(message => {
                    addMessage(message.content, message.role === 'user', message.time);
                });
            } else {
                // Add welcome message if no history
                addWelcomeMessage();
            }
        } catch (error) {
            console.error('Error loading chat history:', error);
            addWelcomeMessage();
        }
    }
    
    // Clear chat history
    function clearChat() {
        chatMessages.innerHTML = '';
        addWelcomeMessage();
        
        // Send request to clear history on the server
        fetch('/clear_history', { method: 'POST' })
            .catch(error => console.error('Error clearing chat history:', error));
    }
    
    // Event Listeners
    chatForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const message = userInput.value.trim();
        if (!message) return;
        
        const time = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
        addMessage(message, true, time);
        
        userInput.value = '';
        
        sendMessage(message);
    });
    
    // Clear chat history button
    clearChatBtn.addEventListener('click', clearChat);
    
    // New chat button (same as clear chat for now)
    if (newChatBtn) {
        newChatBtn.addEventListener('click', clearChat);
    }
    
    // Press Enter to send message (no Shift+Enter needed for single-line input)
    userInput.addEventListener('keydown', function(e) {
        if (e.key === 'Enter') {
            e.preventDefault();
            if (userInput.value.trim()) {
                chatForm.dispatchEvent(new Event('submit'));
            }
        }
    });

    // Focus the input field on page load
    userInput.focus();
    
    // Toggle sidebar button
    if (toggleSidebarBtn) {
        toggleSidebarBtn.addEventListener('click', toggleSidebar);
    }
    
    // Initialize
    initializeTheme();
    initializeSidebar();
    loadChatHistory();
});
