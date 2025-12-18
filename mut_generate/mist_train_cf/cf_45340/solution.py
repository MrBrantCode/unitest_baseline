"""
QUESTION:
Write a function named `sort_tuples` that sorts a list of tuples by the second value in each tuple. The tuples can contain both string and integer types. The function should handle exception cases, such as when elements within a tuple are not suitable for comparison.
"""

def sort_tuples(tuples_list):
    try:
        return sorted(tuples_list, key=lambda x: x[1])
    except TypeError as e:
        print(f"Error while sorting - {str(e)}")
    except Exception as e:
        print(f"Unexpected error - {str(e)}")