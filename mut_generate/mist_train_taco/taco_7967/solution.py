"""
QUESTION:
Given 2 strings, your job is to find out if there is a substring that appears in both strings. You will return true if you find a substring that appears in both strings, or false if you do not. We only care about substrings that are longer than one letter long.

#Examples:

````
*Example 1*
SubstringTest("Something","Fun"); //Returns false

*Example 2*
SubstringTest("Something","Home"); //Returns true
````
In the above example, example 2 returns true because both of the inputs contain the substring "me". (so**ME**thing and ho**ME**)  
In example 1, the method will return false because something and fun contain no common substrings. (We do not count the 'n' as a substring in this Kata because it is only 1 character long)

#Rules:
Lowercase and uppercase letters are the same. So 'A' == 'a'.  
We only count substrings that are > 1 in length.  

#Input:
Two strings with both lower and upper cases.
#Output:
A boolean value determining if there is a common substring between the two inputs.
"""

def has_common_substring(str1, str2):
    # Convert both strings to lowercase
    str1 = str1.lower()
    str2 = str2.lower()
    
    # Iterate through the first string to find substrings of length 2
    for i in range(len(str1) - 1):
        # Extract a substring of length 2
        substring = str1[i:i + 2]
        # Check if this substring is present in the second string
        if substring in str2:
            return True
    
    # If no common substring is found, return False
    return False