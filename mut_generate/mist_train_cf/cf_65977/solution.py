"""
QUESTION:
Create a function `maskPII(S)` that takes a string `S` representing personal information, either an email address or a phone number, and returns a masked version of the information.

For email addresses, the masking process involves converting all names to lowercase and replacing all letters between the first and last letter of the first name with 5 asterisks.

For phone numbers, the masking process involves exposing only the last 4 digits and masking all other digits. The local number should be formatted and masked as `***-***-1111`, where `1` represents the exposed digits. If a country code is present, it should be included in the masking.

The input string `S` has a length of at most 40 characters. Email addresses have a length of at least 8, and phone numbers have a length of at least 10.
"""

import re

def maskPII(S):
    if "@" in S: 
        first, after = S.split("@")
        return "{}*****{}@{}".format(
                first[0], first[-1], after).lower()

    else: 
        digits = re.sub('\D', '', S)
        local = "***-***-" + digits[-4:]
        if len(digits) == 10:
            return local
        return "+{}-{}".format('*'*(len(digits)-10), local)