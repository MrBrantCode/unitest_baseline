"""
QUESTION:
Create a function `validate` that takes in parameters `accessed`, `container`, `name`, `value`, `context`, `roles`, and optional parameters `*args` and `**kw`. The function should implement a custom security policy to enforce access control based on the provided parameters. It should return `1` if access is permitted and `0` if access is denied. The policy should consider the following rules: deny access to "sensitive_resource" for non-admin users and deny access to "public_resource" from an external context; allow access for all other cases.
"""

def validate(accessed, container, name, value, context, roles, *args, **kw):
    # Custom security policy implementation
    if accessed == "sensitive_resource" and "admin" not in roles:
        return 0  # Deny access to sensitive_resource for non-admin users
    elif accessed == "public_resource" and context == "external":
        return 0  # Deny access to public_resource from external context
    else:
        return 1  # Allow access for other cases