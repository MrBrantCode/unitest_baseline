"""
QUESTION:
Implement a program with the following functions:

- `search_contact(contacts, name)`: Search for a name in the contacts dictionary and print the corresponding phone number if the name exists, otherwise print 'Contact not found!'.
- `update_contact(contacts, name, number)`: Update the phone number for a given name if it exists in the dictionary, otherwise add it to the dictionary. Validate the phone number to ensure it contains only numeric characters and is of length 10. If the phone number is invalid, print 'Invalid phone number!'.
- Initialize the contacts dictionary by taking names and phone numbers as input from the user until the user chooses to quit. Validate phone numbers during initialization and prompt the user to re-enter if a phone number is invalid. 

Note: Assume all names are unique and case-sensitive.
"""

def is_valid_phone_number(number):
    if len(number) != 10 or not number.isdigit():
        return False
    return True


def search_contact(contacts, name):
    if name in contacts:
        print('Phone number:', contacts[name])
    else:
        print('Contact not found!')


def update_contact(contacts, name, number):
    if not is_valid_phone_number(number):
        print('Invalid phone number!')
        return
        
    if name in contacts:
        contacts[name] = number
        print('Contact Updated!')
    else:
        contacts[name] = number
        print('Contact Added!')