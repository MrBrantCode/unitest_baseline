"""
QUESTION:
Write a function named 'search_results' that accepts a text query and returns the relevant results in an organized format such as a table or a list, assuming the search engine is already implemented and the results are available.
"""

def search_results(query, search_engine_results):
    """
    This function takes a text query and a list of search engine results, 
    then organizes and returns the results in a structured format.

    Args:
        query (str): The text query to be searched.
        search_engine_results (list): A list of search engine results.

    Returns:
        list: A list of dictionaries containing the search results.
    """

    # Initialize an empty list to store the search results
    results = []

    # Iterate over each result in the search engine results
    for result in search_engine_results:
        # Extract the title, link, and description from the result
        title = result.get('title', '')
        link = result.get('link', '')
        description = result.get('description', '')

        # Create a dictionary to store the result
        result_dict = {
            'query': query,
            'title': title,
            'link': link,
            'description': description
        }

        # Append the result dictionary to the results list
        results.append(result_dict)

    # Return the list of search results
    return results