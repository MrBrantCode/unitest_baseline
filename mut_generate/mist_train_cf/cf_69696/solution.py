"""
QUESTION:
Implement a function called `is_hate_speech` that takes a string input representing a social media post and returns a boolean indicating whether the post contains hate speech or cyberbullying. Assume the input string can contain any characters, including emojis, URLs, and special characters, and may be written in any language.
"""

def is_hate_speech(post):
    # Implementing a real-time hate speech and cyberbullying detection model requires a complex Machine Learning approach.
    # However, for the sake of simplicity, we can use a basic keyword-based approach.

    # Define a list of hate speech keywords (this is a very simplified example and actual implementation would require a more comprehensive list)
    hate_speech_keywords = ["hate", "kill", "injure", "abuse"]

    # Convert the post to lowercase to make the comparison case-insensitive
    post = post.lower()

    # Check if any hate speech keyword is present in the post
    for keyword in hate_speech_keywords:
        if keyword in post:
            return True

    # If no hate speech keyword is found, return False
    return False