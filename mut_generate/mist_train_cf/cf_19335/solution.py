"""
QUESTION:
Write a function called `generate_summary` that takes in a text document as input and returns a concise summary of the main ideas and key points within the text. The function should prioritize sentences based on their relevance and significance, and include a threshold value to guarantee the inclusion of important sentences. The summary should be a shorter version of the original document, capturing the most important information, and should not exceed a maximum length or word limit.
"""

def generate_summary(text_document, max_length=500, word_limit=100, threshold=0.8):
    """
    Generate a concise summary of the main ideas and key points within a text document.
    
    Args:
    text_document (str): The input text document.
    max_length (int): The maximum length of the summary in characters. Default is 500.
    word_limit (int): The maximum number of words in the summary. Default is 100.
    threshold (float): The minimum importance score for a sentence to be guaranteed inclusion in the summary. Default is 0.8.
    
    Returns:
    str: A concise summary of the main ideas and key points within the text document.
    """

    # Preprocess the text document by tokenizing it into sentences
    sentences = text_document.split('.')

    # Calculate the importance score for each sentence
    importance_scores = []
    for i, sentence in enumerate(sentences):
        # Relevance can be determined by the presence of important keywords
        relevance = sum(1 for word in sentence.split() if word.lower() in ['important', 'key', 'main'])
        # Significance can be based on sentence position
        significance = 1 / (i + 1)
        importance_score = relevance * significance
        importance_scores.append(importance_score)

    # Sort the sentences in descending order of their importance scores
    sorted_sentences = [sentence for _, sentence in sorted(zip(importance_scores, sentences), reverse=True)]

    # Initialize the summary and the current length
    summary = ''
    current_length = 0

    # Iterate through the sorted list of sentences and add them to the summary
    for sentence in sorted_sentences:
        # Check if adding the sentence would exceed the maximum length or word limit
        if current_length + len(sentence) > max_length or len(summary.split()) + len(sentence.split()) > word_limit:
            break
        # Check if the sentence has an importance score higher than the threshold
        if importance_scores[sorted_sentences.index(sentence)] > threshold:
            summary += sentence + '. '
            current_length += len(sentence)

    # If the summary is still shorter than desired, add a few more sentences based on their importance scores
    if len(summary.split()) < word_limit:
        for sentence in sorted_sentences:
            if importance_scores[sorted_sentences.index(sentence)] <= threshold:
                if current_length + len(sentence) > max_length or len(summary.split()) + len(sentence.split()) > word_limit:
                    break
                summary += sentence + '. '
                current_length += len(sentence)

    return summary.strip()