"""
QUESTION:
Create a function named `create_closure` that takes a string and a number as arguments, and returns a new function that concatenates the string with the given number of exclamation marks. 

Create another function named `invoke_closures` that takes an array of closures and a string as arguments, invokes each closure with the string, and returns the concatenated results as a single string. 

Note that each closure should be invoked with no argument, and the string given to `invoke_closures` should not be used as an argument to the closures, but rather the string passed to `create_closure` should be used instead.
"""

def create_closure(string, number):
    def concatenate_exclamation_marks():
        return string + "!" * number
    return concatenate_exclamation_marks

def invoke_closures(closures):
    result = ""
    for closure in closures:
        result += closure()
    return result