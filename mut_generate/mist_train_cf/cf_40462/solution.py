"""
QUESTION:
Write a function called `most_recent_author` that takes a list of dictionaries as input, where each dictionary contains the author's name and the modification date in the format "YYYY-MM-DD". Return the author who has made the most recent modification. If multiple authors have the same most recent modification date, return a list of those authors. The input list is not empty, and all dictionaries in the list contain 'author' and 'date' keys.
"""

from typing import List, Dict, Union

def most_recent_author(modifications: List[Dict[str, str]]) -> Union[str, List[str]]:
    author_dates = {}
    max_date = ''
    
    for modification in modifications:
        author = modification['author']
        date = modification['date']
        
        if date > max_date:
            max_date = date
            author_dates[max_date] = [author]
        elif date == max_date:
            author_dates[max_date].append(author)
    
    return author_dates[max_date] if len(author_dates[max_date]) > 1 else author_dates[max_date][0]