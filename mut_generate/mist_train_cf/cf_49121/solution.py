"""
QUESTION:
Create a function `sort_list` that takes in a list of integers and a string parameter `order` as input. The function should return a string of comma-separated values based on the given order, which can be either "asc" for ascending, "desc" for descending, or "unsorted". If the order is not one of these options, the function should return an error message. The function should also handle cases where the input list is empty or contains non-integer values, returning appropriate error messages in such scenarios.
"""

def sort_list(lst, order):
    try:
        # Check if the list is empty
        if not lst:
            return "The input list is empty"
            
        # Check if all elements are integers
        for num in lst:
            if type(num) != int:
                return "The list contains non-integer values"
            
        if order == "asc":
            lst.sort()
        elif order == "desc":
            lst.sort(reverse=True)
        elif order != "unsorted": # Check if order is either "asc", "desc" or "unsorted"
            return "Invalid sorting order. The order must be either 'asc', 'desc' or 'unsorted'"
                
        lst = [str(i) for i in lst] # Convert the integers to strings to join them
        return ", ".join(lst)
        
    except Exception as e:
        return "An error has occurred: "+str(e)