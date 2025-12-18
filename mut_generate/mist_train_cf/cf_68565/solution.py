"""
QUESTION:
Implement a function 'add_new_user' and 'display_user_details' to manage user data stored in a dictionary called 'my_dict'. The 'add_new_user' function should input user attributes (full name, age, city of residence, favorite book, and music genre) and store them as key-value pairs in 'my_dict'. The 'display_user_details' function should take a user's name as an argument and return their attributes from 'my_dict'; if the user's name does not exist, it should return an error message. The program should handle multiple user records, incorporate error handling mechanisms, and validate user input efficiently.
"""

def add_new_user(my_dict):
    """
    Adds a new user to the dictionary with their attributes.

    Args:
        my_dict (dict): The dictionary to store user data.

    Returns:
        dict: The updated dictionary with the new user's data.
    """
    name = input("Enter the user's full name: ")
    age = input("Enter the user's age: ")
    while True:
        try:
            age = int(age)
            break
        except ValueError:
            age = input("Please enter a valid age: ")
    city = input("Enter the user's city of residence: ")
    favorite_book = input("Enter the user's favorite book: ")
    favorite_music_genre = input("Enter the user's favorite music genre: ")
    my_dict[name] = {'age': age, 'city': city, 'favorite_book': favorite_book, 
                      'favorite_music_genre': favorite_music_genre}
    return my_dict


def display_user_details(my_dict, name):
    """
    Retrieves a user's details from the dictionary.

    Args:
        my_dict (dict): The dictionary containing user data.
        name (str): The name of the user to retrieve details for.

    Returns:
        dict or str: The user's details if found, otherwise an error message.
    """
    try:
        user_data = my_dict[name]
    except KeyError:
        return "An error occurred: The user's name does not exist in the dictionary."
    else:
        return user_data