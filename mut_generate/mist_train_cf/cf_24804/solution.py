"""
QUESTION:
Write a function named `most_freq_word` that takes a list of words as input and returns the most frequently used word. The function should be case sensitive, meaning 'apple' and 'Apple' are considered different words. If there are multiple words with the same highest frequency, it should return any one of them.
"""

def most_freq_word(words): 
    # Create an empty dictionary 
    freq = {} 
  
    # Iterate over the list of words 
    for word in words: 
        # Check if word is already present in the freq dictionary 
        if (word in freq): 
            #Increment the count of word 
            freq[word] += 1
        else: 
            # Add it to the dictionary with a count of one 
            freq[word] = 1
  
    # Get the count of most frequent word 
    max_count = max(freq.values()) 
  
    # Loop over words and return the most frequent one 
    for key, value in freq.items(): 
        if value == max_count: 
            return key