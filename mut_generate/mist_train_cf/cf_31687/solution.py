"""
QUESTION:
Implement a function `preserve_filters` that takes `match`, `admin_site`, `opts`, and `request` as inputs. The function should construct a `current_url` using `match.app_name` and `match.url_name`, and a `changelist_url` using `admin_site.name`, `opts.app_label`, and `opts.model_name`. If `current_url` matches `changelist_url`, return the URL-encoded query parameters of `request.GET`. Otherwise, return `None`. 

The function should use the following URL formats: 
- `current_url`: `{app_name}:{url_name}`
- `changelist_url`: `{admin_site.name}:{opts.app_label}_{opts.model_name}_changelist`
"""

def preserve_filters(match, admin_site, opts, request):
    """
    Preserves filters if the current URL matches the changelist URL.

    Args:
        match (object): An object containing app_name and url_name.
        admin_site (object): An object containing the admin site name.
        opts (object): An object containing app_label and model_name.
        request (object): An object containing the current request.

    Returns:
        str or None: The URL-encoded query parameters if the URLs match, otherwise None.
    """

    # Construct the current URL using match.app_name and match.url_name
    current_url = f'{match.app_name}:{match.url_name}'
    
    # Construct the changelist URL using admin_site.name, opts.app_label, and opts.model_name
    changelist_url = f'{admin_site.name}:{opts.app_label}_{opts.model_name}_changelist'
    
    # Compare the current URL with the changelist URL
    if current_url == changelist_url:
        # If they match, return the URL-encoded query parameters of request.GET
        return request.GET.urlencode()
    else:
        # If they don't match, return None
        return None