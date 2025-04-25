"""
India knowledge module for InfinityBot
Contains information about India's geography, culture, history, etc.
"""

import re

# India knowledge dictionary
india_knowledge = {
    "india general": """India, officially the Republic of India, is a country in South Asia. It is the seventh-largest country by area, the second-most populous country, and the most populous democracy in the world. It shares land borders with Pakistan, China, Nepal, Bhutan, Bangladesh, and Myanmar, and has a coastline along the Indian Ocean.""",
    
    "india geography": """India has diverse geography that includes the Himalayan mountain range in the north, the Indo-Gangetic Plain, the Thar Desert, and coastal regions. The country spans multiple climate zones, from tropical in the south to temperate and alpine in the Himalayan north. Major rivers include the Ganges, Brahmaputra, Yamuna, Godavari, and Krishna.""",
    
    "indian culture": """Indian culture is one of the oldest and most diverse in the world. It encompasses a wide variety of religions, languages, cuisines, arts, and architecture. Hinduism, Buddhism, Jainism, and Sikhism all originated in India. The country has 22 officially recognized languages, with Hindi and English being the most widely used for official purposes.""",
    
    "indian history": """India's history dates back to the Indus Valley Civilization (3300–1300 BCE), one of the world's earliest urban civilizations. Throughout its history, India has been ruled by various dynasties including the Maurya, Gupta, Mughal, and Maratha empires. It was colonized by the British East India Company in the 18th century and became part of the British Empire until gaining independence on August 15, 1947.""",
    
    "indian cuisine": """Indian cuisine is known for its extensive use of spices, herbs, vegetables, and fruits. It varies widely by region, reflecting the diverse demographics of the country. Popular dishes include curry, biryani, dosa, samosa, and tandoori chicken. Vegetarianism is widely practiced in India, influenced by religious traditions like Hinduism and Jainism.""",
    
    "indian government": """India is a sovereign, socialist, secular, democratic republic with a parliamentary system of government. The Constitution of India, which came into effect on January 26, 1950, is the supreme law of the land. The government is structured as a federal system with a central government and 28 states and 8 union territories. The President is the head of state, while the Prime Minister is the head of government.""",
    
    "indian economy": """India is the world's fifth-largest economy by nominal GDP and the third-largest by purchasing power parity (PPP). Key sectors include services, manufacturing, and agriculture. India is a major exporter of software services, pharmaceuticals, textiles, and agricultural products. The country has undergone significant economic reforms since the 1990s, moving towards a more market-oriented economy.""",
    
    "indian festivals": """India celebrates numerous festivals reflecting its cultural and religious diversity. Major Hindu festivals include Diwali (Festival of Lights), Holi (Festival of Colors), and Navratri. Other important celebrations include Eid (celebrated by Muslims), Christmas, Guru Nanak Jayanti (Sikhism), Buddha Purnima (Buddhism), and Mahavir Jayanti (Jainism).""",
    
    "indian languages": """India has 22 officially recognized languages mentioned in the Eighth Schedule of the Constitution. Hindi is the most widely spoken language and, along with English, is used for official purposes by the central government. Other major languages include Bengali, Telugu, Marathi, Tamil, Urdu, Gujarati, Kannada, Odia, and Malayalam. The country is home to hundreds of dialects as well.""",
    
    "taj mahal": """The Taj Mahal is an ivory-white marble mausoleum located in Agra, Uttar Pradesh, India. It was commissioned in 1632 by the Mughal emperor Shah Jahan to house the tomb of his favorite wife, Mumtaz Mahal. The Taj Mahal is considered the finest example of Mughal architecture and was designated as a UNESCO World Heritage Site in 1983. It is one of the New Seven Wonders of the World.""",
    
    "indian independence": """India gained independence from British rule on August 15, 1947, after a long struggle for freedom. Key figures in India's independence movement included Mahatma Gandhi, Jawaharlal Nehru, Sardar Vallabhbhai Patel, Subhas Chandra Bose, and many others. The independence also led to the partition of British India into two separate nations: India and Pakistan, resulting in large-scale migration and communal violence.""",
    
    "bollywood": """Bollywood is the informal term used for the Hindi-language film industry based in Mumbai (formerly known as Bombay), India. It is the largest film producer in India and one of the largest centers of film production in the world. Bollywood films are known for their colorful songs and dances, melodramatic plots, and high emotional content. The industry produces over 1000 films annually and has a global audience.""",
    
    "indian sports": """Cricket is the most popular sport in India, with the Indian Premier League (IPL) being one of the largest sports leagues globally. Other popular sports include field hockey (India's national sport), football (soccer), badminton, tennis, and kabaddi. India has produced world champions in sports like chess (Viswanathan Anand), badminton (P.V. Sindhu, Saina Nehwal), and shooting (Abhinav Bindra).""",
    
    "indian education": """India has one of the largest education systems in the world. The country has made significant progress in improving access to education, with a literacy rate of around 74% according to recent data. Higher education institutions include prestigious Indian Institutes of Technology (IITs), Indian Institutes of Management (IIMs), All India Institute of Medical Sciences (AIIMS), and various central and state universities."""
}

def get_response(query):
    """
    Check if the query matches any India knowledge entry
    Returns the corresponding answer or None if no match
    """
    # Convert query to lowercase for case-insensitive matching
    query_lower = query.lower()
    
    # Check for general India queries
    if 'india' in query_lower and not any(key in query_lower for key in india_knowledge if key != "india general"):
        return india_knowledge.get("india general")
    
    # Check for specific India information
    if 'geography' in query_lower and 'india' in query_lower:
        return india_knowledge.get("india geography")
    
    if any(term in query_lower for term in ['culture', 'tradition']) and 'india' in query_lower:
        return india_knowledge.get("indian culture")
    
    if 'history' in query_lower and 'india' in query_lower:
        return india_knowledge.get("indian history")
    
    if any(term in query_lower for term in ['food', 'cuisine', 'dish']) and 'india' in query_lower:
        return india_knowledge.get("indian cuisine")
    
    if any(term in query_lower for term in ['government', 'politics', 'political']) and 'india' in query_lower:
        return india_knowledge.get("indian government")
    
    if any(term in query_lower for term in ['economy', 'economic', 'gdp', 'business']) and 'india' in query_lower:
        return india_knowledge.get("indian economy")
    
    if any(term in query_lower for term in ['festival', 'celebration', 'diwali', 'holi']) and 'india' in query_lower:
        return india_knowledge.get("indian festivals")
    
    if any(term in query_lower for term in ['language', 'speak', 'hindi', 'bengali']) and 'india' in query_lower:
        return india_knowledge.get("indian languages")
    
    # Check for specific landmarks or topics
    if 'taj mahal' in query_lower:
        return india_knowledge.get("taj mahal")
    
    if any(term in query_lower for term in ['independence', 'freedom', 'gandhi']) and 'india' in query_lower:
        return india_knowledge.get("indian independence")
    
    if any(term in query_lower for term in ['bollywood', 'movie', 'film', 'cinema']) and 'india' in query_lower:
        return india_knowledge.get("bollywood")
    
    if any(term in query_lower for term in ['sport', 'cricket', 'hockey']) and 'india' in query_lower:
        return india_knowledge.get("indian sports")
    
    if any(term in query_lower for term in ['education', 'school', 'university', 'college']) and 'india' in query_lower:
        return india_knowledge.get("indian education")
    
    # Check for other keywords in the knowledge base
    for key, value in india_knowledge.items():
        if key in query_lower:
            return value
    
    # No match found
    return None
