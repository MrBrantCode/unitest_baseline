"""
QUESTION:
Implement a `build_tables` method in the `TableManager` class. The method should take `name`, `values`, `time_values`, `functions`, and `percentages` as parameters. The `functions` and `percentages` parameters are optional. The method should create a table with the given `name`, add the attributes from `values` and `time_values`, apply the functions from `functions` to the attributes if provided, calculate the percentages for the attributes from `percentages` if provided, and store the table in the `TableManager` instance.
"""

def build_tables(name, values, time_values, functions=None, percentages=None):
    table = {
        'name': name,
        'attributes': values + time_values
    }

    if functions:
        for attr, func in functions.items():
            if attr in table['attributes']:
                idx = table['attributes'].index(attr)
                table['attributes'][idx] = func(table['attributes'][idx])

    if percentages:
        for attr, percent in percentages.items():
            if attr in table['attributes']:
                idx = table['attributes'].index(attr)
                table['attributes'][idx] = f"{table['attributes'][idx]} ({percent}%)"

    return table