"""
QUESTION:
Write a function `decodePermissions` that takes an integer `permissionSum` as input, where the integer represents the sum of various permissions represented as powers of 2 in decimal format. The function should return a list of strings representing the individual permissions granted. 

The permissions and their corresponding decimal values are:
- MANAGE_WEBHOOKS: 536870912
- MANAGE_EMOJIS_AND_STICKERS: 1073741824
- USE_APPLICATION_COMMANDS: 2147483648
- REQUEST_TO_SPEAK: 4294967296
- MANAGE_THREADS: 17179869184
- CREATE_PUBLIC_THREADS: 34359738368
- CREATE_PRIVATE_THREADS: 68719476736
- USE_EXTERNAL_STICKERS: 137438953472
- SEND_MESSAGES_IN_THREADS: 274877906944
- START_EMBEDDED_ACTIVITIES: 549755813888
"""

def decodePermissions(permissionSum):
    permissions = {
        "MANAGE_WEBHOOKS": 536870912,
        "MANAGE_EMOJIS_AND_STICKERS": 1073741824,
        "USE_APPLICATION_COMMANDS": 2147483648,
        "REQUEST_TO_SPEAK": 4294967296,
        "MANAGE_THREADS": 17179869184,
        "CREATE_PUBLIC_THREADS": 34359738368,
        "CREATE_PRIVATE_THREADS": 68719476736,
        "USE_EXTERNAL_STICKERS": 137438953472,
        "SEND_MESSAGES_IN_THREADS": 274877906944,
        "START_EMBEDDED_ACTIVITIES": 549755813888
    }
    
    result = []
    for permission, value in permissions.items():
        if value & permissionSum:
            result.append(permission)
    
    return result