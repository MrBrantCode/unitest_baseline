"""
QUESTION:
Create a function called `print_person_data` that takes a list of dictionaries as input, where each dictionary represents a person with keys 'name' and 'age'. The function should print the name and age of each person. However, for the person with the highest age, their age should be printed in Roman numerals, and for people whose name starts with a vowel, their age should be printed in binary. The function should handle cases where a person's name starts with a vowel and contains multiple vowels or uppercase vowels, and it should sort the data in descending order of age before printing. The function should also include error handling to handle invalid data or missing values.
"""

def print_person_data(data):
    """
    Prints the name and age of each person in the given list of dictionaries.
    The person with the highest age has their age printed in Roman numerals,
    and people whose name starts with a vowel have their age printed in binary.
    
    Args:
    data (list): A list of dictionaries, where each dictionary represents a person with keys 'name' and 'age'.
    """
    
    # Sort data by age in descending order
    try:
        sorted_data = sorted(data, key=lambda x: x['age'], reverse=True)
    except KeyError as e:
        print(f"Invalid data: Missing key {e}")
        return
    
    # Define function to convert Arabic numerals to Roman numerals
    def arabic_to_roman(n):
        roman_numerals = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }

        result = ''
        for value, numeral in roman_numerals.items():
            while n >= value:
                result += numeral
                n -= value
        return result
    
    # Iterate over sorted data and print name and age
    for i, person in enumerate(sorted_data):
        name = person['name']
        age = person['age']

        if i == 0:
            age_roman = arabic_to_roman(age)
            print(f"Name: {name}, Age: {age_roman}")
        elif name[0].lower() in ['a', 'e', 'i', 'o', 'u']:
            age_binary = bin(age)[2:]
            print(f"Name: {name}, Age: {age_binary}")
        else:
            print(f"Name: {name}, Age: {age}")