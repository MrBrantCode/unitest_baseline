"""
QUESTION:
Construct a function named `construct_google_search_url` that takes three parameters: `query`, `date`, and `location`. The function should return a URL string to search for the given `query` on Google with optional filters for `date` and `location`. 

The `date` parameter can be either a string representing the desired date range in 'YYYY-MM-DD' format or one of 'past_week', 'past_month', 'past_year'. 

The `location` parameter can be a string in one of the following formats: 'country:xx' for a specific country, 'city:xx' for a specific city, or 'latlng:xx,yy' for latitude and longitude. 

The function should return a constructed URL as a string, where the `query` is URL-encoded and the `date` and `location` filters are appended accordingly.
"""

def construct_google_search_url(query, date=None, location=None):
    base_url = 'https://www.google.com/search?q='
    query = query.replace(' ', '+')
    url = base_url + query
    if date:
        if date == 'past_week':
            url += '&tbs=qdr:w'
        elif date == 'past_month':
            url += '&tbs=qdr:m'
        elif date == 'past_year':
            url += '&tbs=qdr:y'
        else:
            url += f'&tbs=qdr:{date}'
    if location:
        url += f'&near={location}'
    return url