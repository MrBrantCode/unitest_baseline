"""
QUESTION:
Create a function `process_nested_list` that takes a list of strings and/or nested lists as input. The function should process each string in the list by converting odd-indexed characters to uppercase and even-indexed characters to lowercase. If the list contains nested lists, the function should process them recursively. The processed strings should be separated by a space and semi-colon ';', while the elements within nested lists should be separated by a comma ','. The function should be able to handle a list of up to a million elements and a maximum nested list depth of 100.
"""

def process_nested_list(lst):
    """Process the nested list and convert it into a complex string"""
    def convert_string(s):
        """Convert char in string: odd-indexed to upper and even-indexed to lower"""
        return ''.join(c.upper() if i%2 else c.lower() for i, c in enumerate(s))

    def convert(lst):
        """Convert list of strings/nested lists to the required complex string"""
        result = []
        for element in lst:
            if type(element) is list:
                result.append(','.join(convert(element)))
            else:
                result.append(convert_string(element))
        return result

    return ' ; '.join(convert(lst))