"""
QUESTION:
Create a method `extract_credentials` within a class that can parse an XML snippet of a `UsernamePasswordCredentialsImpl` and return a dictionary containing the extracted username and password. The XML snippet is in the following format:
```xml
<com.cloudbees.plugins.credentials.impl.UsernamePasswordCredentialsImpl>
    <scope>GLOBAL</scope>
    <id>Test Credential</id>
    <username>Test-User</username>
    <password><PASSWORD></password>
</com.cloudbees.plugins.credentials.impl.UsernamePasswordCredentialsImpl>
```
The returned dictionary should have the format `{'username': 'username', 'password': 'password'}`. The solution should use the `xml.etree.ElementTree` module for XML parsing.
"""

import xml.etree.ElementTree as ET

def extract_credentials(xml_string):
    """
    Extracts username and password from a given XML snippet.

    Args:
        xml_string (str): The XML snippet to parse.

    Returns:
        dict: A dictionary containing the extracted username and password.
    """
    root = ET.fromstring(xml_string)
    username = root.find('username').text
    password = root.find('password').text
    return {'username': username, 'password': password}