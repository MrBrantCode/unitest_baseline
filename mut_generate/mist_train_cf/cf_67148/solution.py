"""
QUESTION:
Create a function `replace_email_url` that takes a string `s` as input and returns a string where all email addresses and URLs are replaced with 'EMAIL' and 'URL' respectively. The function should use regular expressions to identify email addresses and URLs, covering most common formats, including edge cases with erroneous or incomplete addresses and URLs.
"""

import re

def replace_email_url(s):
    # The regular expression for emails:
    # In the user name part, it accepts alphanumeric characters, periods, hyphens, and underscore
    # In the domain name part, it accepts alphanumeric characters, periods, and hyphens
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    # The regular expression for urls:
    # It accepts http, https, ftp and can handle urls without http, https, ftp.
    # It can also handle urls ending with a period or a comma.
    url_pattern = r'(http://www\.|https://www\.|http://|https://)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(/.*)?'

    s = re.sub(email_pattern, 'EMAIL', s)
    s = re.sub(url_pattern, 'URL', s)
    return s