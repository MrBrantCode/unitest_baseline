"""
QUESTION:
Create a function called `generate_google_search_url` that takes two parameters, `search_term` and `num_results`, and returns a custom Google search URL. The function should replace spaces in the search term with the "+" symbol, convert the search term to lowercase, and ensure it contains no special characters. The function should also ensure that the `num_results` parameter is between 1 and 100. The custom URL should be in the format `https://www.google.com/search?q=[search_term]&num=[num_results]`.
"""

import urllib.parse

def generate_google_search_url(search_term, num_results):
    # Check for special or invalid characters in the search term
    if any(char in search_term for char in '!"#$%&\'()*+,-./:;<=>?@[\\]^`{|}~'):
        return "Error: Invalid search term. Special characters are not allowed."
    
    # Convert the search term to lowercase
    search_term = search_term.lower()
    
    # Replace spaces with the "+" symbol
    search_term = search_term.replace(" ", "+")
    
    # Check if the number of search results is within the specified range
    if not (1 <= num_results <= 100):
        return "Error: Invalid number of search results. Please enter a number between 1 and 100."
    
    # Generate the Google search URL
    base_url = "https://www.google.com/search?q="
    num_results_param = "&num=" + str(num_results)
    encoded_search_term = urllib.parse.quote(search_term)
    final_url = base_url + encoded_search_term + num_results_param
    
    return final_url