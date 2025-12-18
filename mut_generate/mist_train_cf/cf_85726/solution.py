"""
QUESTION:
Write a function `transform_string_to_dictionary` that takes a string of person profiles as input, where profiles are separated by semicolons, and each profile's details (name, age, profession) are separated by commas. The function should return a dictionary where the person's name is the key, and the value is a nested dictionary with keys 'age' and 'profession'. The function should validate the input data, handle missing or incorrect information, and accommodate whitespace irregularities.
"""

def transform_string_to_dictionary(input_string):
    persons_dict = {}
    persons = input_string.split(";")
    for person in persons:
        if person: 
            person_details = [x.strip() for x in person.split(",")] 
            if len(person_details) == 3: 
                name, age, profession = person_details
                if name and age.isdigit() and profession: 
                    persons_dict[name] = {'age' : int(age), 'profession' : profession} 
    return persons_dict