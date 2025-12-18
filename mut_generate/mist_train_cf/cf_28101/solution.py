"""
QUESTION:
Implement a function `get_pages_specs` that takes in a list of dictionaries `page_specs` representing page specifications and a function `page_factory` that returns a page object. The function should return a dictionary where the keys are the page names and the values are the page objects returned by the `page_factory`. Each dictionary in `page_specs` is expected to have a 'name' key.
"""

def get_pages_specs(page_specs, page_factory):
    return {spec['name']: page_factory(spec) for spec in page_specs}