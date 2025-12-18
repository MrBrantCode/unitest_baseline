"""
QUESTION:
Construct a function called `construct_dict` that takes three lists of equal length as input: `names`, `birth_dates`, and `birth_cities`. The function should return a dictionary where each key is a name from the `names` list and its corresponding value is a tuple or list of tuples containing the date of birth and city of birth. If there are duplicate names, the function should store all corresponding dates and cities without overwriting previous entries. If the input lists are not of equal length, the function should return an empty dictionary.
"""

def construct_dict(names, birth_dates, birth_cities):
    if len(names) != len(birth_dates) or len(names) != len(birth_cities):
        return {}
    individual_dict = {}
    for name, birth_date, birth_city in zip(names, birth_dates, birth_cities):
        if name in individual_dict:
            if type(individual_dict[name][0]) is list:
                individual_dict[name][0].append(birth_date)
                individual_dict[name][1].append(birth_city)
            else:
                individual_dict[name] = [[individual_dict[name][0], birth_date], [individual_dict[name][1], birth_city]]
        else:
            individual_dict[name] = [birth_date, birth_city]
    return individual_dict