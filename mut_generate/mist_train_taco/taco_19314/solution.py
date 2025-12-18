"""
QUESTION:
You are given a secret message you need to decipher. Here are the things you need to know to decipher it:

For each word:
- the second and the last letter is switched (e.g. `Hello` becomes `Holle`)
- the first letter is replaced by its character code (e.g. `H` becomes `72`)

Note: there are no special characters used, only letters and spaces

Examples
```
decipherThis('72olle 103doo 100ya'); // 'Hello good day'
decipherThis('82yade 115te 103o'); // 'Ready set go'
```
"""

def decipher_message(message):
    def decipher_word(word):
        # Find the number of digits at the beginning of the word
        i = sum(map(str.isdigit, word))
        # Convert the digits to the corresponding character
        decoded = chr(int(word[:i]))
        # If the word has more than just the character code
        if len(word) > i + 1:
            decoded += word[-1]  # Append the last letter
        if len(word) > i:
            decoded += word[i + 1:-1] + word[i:i + 1]  # Append the middle part and the second letter
        return decoded
    
    # Split the message into words, decipher each word, and join them back into a string
    return ' '.join(map(decipher_word, message.split()))