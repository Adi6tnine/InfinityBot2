import logging
import requests
import urllib.parse
from bs4 import BeautifulSoup
import wikipedia
from urllib.parse import quote

# Configure logging
logger = logging.getLogger(__name__)

# Initialize an HTTP session with headers to mimic a browser
session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
})

def clean_text(text):
    """Clean and format text for better readability"""
    import re
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    # Remove references like [1], [2], etc.
    text = re.sub(r'\[\d+\]', '', text)
    return text.strip()

def extract_text_from_html(html_content):
    """Extract meaningful text from HTML content"""
    try:
        # Try to use trafilatura if available (cleaner extraction)
        try:
            import trafilatura
            extracted_text = trafilatura.extract(html_content)
            if extracted_text:
                return clean_text(extracted_text)
        except ImportError:
            logger.debug("Trafilatura not available, falling back to BeautifulSoup")
        
        # Fallback to BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Remove unwanted elements
        for element in soup(['script', 'style', 'header', 'footer', 'nav']):
            element.decompose()
        
        # Get text and clean it
        text = soup.get_text()
        return clean_text(text)
    except Exception as e:
        logger.error(f"Error extracting text from HTML: {str(e)}")
        return ""

def search_wikipedia(query, sentences=3):
    """Search Wikipedia for information"""
    try:
        # Set Wikipedia to use English
        wikipedia.set_lang("en")
        
        # Search for pages
        search_results = wikipedia.search(query, results=3)
        
        if not search_results:
            return None
        
        try:
            # Get the page for the top result
            page = wikipedia.page(search_results[0], auto_suggest=False)
            
            # Get a summary
            summary = wikipedia.summary(search_results[0], sentences=sentences, auto_suggest=False)
            
            # Clean and return the summary
            return clean_text(summary) + f" (Source: Wikipedia - {page.title})"
        
        except wikipedia.DisambiguationError as e:
            # If disambiguation page, use the first option
            try:
                page_title = e.options[0]
                summary = wikipedia.summary(page_title, sentences=sentences, auto_suggest=False)
                return clean_text(summary) + f" (Source: Wikipedia - {page_title})"
            except:
                return None
        
        except Exception as e:
            logger.error(f"Wikipedia search error: {str(e)}")
            return None
    
    except Exception as e:
        logger.error(f"Wikipedia search error: {str(e)}")
        return None

def search_duckduckgo(query):
    """Search DuckDuckGo and extract information"""
    try:
        # Try to use duckduckgo_search if available
        try:
            from duckduckgo_search import DDGS
            ddgs = DDGS()
            results = list(ddgs.text(query, max_results=3))
            
            if results:
                # Return the first result
                top_result = results[0]
                return f"{clean_text(top_result['body'])} (Source: {top_result['href']})"
        except ImportError:
            logger.debug("duckduckgo_search not available, using manual scraping")
        
        # Manual scraping fallback
        encoded_query = quote(query)
        url = f"https://html.duckduckgo.com/html/?q={encoded_query}"
        
        response = session.get(url, timeout=10)
        if response.status_code != 200:
            return None
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract search results
        results = []
        for result in soup.select('.result'):
            title_elem = result.select_one('.result__title')
            snippet_elem = result.select_one('.result__snippet')
            
            if title_elem and snippet_elem:
                title = title_elem.get_text().strip()
                snippet = snippet_elem.get_text().strip()
                
                if title and snippet:
                    results.append({
                        'title': title,
                        'snippet': snippet
                    })
        
        if results:
            return f"{results[0]['snippet']} (Source: DuckDuckGo search result)"
        
        return None
    
    except Exception as e:
        logger.error(f"DuckDuckGo search error: {str(e)}")
        return None

def search_web(query):
    """
    Search the web for information using multiple methods
    Returns the first successful result
    """
    # First try Wikipedia
    wiki_result = search_wikipedia(query)
    if wiki_result:
        return wiki_result
    
    # Then try DuckDuckGo
    ddg_result = search_duckduckgo(query)
    if ddg_result:
        return ddg_result
    
    # Return None if no results found
    return None
