"""
QUESTION:
Create a function `longest_substring_length` that takes two parameters: `string` and `threshold`. The function should find the length of the longest substring without duplicate characters within the given threshold distance. It should handle cases where the input string contains non-alphabetic characters by returning an error message. The function should ignore case sensitivity and have a time complexity of O(n). It should not use built-in functions or data structures to track duplicate characters. If the input string is empty, it should return an error message.
"""

def longest_substring_length(string, threshold):
    # Check if the string is empty or consists only of non-alphabetic characters
    if not string.isalpha():
        return "Error: Invalid input. String contains non-alphabetic characters."
    
    # Convert the string to lowercase
    string = string.lower()
    
    # Initialize variables
    start = 0
    longest_length = 0
    visited = [False] * 26
    
    for i in range(len(string)):
        # Check if the current character is a duplicate within the threshold distance
        if visited[ord(string[i]) - ord('a')]:
            # Find the index of the duplicate character within the threshold distance
            for j in range(i - threshold, i):
                if j >= 0 and string[j] == string[i]:
                    start = j + 1
                    break
        
        # Update the longest length if necessary
        if i - start + 1 > longest_length:
            longest_length = i - start + 1
        
        # Mark the current character as visited
        visited[ord(string[i]) - ord('a')] = True
    
    return longest_length