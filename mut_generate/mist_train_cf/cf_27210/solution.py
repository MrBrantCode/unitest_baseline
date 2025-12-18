"""
QUESTION:
Implement the `find_alternate_spellings` function to find all alternate spellings of a given name by recursively substituting units in groups of alternate spellings. The function takes five arguments: `name` (the input name), `ALT_GROUPS` (a list of groups of alternate spellings), `lower_names` (a list of lowercased valid names), and two optional parameters `checked` (a list to keep track of checked names) and `alts` (a list to store the found alternate spellings). If `checked` or `alts` is not provided, initialize them as empty lists. Return the list of all the alternate spellings found, including the input name and any recursive findings.
"""

import re

def find_alternate_spellings(name, ALT_GROUPS, lower_names, checked=None, alts=None):
    if checked is None:
        checked = []
    if alts is None:
        alts = []

    for group in ALT_GROUPS:
        for unit in group:
            sub = '(' + '|'.join([u for u in group if u != unit]) + ')'
            alt = re.sub(sub, unit, name, count=1)
            if (alt != name) and (alt in lower_names) and (alt not in checked) and (alt not in alts):
                alts.append(alt)

    checked.append(name)

    if len(alts) == 0:
        return checked
    else:
        for alt in alts:
            if alt not in checked:
                checked.extend(find_alternate_spellings(alt, ALT_GROUPS, lower_names, checked, alts))

    return checked