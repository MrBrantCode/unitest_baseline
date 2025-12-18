"""
QUESTION:
Create a function `extract_bracket_contents` that takes a string as input and returns a list of substrings enclosed within round brackets ( ) in the order of their occurrence. The function should handle hierarchically nested round brackets and process special typographic symbols.
"""

def extract_bracket_contents(string):
    def _extract_bracket_contents(nested_part):
        brackets = []
        bracket_count = 0
        current_bracket_content = ""
        for char in nested_part:
            if char == '(':
                if bracket_count > 0:
                    current_bracket_content += char
                bracket_count += 1
            elif char == ')':
                bracket_count -= 1
                if bracket_count == 0:
                    brackets.append(current_bracket_content)
                    current_bracket_content = ""
                else:
                    current_bracket_content += char
            elif bracket_count > 0:
                current_bracket_content += char
        return brackets
    return _extract_bracket_contents(string)