"""
QUESTION:
Implement a method called `process_text` in the `TextProcessor` class to process the text data obtained from the `get_text` method. The `process_text` method should convert all characters to lowercase, remove any leading or trailing whitespace, and replace all occurrences of the word "python" with "programming".
"""

def process_text(text):
    # Process the text data
    text = text.lower()  # Convert all characters to lowercase
    text = text.strip()  # Remove leading and trailing whitespace
    text = text.replace("python", "programming")  # Replace "python" with "programming"
    return text