"""
QUESTION:
Create a function named `extractKeywords` that takes a string `text` as input and returns the top 10 keywords. The function should ignore common words such as "is", "that", "am", and "to". It should count the frequency of each keyword in the text and return the top 10 keywords based on their frequency in descending order. If there are fewer than 10 unique keywords in the text, the function should return all the unique keywords. If there are multiple keywords with the same frequency, the function should sort them alphabetically.
"""

def extractKeywords(text):
    common_words = ["is", "that", "am", "to"]
    text = text.lower().split()
    words = [word for word in text if word not in common_words]
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    sorted_keywords = sorted(word_freq, key=lambda x: (-word_freq[x], x))
    return sorted_keywords[:10]