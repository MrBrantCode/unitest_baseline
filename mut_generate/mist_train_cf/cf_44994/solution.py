"""
QUESTION:
Create a function named `create_user_id` that generates a 10-character, case-insensitive, alphanumeric user ID from a given first name, last name, and date of birth. The generated user ID should be a hashed value of the combined user information. Note that the uniqueness of the generated ID is not guaranteed due to the intentional shortening of the hashed value.
"""

def create_user_id(first_name, last_name, dob):
    # Combine user info into a single string
    user_info = f"{first_name.lower()}_{last_name.lower()}_{dob}"
    # Use python's hash function to create a unique hash
    hashed_info = hash(user_info)
    # Convert the hash to a hex value and keep only 10 characters
    user_id = hex(hashed_info)[2:12]
    return user_id