"""
QUESTION:
Create a complete `urlpatterns` list for a Django application that includes the admin panel, home page, leads page API, and user authentication and registration. The `urlpatterns` list should contain path configurations using the `include` function for the 'frontend', 'leads', and 'accounts' apps, as well as a path for the admin panel. The path configurations should use the `path` function from `django.urls` and `admin.site.urls` for the admin panel.
"""

def entrance(lst):
    return '\n'.join([f'{i+1}. {s}' for i, s in enumerate(lst)])