"""
QUESTION:
Find the minimum length word from a given dictionary words, which has all the letters from the string licensePlate.  Such a word is said to complete the given string licensePlate

Here, for letters we ignore case.  For example, "P" on the licensePlate still matches "p" on the word.

It is guaranteed an answer exists.  If there are multiple answers, return the one that occurs first in the array.

The license plate might have the same letter occurring multiple times.  For example, given a licensePlate of "PP", the word "pair" does not complete the licensePlate, but the word "supper" does.


Example 1:

Input: licensePlate = "1s3 PSt", words = ["step", "steps", "stripe", "stepple"]
Output: "steps"
Explanation: The smallest length word that contains the letters "S", "P", "S", and "T".
Note that the answer is not "step", because the letter "s" must occur in the word twice.
Also note that we ignored case for the purposes of comparing whether a letter exists in the word.



Example 2:

Input: licensePlate = "1s3 456", words = ["looks", "pest", "stew", "show"]
Output: "pest"
Explanation: There are 3 smallest length words that contains the letters "s".
We return the one that occurred first.



Note:

licensePlate will be a string with length in range [1, 7].
licensePlate will contain digits, spaces, or letters (uppercase or lowercase).
words will have a length in the range [10, 1000].
Every words[i] will consist of lowercase letters, and have length in range [1, 15].
"""

def find_min_length_word(licensePlate, words):
    # Helper function to count the frequency of each letter in a string
    def count_letters(s):
        count = {}
        for char in s:
            if char.isalpha():
                char = char.lower()
                if char in count:
                    count[char] += 1
                else:
                    count[char] = 1
        return count
    
    # Count the letters in the licensePlate
    license_count = count_letters(licensePlate)
    
    # Initialize variables to track the minimum length word and its length
    min_word = None
    min_length = float('inf')
    
    # Iterate through each word in the list
    for word in words:
        word_count = count_letters(word)
        
        # Check if the word contains all the letters in the licensePlate with the required frequency
        if all(word_count.get(char, 0) >= license_count[char] for char in license_count):
            # If the word is shorter than the current minimum length word, update the minimum word
            if len(word) < min_length:
                min_word = word
                min_length = len(word)
    
    return min_word