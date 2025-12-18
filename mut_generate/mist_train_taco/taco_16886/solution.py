"""
QUESTION:
The idea for this Kata came from 9gag today.[here](http://9gag.com/gag/amrb4r9)

[screen]:("http://img-9gag-fun.9cache.com/photo/amrb4r9_700b.jpg")

You'll have to translate a string to Pilot's alphabet (NATO phonetic alphabet) [wiki](https://en.wikipedia.org/wiki/NATO_phonetic_alphabet).

Like this:

**Input:**

`If, you can read?`

**Output:**

`India Foxtrot , Yankee Oscar Uniform Charlie Alfa November Romeo Echo Alfa Delta ?`

**Notes**

* The set of used punctuation is `.!?`.
* Punctuation should be kept in your return string, but spaces should not.
* __Xray__ should not have a dash within.
* Every word and punctuation mark should be seperated by a space ' '.
* There should be no trailing whitespace


~~~if:php
Although the proper alphabet for j is `Juliett` you have to use `Juliet` here
~~~
"""

import string

# Define the NATO phonetic alphabet dictionary
db = {
    'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo', 
    'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliett', 
    'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar', 
    'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango', 
    'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'Xray', 'Y': 'Yankee', 
    'Z': 'Zulu'
}

def translate_to_nato(words):
    # Remove spaces and convert to uppercase
    words = words.replace(' ', '').upper()
    
    # Translate each character to its NATO phonetic equivalent
    translated = [db[char] if char in db else char for char in words]
    
    # Join the list into a single string with spaces
    return ' '.join(translated)