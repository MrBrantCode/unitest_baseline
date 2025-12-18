"""
QUESTION:
Design a function `generate_response(query)` that takes a query string as input and returns a response string. The function should be able to answer two types of questions about the Holocene epoch: "What is the current epoch in the geological time scale?" and "When did the Holocene epoch start?" (questions can be rephrased but must contain the keywords). If the query does not match any of the above questions, the function should return a default response "Sorry, I couldn't answer your question." The input query string is case-insensitive, and the output response string should be in sentence format.
"""

def generate_response(query):
    info = {
        "current epoch": "The current epoch in the geological time scale is Holocene.",
        "holocene start": "The Holocene started about 11,700 years ago."
    }

    low_query = query.lower()

    if "current epoch" in low_query:
        return info["current epoch"]
    elif "when" in low_query and "holocene" in low_query:
        return info["holocene start"]
    else:
        return "Sorry, I couldn't answer your question."