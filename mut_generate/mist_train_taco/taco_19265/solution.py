"""
QUESTION:
Make your strings more nerdy: Replace all 'a'/'A' with 4, 'e'/'E' with 3 and 'l' with 1
e.g. "Fundamentals" --> "Fund4m3nt41s"


```if:csharp
Documentation:
Kata.Nerdify Method (String)

Nerdifies a string. Returns a copy of the original string with 'a'/'A' characters replaced with '4', 'e'/'E' characters replaced with '3', and 'l' characters replaced with '1'.

Syntax


public
static
string Nerdify(
string str
    )
  



Parameters

str

Type: System.String
The string to be nerdified.

Return Value

Type: System.String
  The nerdified string.


Exceptions



Exception
Condition

ArgumentNullException
str is null.



```
"""

def nerdify(txt: str) -> str:
    """
    Nerdifies a string by replacing 'a'/'A' with '4', 'e'/'E' with '3', and 'l' with '1'.

    Parameters:
    txt (str): The string to be nerdified.

    Returns:
    str: The nerdified string.
    """
    return txt.translate(str.maketrans('aAeEl', '44331'))