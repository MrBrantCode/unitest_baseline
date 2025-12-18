"""
QUESTION:
Create a function named `word_sum` that takes an array of lowercase words as input. Each word can have at most 10 characters, and the array can have at most 100 words. The function should return the total sum of the computed sums, where each character in the word is replaced with its corresponding number from the English alphabet (a=1, b=2, ..., z=26).
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