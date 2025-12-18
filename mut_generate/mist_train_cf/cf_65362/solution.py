"""
QUESTION:
Construct a Python function named `Hyperlink` that dynamically generates secure HTTPS hyperlinks using the provided constituents. The function should accept the following parameters: sub-domain, main domain, path, query parameters (as a dictionary), and an optional hash value. It should return a string representing the constructed hyperlink. Ensure the function can accommodate any modification in the hyperlink configuration seamlessly and efficiently.
"""

from urllib.parse import urlencode

def Hyperlink(sub_domain, main_domain, path, parameters, hash_value=None):
    base = 'https://'
    sub_domain = sub_domain+'.'
    main_domain = main_domain+'.com/'
    path = path+'?'
    params = urlencode(parameters)

    link = base+sub_domain+main_domain+path+params

    if hash_value is not None:
        link += '#'+hash_value

    return link