"""
QUESTION:
Implement the function `extract_facebook_post_details(api_response)` that takes a JSON API response as input, extracts the post message and ID, truncates the post message to 4 words if necessary, and splits the post ID into two parts. The function should return a dictionary with the keys "post_message" and "post_id_parts". The input API response is a JSON string, and the post message and ID are nested under the 'data' key, with the message under the 'message' key and the ID under the 'id' key.
"""

def extract_facebook_post_details(api_response):
    parsed_data = json.loads(api_response)
    
    post_message = parsed_data['data'][0]['message'] if 'message' in parsed_data['data'][0] else ''
    
    # Truncate post message if it contains more than 4 words
    post_words = post_message.split()
    if len(post_words) > 4:
        post_message = ' '.join(post_words[:4])
    
    post_id = parsed_data['data'][0]['id'].split('_')
    
    return {
        "post_message": post_message,
        "post_id_parts": post_id
    }