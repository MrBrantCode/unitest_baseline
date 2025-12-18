"""
QUESTION:
Create a function called `grandbot` that takes a user's question about the Grand Canyon as input and returns a response based on the question. The function should be able to answer the following questions:

- How long is the Grand Canyon?
- How deep is the Grand Canyon?
- What is the best time to visit the Grand Canyon?
- What activities can I do at the Grand Canyon?

The function should return a response with the corresponding information about the Grand Canyon for each question.
"""

def grandbot(question):
    """
    Returns a response based on the user's question about the Grand Canyon.

    Args:
        question (str): The user's question.

    Returns:
        str: A response with the corresponding information about the Grand Canyon.
    """

    # Create a dictionary to store the questions and their corresponding responses
    grand_canyon_info = {
        "how long is the grand canyon": "The Grand Canyon is approximately 277 miles (446 km) long.",
        "how deep is the grand canyon": "The Grand Canyon is about a mile deep, the average depth being about 1 mile or 1.6 kilometers.",
        "what is the best time to visit the grand canyon": "The best time to visit the Grand Canyon depends on what you want from your visit. The most popular times tend to be during the mild weather of spring (March to May) and fall (September to November). Summer is the peak tourist season but the temperatures can be very high. Winter has fewer visitors and offers a different, quiet but beautiful perspective, though some areas of the park may be closed due to snow.",
        "what activities can i do at the grand canyon": "You can do numerous activities at the Grand Canyon such as hiking, white water rafting in the Colorado River, helicopter tours, visiting viewpoints, camping, mule rides and more. Just remember to respect the rules within the national park to ensure its conservation for future generations!"
    }

    # Convert the user's question to lowercase to make the search case-insensitive
    question = question.lower()

    # Check if the user's question is in the dictionary
    if question in grand_canyon_info:
        # Return the corresponding response
        return grand_canyon_info[question]
    else:
        # Return a default response if the question is not found
        return "Sorry, I couldn't find any information about that. Please ask another question."