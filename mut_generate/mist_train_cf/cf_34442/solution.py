"""
QUESTION:
Create a function named `get_view_function` that takes a URL pattern and returns the corresponding view function associated with that pattern. The function has access to a predefined list of URL patterns and their corresponding view functions. If the URL pattern is not found in the list, the function should return "404 Not Found". The predefined list of URL patterns and view functions is:
[
    ('auth/$', 'gchatautorespond.apps.autorespond.views.auth_view'),
    ('oauth2callback/$', 'gchatautorespond.apps.autorespond.views.auth_return_view'),
    ('worker_status/$', 'gchatautorespond.apps.autorespond.views.worker_status_view'),
    ('test/$', 'gchatautorespond.apps.autorespond.views.test_view'),
    ('$', 'gchatautorespond.apps.autorespond.views.autorespond_view'),
]
"""

def get_view_function(url_pattern: str) -> str:
    urlpatterns = [
        ('auth/$', 'gchatautorespond.apps.autorespond.views.auth_view'),
        ('oauth2callback/$', 'gchatautorespond.apps.autorespond.views.auth_return_view'),
        ('worker_status/$', 'gchatautorespond.apps.autorespond.views.worker_status_view'),
        ('test/$', 'gchatautorespond.apps.autorespond.views.test_view'),
        ('$', 'gchatautorespond.apps.autorespond.views.autorespond_view'),
    ]

    for pattern, view_function in urlpatterns:
        if url_pattern == pattern:
            return view_function

    return '404 Not Found'