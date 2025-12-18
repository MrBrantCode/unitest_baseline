"""
QUESTION:
Write a function `parse_database_uri` that takes a string input representing a database URI in the format "dialect+driver://username:password@host:port/database" and returns a dictionary containing the username, password, host, port, and database name as its keys. Assume the input string will always follow the specified format and the port is an integer.
"""

def parse_database_uri(uri):
    components = uri.split("://")[1].split("@")[0].split(":")
    username = components[0]
    password = components[1]
    host_port = uri.split("@")[1].split("/")[0].split(":")
    host = host_port[0]
    port = int(host_port[1])
    database = uri.split("/")[-1]
    return {
        'username': username,
        'password': password,
        'host': host,
        'port': port,
        'database': database
    }