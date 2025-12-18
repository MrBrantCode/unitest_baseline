"""
QUESTION:
Create a method called "printTitle" that takes no parameters and returns the title of a book as a string. The title should be displayed in uppercase letters with each word separated by a single space and leading/trailing spaces removed. Replace any vowels in the title with corresponding numbers: 'a' or 'A' with '4', 'e' or 'E' with '3', 'i' or 'I' with '1', 'o' or 'O' with '0', and 'u' or 'U' with '2'. The method should have a time complexity of O(n), where n is the length of the title.
"""

def printTitle(title):
    # Convert the title to uppercase and split into words
    words = title.upper().strip().split()
    
    # Replace vowels with corresponding numbers
    vowels = {'A': '4', 'E': '3', 'I': '1', 'O': '0', 'U': '2'}
    for i in range(len(words)):
        word = words[i]
        new_word = ''
        for letter in word:
            if letter in vowels:
                new_word += vowels[letter]
            else:
                new_word += letter
        words[i] = new_word
    
    # Join the words with a single space and return the title
    return ' '.join(words)