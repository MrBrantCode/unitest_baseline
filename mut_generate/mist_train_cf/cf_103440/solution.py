"""
QUESTION:
Create a function called `display_alert_message` that takes a string as input and returns the HTML code to display an alert message with the input string as the text. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input string. The returned HTML code should be in the format "<script>alert('input string');</script>".
"""

def display_alert_message(text):
    return "<script>alert('{}');</script>".format(text)