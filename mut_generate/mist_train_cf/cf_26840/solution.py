"""
QUESTION:
Implement a `UserCollectionSerializer` class that serializes and deserializes user data, ensuring that the username is not empty and unique, the password is not empty and meets certain complexity requirements, and the admin status is a boolean value. The class should have the following functionalities:

- Accept user data for serialization and validate it according to the specified rules.
- Accept serialized user data for deserialization and validate it according to the same rules as serialization.

The `UserCollectionSerializer` class should have an `is_valid` method to perform validation and return `True` if the data is valid and `False` otherwise. The class should also store any validation errors in an `errors` attribute.

Implement the serialization and deserialization logic in the `UserCollectionSerializer` class.
"""

def user_collection_serializer(data):
    errors = {}

    if 'username' in data:
        if not data['username']:
            errors['username'] = ['Username cannot be empty']
    else:
        errors['username'] = ['Username is required']

    if 'password' in data:
        if not data['password']:
            errors['password'] = ['Password cannot be empty']
    else:
        errors['password'] = ['Password is required']

    if 'is_admin' in data:
        if str(data['is_admin']) not in ['True', 'False', 'true', 'false']:
            errors['is_admin'] = ['Invalid value for admin status']
    else:
        errors['is_admin'] = ['Admin status is required']

    return not bool(errors), errors