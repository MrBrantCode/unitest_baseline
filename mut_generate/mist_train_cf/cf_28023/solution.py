"""
QUESTION:
Implement a decorator named `route_join_with_or_without_slash` that registers routes for endpoints with and without trailing slashes and supports variable path segments. The decorator should take the following parameters: `blueprint`, `route`, `methods`, and an optional `path`. It should register the route for both the provided route and the route with a trailing slash appended. If a `path` parameter is provided, the decorator should register the route with the variable path segment.
"""

def route_join_with_or_without_slash(blueprint, route, *args, **kwargs):
    def decorator(f):
        blueprint.add_url_rule(route, view_func=f, *args, **kwargs)
        if not route.endswith('/'):
            blueprint.add_url_rule(route + '/', view_func=f, *args, **kwargs)
        return f
    return decorator