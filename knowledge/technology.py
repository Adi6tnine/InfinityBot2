"""
Technology knowledge module for InfinityBot
Contains information about various technology topics
"""

import re

# Technology knowledge dictionary
tech_knowledge = {
    "artificial intelligence": """Artificial Intelligence (AI) refers to computer systems designed to perform tasks that typically require human intelligence. These include learning, reasoning, problem-solving, perception, and language understanding. AI can be categorized as narrow (designed for specific tasks) or general (capable of performing any intellectual task that a human can do).""",
    
    "machine learning": """Machine Learning is a subset of artificial intelligence that enables systems to learn and improve from experience without being explicitly programmed. It focuses on developing algorithms that can access data, learn from it, and make predictions or decisions. Common types include supervised learning, unsupervised learning, and reinforcement learning.""",
    
    "deep learning": """Deep Learning is a specialized form of machine learning that uses neural networks with many layers (hence "deep"). These neural networks are inspired by the structure of the human brain and excel at recognizing patterns in unstructured data like images, sound, and text. Deep learning powers many modern AI applications like image recognition, speech recognition, and natural language processing.""",
    
    "blockchain": """Blockchain is a decentralized, distributed ledger technology that records transactions across multiple computers. Each record (block) is linked and secured using cryptography, making the system resistant to data modification. While best known for supporting cryptocurrencies like Bitcoin, blockchain has applications in supply chain management, voting systems, and identity verification.""",
    
    "cryptocurrency": """Cryptocurrency is a digital or virtual currency that uses cryptography for security and operates on blockchain technology. Unlike traditional currencies issued by governments (fiat), cryptocurrencies are typically decentralized and not controlled by any central authority. Bitcoin, created in 2009, was the first cryptocurrency, followed by thousands of others like Ethereum, Ripple, and Litecoin.""",
    
    "internet of things": """The Internet of Things (IoT) refers to the network of physical objects embedded with sensors, software, and other technologies to connect and exchange data with other devices and systems over the internet. Examples include smart home devices, wearable fitness trackers, connected appliances, and industrial sensors.""",
    
    "cloud computing": """Cloud computing provides on-demand delivery of computing resources—including storage, processing power, databases, networking, software, and analytics—over the internet. This model eliminates the need to maintain physical infrastructure and allows users to pay only for the resources they use. Major providers include Amazon Web Services (AWS), Microsoft Azure, and Google Cloud Platform.""",
    
    "virtual reality": """Virtual Reality (VR) is a technology that creates a simulated environment, typically experienced through a headset. It immerses users in a completely virtual world, often allowing them to interact with this environment. VR has applications in gaming, education, healthcare, training, and many other fields.""",
    
    "augmented reality": """Augmented Reality (AR) overlays digital information—like images, text, or 3D models—onto the real world. Unlike VR, AR enhances rather than replaces reality. Popular examples include smartphone games like Pokémon GO, AR filters on social media platforms, and applications for interior design or trying on clothing virtually.""",
    
    "5g": """5G is the fifth generation of mobile network technology, offering significantly faster data speeds, lower latency, and more capacity than previous generations. With speeds up to 100 times faster than 4G, 5G enables new applications in areas like autonomous vehicles, smart cities, and remote surgery, while supporting the growing Internet of Things ecosystem.""",
    
    "quantum computing": """Quantum computing uses quantum mechanics principles to process information in ways classical computers cannot. While classical computers use bits (0 or 1), quantum computers use quantum bits or qubits, which can exist in multiple states simultaneously through superposition. This potentially allows quantum computers to solve certain complex problems much faster than classical computers.""",
    
    "cybersecurity": """Cybersecurity involves protecting computer systems, networks, and data from digital attacks. These include unauthorized access, data theft, malware, phishing, and ransomware. As our reliance on digital technology grows, cybersecurity has become increasingly important for individuals, businesses, and governments to protect sensitive information and maintain operational continuity.""",
    
    "big data": """Big Data refers to extremely large and complex data sets that traditional data processing applications cannot handle effectively. It's characterized by the "three Vs": volume (large amounts), velocity (high speed of generation), and variety (different types). Big Data analytics involves examining these data sets to uncover patterns, correlations, and insights that can inform business decisions.""",
    
    "robotics": """Robotics is the interdisciplinary field of science and engineering focused on designing, constructing, and using robots—machines capable of carrying out tasks autonomously or semi-autonomously. Modern robotics integrates mechanical engineering, electronic engineering, information engineering, computer science, and other disciplines. Robots are used in manufacturing, medicine, exploration, and many other areas."""
}

def get_response(query):
    """
    Check if the query matches any technology knowledge entry
    Returns the corresponding answer or None if no match
    """
    # Convert query to lowercase for case-insensitive matching
    query_lower = query.lower()
    
    # Check for exact matches or keywords
    for key, value in tech_knowledge.items():
        if key in query_lower:
            return value
    
    # Check for specific technology questions with regex patterns
    if re.search(r'what is (ai|artificial intelligence)', query_lower):
        return tech_knowledge.get("artificial intelligence")
    
    if re.search(r'what is (machine learning|ml)', query_lower):
        return tech_knowledge.get("machine learning")
    
    if re.search(r'what is (deep learning|dl)', query_lower):
        return tech_knowledge.get("deep learning")
    
    if re.search(r'what is (vr|virtual reality)', query_lower):
        return tech_knowledge.get("virtual reality")
    
    if re.search(r'what is (ar|augmented reality)', query_lower):
        return tech_knowledge.get("augmented reality")
    
    if re.search(r'explain (blockchain|cryptocurrency|bitcoin)', query_lower):
        if 'blockchain' in query_lower:
            return tech_knowledge.get("blockchain")
        elif 'cryptocurrency' in query_lower or 'bitcoin' in query_lower:
            return tech_knowledge.get("cryptocurrency")
    
    if re.search(r'what is (iot|internet of things)', query_lower):
        return tech_knowledge.get("internet of things")
    
    if re.search(r'what is (5g|fifth generation)', query_lower):
        return tech_knowledge.get("5g")
    
    if re.search(r'what is (quantum computing)', query_lower):
        return tech_knowledge.get("quantum computing")
    
    # No match found
    return None
