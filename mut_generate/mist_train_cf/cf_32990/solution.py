"""
QUESTION:
Write a function `categorize_finite_element_functions` that takes a list of function names as input and returns a dictionary. The input function names are categorized based on their prefix: "H8" for 8-node elements, "Q4" for 4-node elements, and "Q5" for 5-node elements. The function should group the input function names into these three categories and return a dictionary with the element types ("H8", "Q4", "Q5") as keys and lists of corresponding function names as values.
"""

def categorize_finite_element_functions(functions):
    categorized_functions = {'H8': [], 'Q4': [], 'Q5': []}
    
    for function in functions:
        if function.startswith('H8'):
            categorized_functions['H8'].append(function)
        elif function.startswith('Q4'):
            categorized_functions['Q4'].append(function)
        elif function.startswith('Q5'):
            categorized_functions['Q5'].append(function)
    
    return categorized_functions