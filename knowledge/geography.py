"""
Geography knowledge module for InfinityBot
Contains information about countries, continents, oceans, etc.
"""

import re

# Geography knowledge dictionary
geography_knowledge = {
    "continents": """There are seven continents on Earth: Africa, Antarctica, Asia, Europe, North America, Australia (Oceania), and South America. Asia is the largest continent by both land area and population, while Antarctica is the least populated.""",
    
    "oceans": """The five named oceans of the world are the Pacific Ocean (the largest), Atlantic Ocean, Indian Ocean, Southern Ocean, and Arctic Ocean (the smallest). Together they cover approximately 71% of Earth's surface.""",
    
    "countries": """There are 195 recognized sovereign states in the world, of which 193 are member states of the United Nations. The largest country by land area is Russia, while the most populous country is China. Vatican City is the smallest country both by area and population.""",
    
    "mountains": """Mountains are elevated portions of the Earth's crust. The world's highest mountain is Mount Everest in the Himalayas, standing at 8,848.86 meters (29,031.7 feet) above sea level. Other notable mountain ranges include the Andes in South America, the Rockies in North America, and the Alps in Europe.""",
    
    "rivers": """Rivers are natural flowing watercourses that usually empty into a sea or ocean. The Amazon in South America is the world's largest river by volume, while the Nile in Africa is historically considered the longest, though some measurements suggest the Amazon may be slightly longer.""",
    
    "deserts": """Deserts are arid regions that receive very little precipitation. The largest hot desert is the Sahara in North Africa, covering about 9 million square kilometers. Antarctica is considered the world's largest cold desert.""",
    
    "climate zones": """Earth has several major climate zones: tropical (near the equator), temperate (middle latitudes), and polar (near the poles). These are further divided into specific climate types like tropical rainforest, desert, Mediterranean, continental, and tundra based on temperature and precipitation patterns.""",
    
    "usa": """The United States of America (USA) is a country comprising 50 states, a federal district (Washington D.C.), and various territories. It is the third-largest country by area and the third most populous. The USA has the world's largest economy by nominal GDP and is known for its cultural influence, technological innovation, and military strength.""",
    
    "uk": """The United Kingdom (UK), officially the United Kingdom of Great Britain and Northern Ireland, is a sovereign country in northwestern Europe. It consists of England, Scotland, Wales, and Northern Ireland. London is its capital and largest city. The UK has significant historical global influence and is a permanent member of the UN Security Council.""",
    
    "europe": """Europe is a continent located entirely in the Northern Hemisphere, comprising the westernmost peninsulas of Eurasia. It is bordered by the Arctic Ocean to the north, the Atlantic Ocean to the west, the Mediterranean Sea to the south, and Asia to the east. There are approximately 44-50 countries in Europe, depending on the definition used.""",
    
    "asia": """Asia is Earth's largest and most populous continent, located primarily in the Eastern and Northern Hemispheres. It covers about 30% of Earth's total land area and is home to roughly 60% of the world's population. Asia is known for its diverse cultures, economies, historical civilizations, and geographic features.""",
    
    "africa": """Africa is the world's second-largest and second-most populous continent, after Asia. It covers about 20% of Earth's land area and is home to 1.4 billion people. The continent is known for its rich biodiversity, diverse cultures and ethnicities, and important natural resources. The Nile River, the world's longest river, and the Sahara, the world's largest hot desert, are both in Africa.""",
    
    "south america": """South America is a continent situated in the Western Hemisphere, mostly in the Southern Hemisphere. It is bordered by the Atlantic Ocean to the east and the Pacific Ocean to the west. Major countries include Brazil (the largest by both area and population), Argentina, Colombia, and Peru. The continent is known for the Amazon Rainforest, the Andes mountain range, and diverse ecosystems.""",
    
    "north america": """North America is a continent in the Northern Hemisphere, bordered by the Arctic Ocean to the north, the Atlantic Ocean to the east, the Pacific Ocean to the west, and South America to the southeast. Major countries include the United States, Canada, and Mexico. It features diverse geography including the Rocky Mountains, Great Plains, and Great Lakes.""",
    
    "australia": """Australia is both a continent and a country, surrounded by the Indian and Pacific Oceans. It is the smallest continent by land area but the sixth-largest country in the world. Australia is known for its unique wildlife (like kangaroos and koalas), the Great Barrier Reef, and vast desert regions known as the Outback.""",
    
    "antarctica": """Antarctica is Earth's southernmost continent, containing the geographic South Pole. It is situated in the Antarctic region of the Southern Hemisphere and is surrounded by the Southern Ocean. Nearly 98% of Antarctica is covered by ice, making it the coldest, driest, and windiest continent with the highest average elevation. It has no permanent human population but hosts scientific research stations operated by various countries."""
}

def get_response(query):
    """
    Check if the query matches any geography knowledge entry
    Returns the corresponding answer or None if no match
    """
    # Convert query to lowercase for case-insensitive matching
    query_lower = query.lower()
    
    # Check for exact matches or keywords
    for key, value in geography_knowledge.items():
        if key in query_lower:
            return value
    
    # Check for specific geography questions
    if re.search(r'how many continents', query_lower):
        return geography_knowledge.get("continents")
    
    if re.search(r'how many oceans', query_lower):
        return geography_knowledge.get("oceans")
    
    if re.search(r'how many countries', query_lower):
        return geography_knowledge.get("countries")
    
    if re.search(r'what is the (highest|tallest) mountain', query_lower):
        return geography_knowledge.get("mountains")
    
    if re.search(r'what is the (longest|largest) river', query_lower):
        return geography_knowledge.get("rivers")
    
    if re.search(r'what is the (largest|biggest) desert', query_lower):
        return geography_knowledge.get("deserts")
    
    if re.search(r'tell me about (europe|asia|africa|north america|south america|australia|antarctica)', query_lower):
        for continent in ["europe", "asia", "africa", "north america", "south america", "australia", "antarctica"]:
            if continent in query_lower:
                return geography_knowledge.get(continent)
    
    # No match found
    return None
