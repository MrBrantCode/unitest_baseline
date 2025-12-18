"""
QUESTION:
Implement the `validate_and_search` function, which takes a search provider instance `sp` and a web framework request object `request` as parameters. The function should return an error code if the `request` object is `None` or does not contain a query; otherwise, it should call the `search` method of `sp` with the query from the `request` object and return the result. The function should handle the following scenarios: 
- If `request` is `None`, return `ERR_VALIDATE_SEARCH_NULL`.
- If `request` does not contain a query, return `ERR_VALIDATE_SEARCH_NO_QUERY`.
- If `request` is valid and contains a query, return the result of `sp.search(request["query"])`.
"""

def validate_and_search(sp, request):
    if request is None:
        return "ERR_VALIDATE_SEARCH_NULL"
    elif "query" not in request:
        return "ERR_VALIDATE_SEARCH_NO_QUERY"
    else:
        return sp.search(request["query"])