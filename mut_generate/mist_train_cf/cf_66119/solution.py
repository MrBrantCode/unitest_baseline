"""
QUESTION:
Implement a `classify_species` function that takes a string of a scientific name of a wildlife species as input, split it into genus and species, and classify it into one of five categories: Mammalia, Aves, Reptilia, Amphibia, or Pisces. If the input does not match any known species, return 'Unknown'. The function should use a string-based classification system and handle exact species names with correct capitalization and spelling.
"""

def classify_species(species_name):
    # Define a list of animals for each classification
    mammalia = ['Felis catus', 'Canis lupus', 'Equus caballus']
    aves = ['Gallus gallus', 'Columba livia', 'Corvus brachyrhynchos']
    reptilia = ['Crocodylus niloticus', 'Varanus komodoensis', 'Chelonia mydas']
    amphibia = ['Xenopus laevis', 'Ambystoma mexicanum', 'Rana temporaria']
    pisces = ['Danio rerio', 'Carassius auratus', 'Gadus morhua']

    # Split the input into genus and species
    genus, species = species_name.split()

    # Determine the classification
    if species_name in mammalia:
        return 'Mammalia'
    elif species_name in aves:
        return 'Aves'
    elif species_name in reptilia:
        return 'Reptilia'
    elif species_name in amphibia:
        return 'Amphibia'
    elif species_name in pisces:
        return 'Pisces'
    else:
        return 'Unknown'