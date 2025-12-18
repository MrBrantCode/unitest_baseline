"""
QUESTION:
Create a function `create_y0` that takes in `params` and `species` as inputs. Using the given indices in `params.phytoindex` and `params.pocindex`, create a list `y0` where the spool and rpool values for phytoplankton species and the dissolved values for particulate organic carbon species are appended in the correct order. The function should return the populated `y0` list.
"""

def create_y0(params, species):
    """
    Creates a list y0 containing the spool and rpool values for phytoplankton species 
    and the dissolved values for particulate organic carbon species.

    Args:
        params (object): An object containing phytoindex and pocindex attributes.
        species (list): A list of species objects with get_spool, get_rpool, and get_dissolved methods.

    Returns:
        list: A list of pool values for the specified species.
    """

    y0 = []

    # Append spool and rpool for phytoplankton species
    for i in params.phytoindex:
        y0.append(species[i].get_spool())
        y0.append(species[i].get_rpool())

    # Append dissolved pool for particulate organic carbon species
    for i in params.pocindex:
        y0.append(species[i].get_dissolved())

    return y0