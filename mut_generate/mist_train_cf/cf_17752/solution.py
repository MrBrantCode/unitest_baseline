"""
QUESTION:
Create a function named `validate_age` to check if a given age is valid according to the following rules:

- The age must be within the range of 18 to 65 years old.
- The function should handle different input formats, including numerical values and textual representations of age (e.g., "twenty-five").
- The function should also check for invalid ages, including negative ages and ages exceeding the maximum human lifespan.
- The function should be able to handle age input in different calendar systems.

Assume that the `parse_age_text`, `parse_age_word`, and `get_maximum_lifespan` functions are already implemented.
"""

def validate_age(age):
    try:
        # Handle textual representations of age
        if isinstance(age, str):
            age = parse_age_text(age)
        
        # Check if age is within the specified range
        if not (18 <= age <= 65):
            return False
        
        # Check if age is negative or exceeds maximum lifespan
        if age < 0 or age > get_maximum_lifespan():
            return False
        
        return True
    
    except Exception as e:
        print(f"Error validating age: {str(e)}")
        return False