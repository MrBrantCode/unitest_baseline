"""
QUESTION:
Implement a function `filterIcons(iconSet, iconsData)` that filters a list of icons based on given criteria. The `iconSet` is a dictionary containing an array of criteria objects, each consisting of a comparison operator, a type ("number", "percentile", or "percent"), and a threshold value. The `iconsData` is a list of dictionaries containing information about the icons. The function should return a filtered list of icons that satisfy all the given criteria.
"""

def filterIcons(iconSet, iconsData):
    def satisfy_criteria(icon, criteria):
        if criteria['type'] == 'number':
            value = icon['value']
        elif criteria['type'] == 'percentile':
            value = icon['percentile']
        elif criteria['type'] == 'percent':
            value = icon['percent']
        
        if criteria['criteria'] == '>=' and value < criteria['value']:
            return False
        elif criteria['criteria'] == '<' and value >= criteria['value']:
            return False
        elif criteria['criteria'] == '<=' and value > criteria['value']:
            return False
        return True

    return [icon for icon in iconsData if all(satisfy_criteria(icon, criteria) for criteria in iconSet['icons'])]