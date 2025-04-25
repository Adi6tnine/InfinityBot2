"""
Jokes module for InfinityBot
Contains a collection of jokes and functions to retrieve them
"""

import random

# Collection of jokes
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "I told my wife she was drawing her eyebrows too high. She looked surprised.",
    "What's the best thing about Switzerland? I don't know, but the flag is a big plus.",
    "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them.",
    "Why do we tell actors to 'break a leg?' Because every play has a cast.",
    "Parallel lines have so much in common. It's a shame they'll never meet.",
    "I'm reading a book about anti-gravity. It's impossible to put down!",
    "What do you call a parade of rabbits hopping backwards? A receding hare-line.",
    "Why don't some couples go to the gym? Because some relationships don't work out.",
    "What do you call a fake noodle? An impasta!",
    "Why couldn't the bicycle stand up by itself? It was two tired.",
    "How do you organize a space party? You planet.",
    "What's orange and sounds like a parrot? A carrot.",
    "Why did the coffee file a police report? It got mugged.",
    "How does a penguin build its house? Igloos it together.",
    "Why don't eggs tell jokes? They'd crack each other up.",
    "What do you call a bear with no teeth? A gummy bear.",
    "Why did the invisible man turn down the job offer? He couldn't see himself doing it.",
    "What do you call a fish wearing a crown? King of the sea!",
    "What do you get when you cross a snowman and a vampire? Frostbite.",
    "Why was the math book sad? It had too many problems.",
    "What did one wall say to the other wall? I'll meet you at the corner!",
    "Why don't scientists trust atoms? Because they make up everything!",
    "What's a computer's favorite snack? Microchips!",
    "Why did the student eat his homework? Because the teacher said it was a piece of cake!",
    "What do you call a dinosaur with an extensive vocabulary? A thesaurus.",
    "Why did the golfer bring two pairs of pants? In case he got a hole in one.",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "What do you call cheese that isn't yours? Nacho cheese!"
]

# Technology jokes
tech_jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why was the JavaScript developer sad? Because he didn't Node how to Express himself.",
    "Why did the programmer quit his job? Because he didn't get arrays (a raise)!",
    "What do you call a computer floating in the ocean? A Dell rolling in the deep.",
    "Why did the developer go broke? Because he used up all his cache.",
    "What did the Java code say to the C code? You've got no class.",
    "Why don't programmers like nature? It has too many bugs and no debugging tool.",
    "What's a programmer's favorite place to hang out? Foo Bar.",
    "Why was the SQL query sad? It had too many JOINs but nobody to SELECT from.",
    "Two bytes meet. The first byte asks, 'Are you ill?' The second byte replies, 'No, just feeling a bit off.'"
]

# Science jokes
science_jokes = [
    "A neutron walks into a bar and asks how much for a drink. The bartender replies, 'For you, no charge.'",
    "Why can't you trust an atom? Because they make up everything!",
    "I was reading a book on helium. I couldn't put it down!",
    "What did one ocean say to the other ocean? Nothing, they just waved.",
    "What do you do with a sick chemist? If you can't helium, and you can't curium, then you might as well barium.",
    "Why did the physicist break up with the biologist? There was no chemistry.",
    "A photon checks into a hotel. The bellhop asks, 'Any luggage?' The photon replies, 'No, I'm traveling light.'",
    "Did you hear oxygen and potassium went on a date? It went OK.",
    "Why do biologists look forward to casual Fridays? They're allowed to wear genes to work.",
    "The glass is neither half-full nor half-empty. The glass is twice as big as it needs to be."
]

def get_random_joke():
    """Return a random joke from the collection"""
    return random.choice(jokes)

def get_tech_joke():
    """Return a random technology joke"""
    return random.choice(tech_jokes)

def get_science_joke():
    """Return a random science joke"""
    return random.choice(science_jokes)

def get_response(query):
    """
    Check if the query is asking for a joke
    Returns a joke or None if the query isn't about jokes
    """
    query_lower = query.lower()
    
    # Check if asking for a joke
    if 'joke' in query_lower:
        # Check for specific types of jokes
        if 'tech' in query_lower or 'programming' in query_lower or 'computer' in query_lower:
            return get_tech_joke()
        elif 'science' in query_lower or 'physics' in query_lower or 'chemistry' in query_lower:
            return get_science_joke()
        else:
            return get_random_joke()
    
    # Check for other fun queries
    if 'make me laugh' in query_lower or 'tell me something funny' in query_lower:
        return get_random_joke()
    
    # No match found
    return None
