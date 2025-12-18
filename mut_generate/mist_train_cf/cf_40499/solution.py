"""
QUESTION:
Implement the function `process_csv(headers, data)` that takes a list of headers and a list of data as input where the data is a list of lists, each containing a music style and its associated country. The function should return a dictionary containing three results: 
1. A dictionary where keys are music styles and values are their occurrences.
2. The country with the highest number of music styles associated with it.
3. A dictionary where keys are countries and values are lists of music styles associated with each country.

Assume that the input data is well-formed and does not contain any errors. The input headers list will always contain two strings 'style' and 'country', and the data list will always contain lists of two strings each.
"""

def process_csv(headers, data):
    music_styles_count = {}
    country_music_styles = {}
    
    for style, country in data:
        # Count occurrences of each music style
        music_styles_count[style] = music_styles_count.get(style, 0) + 1
        
        # Create dictionary of countries and associated music styles
        country_music_styles.setdefault(country, []).append(style)
    
    # Identify the country with the highest number of music styles
    max_country = max(country_music_styles, key=lambda k: len(country_music_styles[k]))
    
    return {
        'music_styles_count': music_styles_count,
        'max_country': max_country,
        'country_music_styles': country_music_styles
    }