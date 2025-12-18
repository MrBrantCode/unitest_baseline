"""
QUESTION:
Create a function `categorize_age` that takes a Pandas DataFrame with a column 'age' and adds a new column 'age_group' containing categorical values based on the age. The categorization should be as follows: people under 18 are "young", people between 18 and 64 (inclusive) are "adult", and people 65 and older are "elderly".
"""

def categorize_age(age):
    if age < 18:
        return "young"
    elif 18 <= age < 65:
        return "adult"
    else:
        return "elderly"