"""
QUESTION:
Implement a function `parse_improper_dihedral(db, entry_name)` that takes the database `db` and the name of the improper dihedral entry `entry_name` as input. The function should return a tuple `(style, parameters)` containing the style of the improper dihedral potential and its numerical parameters. If the entry does not exist in the database, the function should return `None`. The `db` object has an `improper` attribute, which is a dictionary containing the improper dihedral entries. Each entry has `style` and `params` attributes, where `style` is a string representing the type of improper dihedral potential and `params` is a string of space-separated numerical values.
"""

def parse_improper_dihedral(db, entry_name):
    if entry_name in db.improper:
        style = db.improper[entry_name].style
        params = list(map(int, db.improper[entry_name].params.split()))
        return style, params
    else:
        return None