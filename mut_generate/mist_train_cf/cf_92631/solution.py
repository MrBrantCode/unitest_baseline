"""
QUESTION:
Replace each character in an array of words with its corresponding number from the English alphabet (a=1, b=2, ...z=26) and return the total sum of the computed word sums. Each word will have at most 10 lowercase letters and the array will have at most 100 words. Implement a function named `word_sum` that takes an array of words as input and returns the total sum.
"""

def word_sum(arr):
    total_sum = 0

    for word in arr:
        word_sum = 0
        for char in word:
            # Calculate the number corresponding to each character
            char_num = ord(char) - ord('a') + 1
            word_sum += char_num
        
        total_sum += word_sum
    
    return total_sum