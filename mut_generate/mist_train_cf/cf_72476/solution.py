"""
QUESTION:
Implement a function named `ToPMine` to mine topics and phrases in large documents that contain many phrases. The function should be able to handle overlapping phrases and produce interpretable or accurate topic models for certain types of text data. Note that there is no pre-existing Python package for ToPMine, so the algorithm needs to be implemented from scratch.
"""

def ToPMine(documents):
    """
    Mine topics and phrases in large documents.

    Parameters:
    documents (list): A list of strings representing the documents to be mined.

    Returns:
    topics (list): A list of topics extracted from the documents.
    """
    # Tokenize the documents
    tokens = [document.split() for document in documents]

    # Remove stop words and punctuation
    stop_words = set(["is", "the", "and", "a", "an", "in", "on", "at", "by", "with"])
    filtered_tokens = [[word for word in token if word.lower() not in stop_words] for token in tokens]

    # Find phrases (sequences of words that appear together frequently)
    phrase_dict = {}
    for token in filtered_tokens:
        for i in range(len(token)):
            for j in range(i + 1, len(token) + 1):
                phrase = tuple(token[i:j])
                if phrase in phrase_dict:
                    phrase_dict[phrase] += 1
                else:
                    phrase_dict[phrase] = 1

    # Filter out phrases that appear less than a certain threshold
    threshold = 5
    filtered_phrases = {phrase: count for phrase, count in phrase_dict.items() if count >= threshold}

    # Create a graph where phrases are nodes and edges represent co-occurrence
    graph = {}
    for phrase in filtered_phrases:
        graph[phrase] = []
        for other_phrase in filtered_phrases:
            if phrase != other_phrase:
                if any(word in other_phrase for word in phrase):
                    graph[phrase].append(other_phrase)

    # Use graph clustering to identify topics
    topics = []
    visited = set()
    for phrase in graph:
        if phrase not in visited:
            cluster = [phrase]
            stack = [phrase]
            while stack:
                node = stack.pop()
                visited.add(node)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        cluster.append(neighbor)
                        stack.append(neighbor)
            topics.append(cluster)

    return topics