"""
QUESTION:
Implement a function `filter_and_sort_urls(t_history_urls, _search, t_sort_order)` that filters and sorts a list of website history URLs based on a given search domain and sort order criteria. The function should take in the following parameters:
- `t_history_urls`: a list of strings representing website history URLs.
- `_search`: a string representing the search domain.
- `t_sort_order`: a list of dictionaries, each containing the keys 'sort' and 'order' to specify the sorting criteria.

The function should return a new list of URLs that match the search domain and are sorted based on the given criteria. If `t_sort_order` is empty, return the filtered URLs without sorting. The sorting criteria 'indexed' and 'asc' or 'desc' order are supported.
"""

def filter_and_sort_urls(t_history_urls, _search, t_sort_order):
    filtered_urls = [url for url in t_history_urls if _search in url]

    if not t_sort_order:
        return filtered_urls

    def custom_sort_key(url):
        for sort_criteria in t_sort_order:
            if sort_criteria['sort'] == 'indexed':
                index = url.find(_search)
                if index != -1:
                    return index if sort_criteria['order'] == 'asc' else -index
            # Handle other sorting criteria if needed

    sorted_urls = sorted(filtered_urls, key=custom_sort_key)
    return sorted_urls