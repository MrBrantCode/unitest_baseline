"""
QUESTION:
Create a function `update_contact` that updates a contact's details in a database. The function should take three parameters: `existing_phone_number`, `new_phone_number`, and `new_name`. 

The function should first check if the contact with the `existing_phone_number` exists in the database. If not, it should return an error message. 

Next, it should check if the `new_phone_number` is already assigned to another contact in the database. If it is, the function should return an error message. 

If both checks pass, the function should update the contact's details with the `new_phone_number` and `new_name`, and return the updated contact's details. 

The function should handle potential errors and return corresponding error messages. The function should also include unit tests to ensure its correctness.
"""

def update_contact(existing_phone_number, new_phone_number, new_name, contacts):
    """
    Updates a contact's details in the database.

    Args:
    existing_phone_number (str): The existing phone number of the contact.
    new_phone_number (str): The new phone number of the contact.
    new_name (str): The new name of the contact.
    contacts (dict): A dictionary representing the contact database.

    Returns:
    dict: A dictionary containing the updated contact's details or an error message.
    """
    
    # Check if the contact with the existing_phone_number exists in the database
    if existing_phone_number not in contacts:
        return {"error": "Contact with given phone number does not exist"}
    
    # Check if the new_phone_number is already assigned to another contact in the database
    if new_phone_number in contacts and new_phone_number != existing_phone_number:
        return {"error": "New phone number is already assigned to another contact"}
    
    # Update the contact's details with the new_phone_number and new_name
    contacts[new_phone_number] = new_name
    if existing_phone_number != new_phone_number:
        del contacts[existing_phone_number]
    
    # Return the updated contact's details
    return {"message": "Contact updated successfully", "contact": {"phone_number": new_phone_number, "name": new_name}}