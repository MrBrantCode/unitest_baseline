"""
QUESTION:
Create a function called `authenticate_url(url)` that takes a string `url` as input and returns a boolean indicating whether the URL starts with 'https://', has at most three subdomains with alphanumeric characters only (separated by '.'), and ends with '.com'. The function should use regular expressions for validation.
"""

import re

def authenticate_url(url):
  pattern = r'^https:\/\/([A-Za-z0-9]+\.){1,3}com$'
  if re.match(pattern, url):
    return True
  else:
    return False