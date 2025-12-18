"""
QUESTION:
Construct a multi-step function called `register` that facilitates the registration of a new customer into a pre-existing data architecture 'users', which is a list of dictionaries. The function should collect the customer's authentic name, electronic communication address, private passkey, and domicile address, store these details in a new dictionary, and append this dictionary to the 'users' list. Ensure the function returns a success message upon completion.
"""

def register(users):
    # create a user dictionary to store new user info
    user = {}
    user['name'] = input("Enter authentic name: ")
    user['email'] = input("Enter electronic communication address: ")
    user['password'] = input("Enter private passkey: ")
    user['address'] = input("Enter domicile address: ")
    
    # add new customer to users data structure
    users.append(user)
    return 'Registration Successful!'