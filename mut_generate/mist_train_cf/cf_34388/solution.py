"""
QUESTION:
Complete the `crime()` function to identify and count occurrences of specific crime types from a given list of words. The function should print a header "Crime Type | Crime ID | Crime Count", followed by each of the specific crime types ("ASSAULT", "ROBBERY", "THEFT OF VEHICLE", and "BREAK AND ENTER") along with their counts, and populate the list `lst` with the identified crime types. The function should also ensure that only crime types with a count greater than 0 are printed and added to `lst`.
"""

def crime(words):
    """
    Identifies and counts occurrences of specific crime types from a given list of words.
    
    Args:
        words (list): A list of words to process for crime types.
    
    Returns:
        list: A list of identified crime types.
    """
    
    # Initialize a dictionary to store the counts of each crime type
    crime_counts = {"ASSAULT": 0, "ROBBERY": 0, "THEFT OF VEHICLE": 0, "BREAK AND ENTER": 0}
    
    # Print the header for the crime data
    print(" Crime Type | Crime ID | Crime Count")
    
    # Iterate through the words to identify specific crime types and update counts
    for word in words:
        if word in crime_counts:
            crime_counts[word] += 1
    
    # Print the identified crime types and their counts
    for crime_type, count in crime_counts.items():
        if count > 0:
            print(f" {crime_type} | {hash(crime_type)} | {count}")
    
    # Return the identified crime types
    return [crime_type for crime_type, count in crime_counts.items() if count > 0]