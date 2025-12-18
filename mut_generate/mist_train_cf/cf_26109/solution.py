"""
QUESTION:
Create a function named 'categorize_text' that classifies a given text into its respective category based on its content. The function should take a string of text as input and return the category as a string.
"""

def categorize_text(text):
    # Implement the categorization logic here
    # For demonstration purposes, this example uses a simple if-else statement
    # In a real-world application, consider using machine learning models or NLP techniques

    if 'story' in text.lower() or 'plot' in text.lower():
        return 'Storytelling'
    elif 'news' in text.lower() or 'article' in text.lower():
        return 'News'
    elif 'poem' in text.lower() or 'verse' in text.lower():
        return 'Poetry'
    else:
        return 'Unknown'