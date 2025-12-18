"""
QUESTION:
Create a function `new_user_id` that transforms a given string `user_id` according to the following rules: 

- Convert to lowercase.
- Remove any characters that are not alphanumeric, hyphen, underscore, or period.
- Replace consecutive periods with a single period.
- If the user ID starts or ends with a period, remove it.
- If the user ID is empty after the above steps, set it to "a".
- If the user ID exceeds 15 characters after the above steps, trim it to 15 characters. If the user ID ends with a period after the trimming, remove it.

The function should take a string `user_id` as input and return the transformed user ID.
"""

import re

def new_user_id(user_id: str) -> str:
    user_id = user_id.lower()
    user_id = re.sub(r'[^a-z0-9-_.]', '', user_id)
    user_id = re.sub(r'\.+', '.', user_id)
    user_id = user_id.strip('.')
    if not user_id:
        user_id = 'a'
    user_id = user_id[:15].rstrip('.')
    return user_id