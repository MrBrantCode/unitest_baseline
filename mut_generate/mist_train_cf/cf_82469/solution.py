"""
QUESTION:
Create a function `get_data` that accepts a JSON payload with a 'keyword' field and returns the corresponding data from a predefined database in JSON format. The database contains keyword-value pairs where the value is another JSON object. If the 'keyword' field is missing from the payload or the keyword is not found in the database, return a JSON error message with a 400 status code.
"""

def get_data(payload):
    """
    Returns the corresponding data from a predefined database in JSON format.

    Args:
        payload (dict): A JSON payload with a 'keyword' field.

    Returns:
        dict: A JSON object containing the corresponding data if found, otherwise a JSON error message.
    """

    database = {
        'car': {'brand': 'Tesla', 'model': 'Model Y', 'year': 2018},
        'book': {'title': 'Invisible Man', 'author': 'Ralph Ellison', 'year': 1952},
        'apple': {'type': 'fruit', 'color': 'red'}
    }

    if 'keyword' not in payload:
        return {'message': 'No keyword field'}, 400

    keyword = payload['keyword']

    if keyword not in database:
        return {'message': 'Keyword not in database'}, 400

    return {keyword: database[keyword]}, 200