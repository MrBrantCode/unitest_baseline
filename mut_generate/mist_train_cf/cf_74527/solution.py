"""
QUESTION:
Implement a function named `valid_url` and use it in a Flask route named `home` that handles POST requests. The `valid_url` function should validate the input URL based on the following criteria:

* The URL should be well-formed, with a scheme (e.g., http or https) and a network location (e.g., domain name).
* The URL's domain name should match a whitelist of allowed domains.

The `home` route should redirect the user to the input URL if it is valid, and return a 400 error if it is not. The function should also handle potential runtime errors. Implement unit tests to ensure the code works as expected. The whitelist of allowed domains includes `test.website.com`, `my.domain.com`, and `another.allowed.domain`.
"""

import re
from urllib.parse import urlparse

def valid_url(url): 
  try: 
    parsed_url = urlparse(url)
    if bool(parsed_url.scheme) and bool(parsed_url.netloc): 
      if re.fullmatch(r'(www\.)?(test\.website\.com|my\.domain\.com|another\.allowed\.domain)', parsed_url.netloc): 
        return True
    elif url == "":
      return False
    else: 
      return False
  except: 
  # This exception block will handle cases where input is not in string format
    return False