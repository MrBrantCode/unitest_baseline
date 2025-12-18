"""
QUESTION:
Create a function called `addCustomerProfile` to store customer information. The function should take in three parameters: `name`, `address`, and `phoneNumber`. It should store the customer information in a structured data repository, where each customer's profile includes their name, address, and phone number. The function should be able to handle multiple customer profiles and allow for easy retrieval of the stored information.
"""

# Function to add customer profiles
def addCustomerProfile(customerProfiles, name, address, phoneNumber):
    customerProfiles[name] = {
        "Address":address, 
        "Phone Number":phoneNumber
    }
    return customerProfiles