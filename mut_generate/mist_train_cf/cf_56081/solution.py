"""
QUESTION:
Define a function `chatbot_response` that takes a query string as input and returns a relevant response. The function should have the capability to answer frequently asked questions and provide product suggestions. Implement the function in such a way that it can be easily integrated into a website and can be trained with data for more specific responses.
"""

def chatbot_response(query):
    # Define a dictionary to store frequently asked questions and their answers
    faqs = {
        "What is your name?": "I'm an AI chatbot.",
        "How can you help me?": "I can answer your questions and provide product suggestions.",
        # Add more FAQs here...
    }

    # Define a dictionary to store product suggestions
    products = {
        "laptop": ["Dell Inspiron", "HP Envy", "Apple MacBook"],
        "smartphone": ["Apple iPhone", "Samsung Galaxy", "Google Pixel"],
        # Add more products here...
    }

    # Check if the query is a frequently asked question
    if query in faqs:
        return faqs[query]

    # Check if the query is a product suggestion
    for product, suggestions in products.items():
        if product in query:
            return "We recommend the following " + product + "s: " + ", ".join(suggestions)

    # If the query is not a FAQ or product suggestion, return a default response
    return "Sorry, I didn't understand your query. Please try again."