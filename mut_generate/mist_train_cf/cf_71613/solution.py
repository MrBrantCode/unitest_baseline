"""
QUESTION:
Create a function named `classify_column_names` to categorize a list of column names into predefined categories. The function should map each column name to a single word, such as 'email' or 'givenName'. The function should be able to handle dissimilar names like 'email_addr', 'email_address', 'first_name', 'firstName', etc.
"""

def classify_column_names(column_names):
    # Create a dictionary or map of synonyms for each classified word
    synonyms = {
        'email': ['email', 'email_addr', 'email_address'],
        'givenName': ['first', 'first_name', 'firstName', 'christianName', 'christian_name'],
        # Add more categories as needed
    }

    # Initialize an empty dictionary to store the classified column names
    classified_names = {}

    # Iterate over each column name
    for column_name in column_names:
        # Initialize a flag to check if the column name is classified
        classified = False

        # Iterate over each category and its synonyms
        for category, synonym_list in synonyms.items():
            # Check if the column name is in the list of synonyms
            if column_name.lower() in [synonym.lower() for synonym in synonym_list]:
                # If it is, add it to the classified names dictionary with the category as the key
                classified_names[column_name] = category
                classified = True
                break

        # If the column name is not classified, add it to the dictionary with a default category
        if not classified:
            classified_names[column_name] = 'unknown'

    return classified_names