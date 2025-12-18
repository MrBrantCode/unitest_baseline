"""
QUESTION:
Implement the function `construct_search_url(params, query, offset, number_of_results)` that constructs a URL for a search query based on the given parameters. The function should take into account the selected language, cookies, query, paging, and time range. The function parameters are:
- `params`: a dictionary containing the parameters for constructing the URL, including the language, cookies, and time range.
- `query`: the search query string.
- `offset`: the offset for paging.
- `number_of_results`: the number of results to be displayed.
Assuming `search_url` is a string with placeholders for query, offset, and number_of_results, `match_language`, `supported_languages`, `language_aliases`, `time_range_dict`, and `time_range_string` are defined elsewhere, and `urlencode` is from the `urllib.parse` module.
"""

from urllib.parse import urlencode

def construct_search_url(params, query, offset, number_of_results):
    language = match_language(params['language'], supported_languages, language_aliases).lower()
    params['cookies']['_EDGE_S'] = 'mkt=' + language + '&F=1'

    url = search_url.format(query=urlencode({'q': query}),
                            offset=offset,
                            number_of_results=number_of_results)

    if params['time_range'] in time_range_dict:
        url += time_range_string.format(interval=time_range_dict[params['time_range']])

    return url