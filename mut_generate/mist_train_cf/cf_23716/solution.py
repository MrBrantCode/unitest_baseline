"""
QUESTION:
Write a function `limit_documents` that takes in a list of documents and returns a subset of those documents where the topics include current events in the world.
"""

def limit_documents(documents):
    current_events = ["politics", "sports", "news"]
    return [document for document in documents if any(topic in current_events for topic in document["topics"])]