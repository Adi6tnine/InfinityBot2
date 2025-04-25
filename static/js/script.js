document.addEventListener('DOMContentLoaded', function() {
    // DOM Elements
    const chatMessages = document.getElementById('chat-messages');
    const chatForm = document.getElementById('chat-form');
    const userInput = document.getElementById('user-input');
    const themeToggle = document.getElementById('theme-toggle');
    const clearChatBtn = document.getElementById('clear-chat');
    const chatHistoryBtn = document.getElementById('chat-history-btn');
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
        // Get DOM elements
        const sidebar = document.querySelector('.sidebar');
        const chatMain = document.querySelector('.chat-main');
        
        // Toggle the sidebar visibility
        if (sidebar.classList.contains('sidebar-hidden')) {
            // Show sidebar
            sidebar.classList.remove('sidebar-hidden');
            chatMain.classList.remove('chat-main-full');
            toggleSidebarBtn.querySelector('i').className = 'fas fa-bars';
            toggleSidebarBtn.setAttribute('title', 'Hide sidebar');
            localStorage.setItem('sidebar-visible', 'true');
        } else {
            // Hide sidebar
            sidebar.classList.add('sidebar-hidden');
            chatMain.classList.add('chat-main-full');
            toggleSidebarBtn.querySelector('i').className = 'fas fa-expand';
            toggleSidebarBtn.setAttribute('title', 'Show sidebar');
            localStorage.setItem('sidebar-visible', 'false');
        }
        
        // Force a reflow
        setTimeout(() => {
            window.dispatchEvent(new Event('resize'));
        }, 300);
    }
    
    // Initialize sidebar state from localStorage
    function initializeSidebar() {
        const sidebarVisible = localStorage.getItem('sidebar-visible');
        const sidebar = document.querySelector('.sidebar');
        const chatMain = document.querySelector('.chat-main');
        
        // If user previously set sidebar to hidden, hide it now
        if (sidebarVisible === 'false') {
            sidebar.classList.add('sidebar-hidden');
            chatMain.classList.add('chat-main-full');
            toggleSidebarBtn.querySelector('i').className = 'fas fa-expand';
            toggleSidebarBtn.setAttribute('title', 'Show sidebar');
        } else {
            // Default is visible sidebar
            sidebar.classList.remove('sidebar-hidden');
            chatMain.classList.remove('chat-main-full');
            toggleSidebarBtn.querySelector('i').className = 'fas fa-bars';
            toggleSidebarBtn.setAttribute('title', 'Hide sidebar');
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
    
    // Chat history button should toggle the chat history view
    if (chatHistoryBtn) {
        chatHistoryBtn.addEventListener('click', function() {
            // Toggle chat history display
            const chatHistoryDiv = document.querySelector('.chat-history');
            if (chatHistoryDiv) {
                // First, fetch the latest chat history
                fetch('/get_history')
                    .then(response => response.json())
                    .then(data => {
                        // Clear previous history items
                        chatHistoryDiv.innerHTML = '';
                        
                        if (data.history && data.history.length > 0) {
                            // Group messages by conversation
                            const conversations = [];
                            let currentConvo = [];
                            
                            data.history.forEach((msg, index) => {
                                currentConvo.push(msg);
                                
                                // If this is a bot message and there's no next message or next message is from user,
                                // consider this the end of a conversation
                                if (msg.role === 'assistant' && 
                                    (index === data.history.length - 1 || 
                                     data.history[index + 1].role === 'user')) {
                                    conversations.push([...currentConvo]);
                                    currentConvo = [];
                                }
                            });
                            
                            // If there's anything left in currentConvo, add it
                            if (currentConvo.length > 0) {
                                conversations.push(currentConvo);
                            }
                            
                            // Create history items for each conversation (showing just the first exchange)
                            conversations.forEach((convo, i) => {
                                if (convo.length > 0) {
                                    // Find first user message
                                    const userMsg = convo.find(msg => msg.role === 'user');
                                    if (userMsg) {
                                        const historyItem = document.createElement('div');
                                        historyItem.className = 'history-item';
                                        historyItem.innerHTML = `
                                            <div class="history-item-content">
                                                <i class="fas fa-comment-alt"></i>
                                                <span>${userMsg.content.substring(0, 30)}${userMsg.content.length > 30 ? '...' : ''}</span>
                                            </div>
                                        `;
                                        
                                        // Add click event to load this conversation
                                        historyItem.addEventListener('click', function() {
                                            // Clear current chat and load this conversation
                                            chatMessages.innerHTML = '';
                                            
                                            // Add all messages from this conversation
                                            convo.forEach(msg => {
                                                addMessage(msg.content, msg.role === 'user', msg.time);
                                            });
                                            
                                            // If on mobile, close the sidebar
                                            if (window.innerWidth <= 768) {
                                                toggleSidebar();
                                            }
                                        });
                                        
                                        chatHistoryDiv.appendChild(historyItem);
                                    }
                                }
                            });
                            
                            // Add a style element for history items if it doesn't exist
                            if (!document.getElementById('history-style')) {
                                const style = document.createElement('style');
                                style.id = 'history-style';
                                style.textContent = `
                                    .history-item {
                                        padding: 10px;
                                        border-radius: var(--border-radius);
                                        background-color: var(--sidebar-hover);
                                        margin-bottom: 8px;
                                        cursor: pointer;
                                        transition: var(--transition);
                                    }
                                    .history-item:hover {
                                        background-color: var(--button-hover);
                                    }
                                    .history-item-content {
                                        display: flex;
                                        align-items: center;
                                        gap: 10px;
                                    }
                                    .history-item-content i {
                                        color: var(--primary-color);
                                    }
                                `;
                                document.head.appendChild(style);
                            }
                        } else {
                            chatHistoryDiv.innerHTML = '<div class="no-history">No chat history yet</div>';
                        }
                    })
                    .catch(error => {
                        console.error('Error loading chat history:', error);
                        chatHistoryDiv.innerHTML = '<div class="no-history">Error loading chat history</div>';
                    });
            }
        });
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
