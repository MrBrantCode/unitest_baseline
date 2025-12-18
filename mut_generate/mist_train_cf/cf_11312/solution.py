"""
QUESTION:
Create a function called `count_words` that takes a sentence as input and returns a dictionary containing the count of each word in the sentence, excluding common words like "the", "a", "an", etc. The function should ignore case, punctuation, and only consider unique words.
"""

def count_words(sentence):
    common_words = ["the", "a", "an", "and", "or", "but", "if", "is", "are", "was", "were", "has", "have", "had", "do", "does", "did", "for", "of", "with", "at", "by", "from", "in", "out", "on", "off", "to", "into", "onto", "up", "down", "over", "under", "through", "between", "among", "after", "before", "underneath", "above", "below", "around", "about", "near", "far", "away", "beneath", "beside", "besides", "behind", "ahead", "along", "upon", "against", "throughout", "during", "within", "without", "toward", "towards", "onto", "into", "over", "through", "behind", "in", "out", "up", "down", "on", "off", "across", "about", "above", "after", "against", "along", "among", "around", "as", "at", "before", "behind", "below", "beneath", "beside", "between", "beyond", "but", "by", "despite", "during", "for", "from", "in", "inside", "into", "near", "of", "off", "on", "onto", "out", "outside", "over", "past", "regarding", "round", "since", "through", "throughout", "till", "to", "toward", "under", "underneath", "until", "unto", "up", "upon", "with", "within", "without"]
    
    # Remove punctuation marks and convert the sentence to lowercase
    sentence = sentence.lower().replace(".", "").replace(",", "").replace("!", "").replace("?", "")
    
    # Split the sentence into a list of words
    words = sentence.split()
    
    # Create an empty dictionary to store the word counts
    word_counts = {}
    
    # Iterate through each word in the sentence
    for word in words:
        # Check if the word is not a common word
        if word not in common_words:
            # Check if the word is already in the dictionary
            if word in word_counts:
                # Increment the count of the word by 1
                word_counts[word] += 1
            else:
                # Add the word to the dictionary with a count of 1
                word_counts[word] = 1
    
    return word_counts