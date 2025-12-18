"""
QUESTION:
Implement a function `extract_keywords(input_string: str) -> dict` that takes a string as input and returns a dictionary where the keys are the main keywords (denoted by '#') and the values are lists of sub-keywords (denoted by '$') associated with each main keyword. The input string is formatted into lines where the main keyword line starts with "Main-Keywords (#):" followed by the main keyword, and the sub-keyword line starts with "Sub-Keywords ($) per Main-Keyword:" followed by the sub-keyword.
"""

def extract_keywords(input_string: str) -> dict:
    result = {}
    lines = input_string.split("\n")

    for line in lines:
        if line.startswith("Main-Keywords (#):"):
            main_keywords = line.split(":")[1].strip()
            result[main_keywords] = []
        elif line.startswith("Sub-Keywords ($) per Main-Keyword:"):
            sub_keywords = line.split(":")[1].strip()
            for main_keyword in result:
                result[main_keyword].append(sub_keywords)

    return result