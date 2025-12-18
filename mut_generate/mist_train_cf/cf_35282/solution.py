"""
QUESTION:
Implement a function `process_query_strategy(settings)` that takes a dictionary `settings` as input. The dictionary contains a 'query_strategy' key with a string value that determines the query strategy to be used. The function should handle the query strategy as follows:
- If 'query_strategy' is 'max' or 'max_sampling', return a function along with the description "Maximum inclusion sampling".
- If 'query_strategy' is 'rand_max' or 'rand_max_sampling', modify the 'rand_max_frac' parameter in 'query_kwargs' of the input dictionary to 0.05 and return the modified dictionary.
"""

def process_query_strategy(settings):
    method = settings['query_strategy']
    if method in ['max', 'max_sampling']:
        def max_sampling():
            # Implementation of max_sampling function
            pass
        return max_sampling, "Maximum inclusion sampling"
    if method in ['rand_max', 'rand_max_sampling']:
        settings['query_kwargs']['rand_max_frac'] = 0.05
        return settings