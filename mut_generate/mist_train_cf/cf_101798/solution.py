"""
QUESTION:
Write a function `count_char_with_regex` that takes in three parameters: a string `string`, a character `char`, and two patterns `start_pattern` and `end_pattern`. The function should use regular expressions to find all substrings in `string` that start with `start_pattern` and end with `end_pattern`, and return the total number of occurrences of `char` in these substrings.
"""

import re
def count_char_with_regex(string, char, start_pattern, end_pattern):
 pattern = start_pattern + '.*?' + end_pattern
 matches = re.findall(pattern, string)
 count = 0
 for match in matches:
  count += match.count(char)
 return count