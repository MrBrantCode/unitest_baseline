"""
QUESTION:
Given a number, return a string with dash``` '-' ```marks before and after each odd integer,  but do not begin or end the string with a dash mark.

Ex:
"""

def dashatize_number(num):
    try:
        # Convert the number to its absolute value and then to a string
        num_str = str(abs(num))
        
        # Use list comprehension to add dashes around odd digits
        result = ''.join(['-' + i + '-' if int(i) % 2 else i for i in num_str])
        
        # Replace double dashes with single dashes and strip any leading or trailing dashes
        result = result.replace('--', '-').strip('-')
        
        return result
    except:
        return 'None'