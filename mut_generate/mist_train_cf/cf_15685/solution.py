"""
QUESTION:
Create a function called "add_info" that takes a dictionary as an argument. The function should prompt the user to enter the following information: 
- Occupation: 
- Favorite color: 
- Hobbies (can be multiple, separated by commas): 
- Street: 
- Zip Code: 

The function should handle cases where the user enters invalid input or skips a prompt by re-prompting until valid input is provided. Then, update the dictionary with the new information and add a nested dictionary called "address" with the street and zip code information. Finally, the function should return the updated dictionary.

Additionally, create a function called "display_info" that takes the updated dictionary and prints out the person's information in a nicely formatted way, handling cases where certain information is missing or not provided by the user by displaying a placeholder or default value instead.
"""

def add_info(person):
    """Prompts the user to enter information and updates the dictionary."""
    while True:
        occupation = input("Enter occupation: ")
        if occupation != "":
            break

    while True:
        favorite_color = input("Enter favorite color: ")
        if favorite_color != "":
            break

    while True:
        hobbies = input("Enter hobbies (separated by commas): ")
        if hobbies != "":
            hobbies_list = [hobby.strip() for hobby in hobbies.split(",")]
            break

    person["Occupation"] = occupation
    person["Favorite color"] = favorite_color
    person["Hobbies"] = hobbies_list

    while True:
        street = input("Enter street: ")
        if street != "":
            break

    while True:
        zip_code = input("Enter zip code: ")
        if zip_code != "":
            break

    address = {
        "Street": street,
        "Zip Code": zip_code
    }

    person["Address"] = address
    return person


def display_info(person):
    """Prints out the person's information in a nicely formatted way."""
    print("Name:", person.get("Name", "N/A"))
    print("Age:", person.get("Age", "N/A"))
    print("City:", person.get("City", "N/A"))
    print("Height:", person.get("Height", "N/A"))
    print("Occupation:", person.get("Occupation", "N/A"))
    print("Favorite color:", person.get("Favorite color", "N/A"))
    print("Hobbies:", ", ".join(person.get("Hobbies", [])))
    print("Address:")
    print("    Street:", person.get("Address", {}).get("Street", "N/A"))
    print("    Zip Code:", person.get("Address", {}).get("Zip Code", "N/A"))