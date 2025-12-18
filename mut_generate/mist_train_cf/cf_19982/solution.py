"""
QUESTION:
Create a function named `create_alert_html` that takes a string `message` as input and returns the HTML code to display an alert message with the input string as the text, properly escaping any special characters. The function should have a time complexity of O(n) and a space complexity of O(n).
"""

def create_alert_html(message):
    escaped_message = message.replace("'", "\\'")
    return "<script>alert('{}');</script>".format(escaped_message)