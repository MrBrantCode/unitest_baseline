"""
QUESTION:
Create a function `extract_ftp_url(s)` that takes a Unicode character string `s` as input and returns a dictionary containing the components of an FTP URL if found. The FTP URL is expected to be in the format "ftp://user:password@host:port/path". The function should be able to extract the user, password, host, port (optional), and path (optional) from the URL.
"""

import re

def extract_ftp_url(s):
    ftp_url_exp = re.compile(r""" 
        ftp:\/\/  # protocol
        (?P<user>[^:]+):     # user
        (?P<password>[^@]+)@  # password
        (?P<host>[^:\/]+)     # host
        (?::                  
        (?P<port>\d+))?       # port (optional)
        (?:\/
        (?P<path>.*))?        # path (optional)
        """, re.X)

    match = ftp_url_exp.search(s)

    return match.groupdict() if match else None