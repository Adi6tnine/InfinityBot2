"""
Science knowledge module for InfinityBot
Contains information about various scientific topics
"""

import re

# Science knowledge dictionary
science_knowledge = {
    "solar system": """Our solar system consists of the Sun, eight planets (Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune), dwarf planets (including Pluto), moons, asteroids, comets, and other celestial objects. The planets orbit around the Sun, which is a medium-sized star at the center of our solar system.""",
    
    "planet": """There are eight recognized planets in our solar system: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune. The first four are terrestrial (rocky) planets, while the latter four are gas giants. Pluto was reclassified as a dwarf planet in 2006.""",
    
    "gravity": """Gravity is a fundamental force of nature that attracts objects with mass toward each other. On Earth, gravity gives weight to objects and causes objects to fall toward the ground when dropped. Sir Isaac Newton's law of universal gravitation and Einstein's theory of general relativity are the primary theories explaining gravity.""",
    
    "atom": """An atom is the basic unit of matter, consisting of a nucleus (made of protons and neutrons) surrounded by electrons. Atoms are the building blocks of all matter and are incredibly small - a typical atom is about 0.1-0.5 nanometers in diameter.""",
    
    "element": """An element is a substance made up of atoms with the same number of protons. There are 118 known elements, 94 of which occur naturally on Earth. Examples include hydrogen, oxygen, carbon, gold, and uranium. The periodic table organizes all known elements by their atomic number.""",
    
    "dna": """DNA (Deoxyribonucleic Acid) is a molecule that carries the genetic instructions for the development, functioning, growth, and reproduction of all known organisms. DNA consists of two strands coiled around each other in a double helix structure, made up of nucleotides containing the bases adenine (A), thymine (T), guanine (G), and cytosine (C).""",
    
    "evolution": """Evolution is the process by which different kinds of living organisms have developed from earlier forms during the history of the Earth. The theory of evolution by natural selection was first formulated by Charles Darwin in his book 'On the Origin of Species' (1859), explaining how species adapt to their environments over generations.""",
    
    "climate change": """Climate change refers to long-term shifts in temperatures and weather patterns, primarily caused by human activities like burning fossil fuels, which increase levels of greenhouse gases in Earth's atmosphere. Effects include rising temperatures, more frequent extreme weather events, rising sea levels, and ecosystem disruptions.""",
    
    "quantum": """Quantum mechanics is a fundamental theory in physics that describes nature at the smallest scales of energy levels of atoms and subatomic particles. It departs from classical physics in that energy, momentum, and other quantities are often restricted to discrete values (quantization), objects have wave-like properties, and there are limits to the precision with which quantities can be measured (Heisenberg's uncertainty principle).""",
    
    "relativity": """Einstein's theory of relativity consists of two theories: special relativity (1905) and general relativity (1915). Special relativity states that the laws of physics are the same for all non-accelerating observers and that the speed of light is constant regardless of the observer's motion. General relativity describes gravity as a geometric property of space and time (spacetime), explaining how massive objects distort the fabric of spacetime, causing what we perceive as gravity.""",
    
    "big bang": """The Big Bang theory is the prevailing cosmological model explaining the existence of the observable universe. According to this theory, the universe began as a singularity around 13.8 billion years ago, then expanded extremely rapidly, and has continued to expand to this day. The theory is supported by observations of cosmic microwave background radiation and the cosmic expansion.""",
    
    "cell": """The cell is the basic structural, functional, and biological unit of all known living organisms. Cells are the smallest units of life, often called the 'building blocks of life.' There are two main types of cells: prokaryotic (simple, no nucleus) and eukaryotic (complex, with nucleus). Human bodies contain trillions of cells of various types, each specialized for different functions.""",
    
    "photosynthesis": """Photosynthesis is the process by which green plants, algae, and some bacteria convert light energy, usually from the sun, into chemical energy in the form of glucose or other sugars. The process uses carbon dioxide and water, releasing oxygen as a byproduct. This process is fundamental for maintaining Earth's atmosphere and providing energy for nearly all ecosystems.""",
    
    "periodic table": """The periodic table is a tabular arrangement of chemical elements, organized by their atomic number, electron configuration, and recurring chemical properties. Elements are arranged in rows (periods) and columns (groups). The table was first created by Dmitri Mendeleev in 1869 and has been refined over time, now containing 118 confirmed elements."""
}

def get_response(query):
    """
    Check if the query matches any science knowledge entry
    Returns the corresponding answer or None if no match
    """
    # Convert query to lowercase for case-insensitive matching
    query_lower = query.lower()
    
    # Check for exact matches or keywords
    for key, value in science_knowledge.items():
        if key in query_lower:
            return value
    
    # Check for specific science questions
    if re.search(r'what is an? (atom|element|dna|cell)', query_lower):
        match = re.search(r'what is an? (atom|element|dna|cell)', query_lower)
        topic = match.group(1)
        return science_knowledge.get(topic)
    
    if re.search(r'how (does|do) (gravity|photosynthesis) work', query_lower):
        match = re.search(r'how (does|do) (gravity|photosynthesis) work', query_lower)
        topic = match.group(2)
        return science_knowledge.get(topic)
    
    if re.search(r'(what|tell me about) (is|the) (solar system|periodic table|big bang)', query_lower):
        for term in ['solar system', 'periodic table', 'big bang']:
            if term in query_lower:
                return science_knowledge.get(term)
    
    # No match found
    return None
