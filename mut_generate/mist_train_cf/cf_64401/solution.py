"""
QUESTION:
Write a function named `find_customers` that takes a list of customer names as input. The function should return a list of customer names that contain the string "ali", sorted in descending order by the total number of occurrences of the substring "a" in the name. The search for "ali" should be case-insensitive.
"""

def find_customers(customers):
    # Filter out the customer names with 'ali'
    ali_customers = [name for name in customers if 'ali' in name.lower()]

    # Get the count of 'a' in each name along with the name
    counts = [(name, name.lower().count('a')) for name in ali_customers]

    # Sort by count of 'a' in descending order
    counts.sort(key=lambda x: x[1], reverse=True)

    # Return only the names sorted by count of 'a'
    return [name for name, _ in counts]