"""
QUESTION:
Implement a function `words_to_numbers(input)` that translates English-word numerals into their digital representation. The function should take a string `input` as an argument, which contains a number written in words, and return the digital representation of that number as a string. 

For example, "one thousand two hundred and thirty four" should return '1234'. The input string may contain the words "and" and hyphenated numbers (e.g., "twenty-two"), which should be ignored and handled correctly.
"""

def words_to_numbers(input):
    word = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8,
            "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
            "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20, "thirty": 30,
            "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90, "hundred": 100,
            "thousand": 1000, "million": 1000000, "billion": 1000000000, "trillion": 1000000000000}

    current = result = 0
    for part in input.replace("-", " ").split():
        if part in ["and", "minus"]:
            continue
        
        if part not in word:
            return "error"
        else:
            val = word[part]
            
            # if the word represents hundreds, thousands, millions or billions
            if val >= 100:
                if current == 0:
                    current = val
                else:
                    current *= val
            # if the word represents units or tens
            else:
                current += val
            
            # if the current number is a valid number by itself (e.g., 1200 in "one thousand two hundred")
            if current >= 1000 or val == 100:
                result += current
                current = 0

    return str(result + current)