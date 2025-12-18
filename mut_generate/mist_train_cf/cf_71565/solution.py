"""
QUESTION:
Write a function `calculateVowelCountAndWordDetail` that takes a string as input and returns a tuple containing the total number of vowels (both lowercase and uppercase) in the string and the number of words that start or end with a vowel.
"""

def calculateVowelCountAndWordDetail(inputString):
    # list of vowels
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    # convert the string to lowercase
    inputString = inputString.lower()
    
    # calculate total vowel and word count 
    vowelCount = 0
    vowelStartEndWordCount = 0
    words = inputString.split() # split string into words
    
    for word in words:
        for char in word:
            if char in vowels:
                vowelCount += 1
        
        # check if first and last character of the word are vowels
        if word[0] in vowels or word[-1] in vowels:
            vowelStartEndWordCount += 1
            
    return (vowelCount, vowelStartEndWordCount)