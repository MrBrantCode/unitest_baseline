"""
QUESTION:
Write a function named `unusual_addition` that accepts a list of strings, where each string contains only numerical digits. For each string, replace 'i' with the count of odd digits and 'e' with the count of even digits in the string, then return the modified strings in a list.
"""

def unusual_addition(lst):
    """This function accepts a list solely made up of strings containing numerical digits only and returns a list.
    In the output, for each element, replace the 'i' with the true count of odd digits and 'e' with the true count of even digits in 
    the i'th string from the input.
    """
    output = []
    for idx, str in enumerate(lst):
        odd_count = sum(1 for s in str if int(s) % 2 != 0)
        even_count = sum(1 for s in str if int(s) % 2 == 0)
        replace_string = f"the number of odd elements {odd_count}n the str{even_count}ng {even_count} of the {odd_count}nput."
        output.append(replace_string)

    return output