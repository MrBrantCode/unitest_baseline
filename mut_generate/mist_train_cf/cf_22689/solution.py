"""
QUESTION:
Write a function called `shortest_substring_word` that takes an array of words and a string as input. The function should find the shortest word in the array that is a substring of the string, ignoring case differences, and return it in lowercase. The array can contain duplicates and the string can contain special characters and spaces. The length of the words in the array and the string is limited to 100 characters. If no word in the array is a substring of the string, the function should return an empty string.
"""

def shortest_substring_word(arr, string):
    # Initialize the shortest word to be a very long word
    shortest_word = "a" * 101
    
    # Iterate through each word in the array
    for word in arr:
        # Check if the word in lowercase is a substring of the string in lowercase
        if word.lower() in string.lower():
            # Check if the word is shorter than the current shortest word
            if len(word) < len(shortest_word):
                shortest_word = word
                
    # Return the shortest word in lowercase if it was found, otherwise return an empty string
    return shortest_word.lower() if len(shortest_word) <= 100 else ""