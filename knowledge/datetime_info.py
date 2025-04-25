"""
Date and time information module for InfinityBot
Provides current date, time, and related information
"""

import datetime
import re

def get_current_datetime_info(query):
    """
    Get information about current date and time based on the query
    Returns formatted response or None if not a date/time query
    """
    query_lower = query.lower()
    now = datetime.datetime.now()
    
    # Check for time queries
    if re.search(r'what( is|\'s) (the )?time', query_lower):
        return f"The current time is {now.strftime('%I:%M %p')}."
    
    # Check for date queries
    if re.search(r'what( is|\'s) (the )?date', query_lower) or 'today\'s date' in query_lower:
        return f"Today's date is {now.strftime('%A, %B %d, %Y')}."
    
    # Check for day of week queries
    if re.search(r'what( is|\'s) (the )?day', query_lower) or 'what day is it' in query_lower:
        return f"Today is {now.strftime('%A')}."
    
    # Check for month queries
    if re.search(r'what( is|\'s) (the )?month', query_lower):
        return f"The current month is {now.strftime('%B')}."
    
    # Check for year queries
    if re.search(r'what( is|\'s) (the )?year', query_lower):
        return f"The current year is {now.strftime('%Y')}."
    
    # Check for full date and time queries
    if 'date and time' in query_lower or 'time and date' in query_lower:
        return f"It is currently {now.strftime('%I:%M %p')} on {now.strftime('%A, %B %d, %Y')}."
    
    # Check for season
    if 'what season' in query_lower:
        month = now.month
        day = now.day
        
        # Northern hemisphere seasons (approximate)
        if (month == 3 and day >= 20) or (month > 3 and month < 6) or (month == 6 and day < 21):
            return "It's currently spring in the Northern Hemisphere and autumn/fall in the Southern Hemisphere."
        elif (month == 6 and day >= 21) or (month > 6 and month < 9) or (month == 9 and day < 22):
            return "It's currently summer in the Northern Hemisphere and winter in the Southern Hemisphere."
        elif (month == 9 and day >= 22) or (month > 9 and month < 12) or (month == 12 and day < 21):
            return "It's currently autumn/fall in the Northern Hemisphere and spring in the Southern Hemisphere."
        else:
            return "It's currently winter in the Northern Hemisphere and summer in the Southern Hemisphere."
    
    # Return None if not a date/time query
    return None

def get_response(query):
    """
    Process date/time related queries
    Returns response or None if not a date/time query
    """
    return get_current_datetime_info(query)
