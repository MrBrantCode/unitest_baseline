"""
QUESTION:
Construct a function `construct_google_search_url` that takes four parameters: `query`, `date`, `location`, and `language`. The function should return a URL string to search for `query` on Google with filtering options for `date`, `location`, and `language`. 

The `date` parameter should support 'YYYY-MM-DD' format or 'past_week', 'past_month', 'past_year'. The `location` parameter should support 'country:xx', 'city:xx', or 'latlng:xx,yy'. The `language` parameter should support 'lang:xx'.
"""

def construct_google_search_url(query, date, location, language):
    url = 'https://www.google.com/search?q=' + query.replace(' ', '+') + '&tbs='
    
    if date == 'past_week':
        url += 'qdr:w'
    elif date == 'past_month':
        url += 'qdr:m'
    elif date == 'past_year':
        url += 'qdr:y'
    else:
        url += 'cdr:1,cd_min:' + date + ',cd_max:' + date
    
    url += ',' + location.replace(':', ',') + ',lr:' + language.replace(':', '_')
    
    return url