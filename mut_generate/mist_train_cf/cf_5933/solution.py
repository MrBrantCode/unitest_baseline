"""
QUESTION:
Create a function named `parse_string` that takes a string as input and returns a dictionary where each key is a person's name and the corresponding value is another dictionary containing the person's age, occupation, and address (if available). The input string contains information about multiple people separated by the word "person". Each person's information includes their name, age, occupation, and optional address, which can occur before or after the other information. The format for each piece of information is the type (e.g., "name", "age", etc.) followed by the corresponding value.
"""

def parse_string(string):
    people_dict = {}
    words = string.split()
    current_name = ""
    current_age = 0
    current_occupation = ""
    current_address = ""
    
    for i in range(len(words)):
        if words[i] == "name":
            current_name = words[i+1]
        elif words[i] == "age":
            current_age = int(words[i+1])
        elif words[i] == "occupation":
            current_occupation = words[i+1]
        elif words[i] == "address":
            current_address = words[i+1]
        elif words[i] == "person":
            person_dict = {"age": current_age, "occupation": current_occupation}
            if current_address != "":
                person_dict["address"] = current_address
            people_dict[current_name] = person_dict
            current_name = ""
            current_age = 0
            current_occupation = ""
            current_address = ""
    
    return people_dict