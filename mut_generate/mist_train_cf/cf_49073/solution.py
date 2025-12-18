"""
QUESTION:
Design a function `ai_chatbot_response` that takes a user query as input and returns a response based on the query. The function should be able to handle at least five predefined queries: "What are your business hours?", "Where can I access my account?", "I need to talk to a customer service representative.", "What's your return policy?", and "How to track my order?". If the query is not recognized, the function should return a message indicating that the query is beyond its capabilities and offer to transfer the user to a live customer representative. Assume that the business hours, website link, return policy link, and other relevant information are predefined.
"""

def ai_chatbot_response(query):
    """
    This function takes a user query as input and returns a response based on the query.
    
    Parameters:
    query (str): The user's query.
    
    Returns:
    str: The chatbot's response to the query.
    """
    
    # Predefined queries and responses
    queries_responses = {
        "What are your business hours?": "Our business hours are from 9 AM to 5 PM, Monday to Friday. Please feel free to contact us during these hours.",
        "Where can I access my account?": "You can access your account by visiting our website and clicking on the 'Sign In' button at the top right corner. Here is the link to our website: [website_link]",
        "I need to talk to a customer service representative.": "Sure, I can help you with that. Please hold on while I connect you to a customer service representative.",
        "What's your return policy?": "You can return any item bought from us within 30 days of purchase, provided it is in its original condition and packaging. Here is the full details of our return policy: [return_policy_link].",
        "How to track my order?": "You can track the status of your orders by signing in to your account on our website and clicking on the 'Order History' tab. If you're having trouble finding this information, you can also call our customer service line for support."
    }
    
    # Check if the query is recognized
    if query in queries_responses:
        # Return the response for the query
        return queries_responses[query]
    else:
        # Return a message indicating that the query is beyond the chatbot's capabilities
        return "I'm not sure I understand your question. I can offer to transfer you to a live customer representative if you'd like."