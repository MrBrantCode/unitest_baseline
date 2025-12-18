"""
QUESTION:
Construct a function `convert_and_print_people` that takes a JSON list of people, where each person is an object with 'name' and 'age' properties. Iterate over the list, and for each person, print their name and age in the format "Name: [name], Age: [age]". However, for the person with the highest age, convert their age to Roman numerals before printing. Assume the input list contains at least one person, and ages are positive integers. The function should not take any additional arguments other than the list of people.
"""

def convert_and_print_people(people):
    # Find the person with the highest age
    max_age = max(people, key=lambda x: x["age"])["age"]

    # Function to convert Arabic numerals to Roman numerals
    def convert_to_roman(num):
        roman_numerals = {
            1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL',
            50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
        }
        result = ''
        for value, numeral in sorted(roman_numerals.items(), reverse=True):
            while num >= value:
                result += numeral
                num -= value
        return result

    # Iterate over the data and print the name and age
    for person in people:
        name = person["name"]
        age = person["age"]
        if age == max_age:
            age = convert_to_roman(age)
        print(f"Name: {name}, Age: {age}")