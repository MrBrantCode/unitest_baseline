"""
QUESTION:
Écrivez une fonction Python nommée `to_snake_case` qui prend en entrée une chaîne de caractères en camel case et la convertit en snake case, en remplaçant les caractères spéciaux tels que les points, les tirets et les espaces par des traits de soulignement. La fonction doit également convertir la chaîne en minuscules. La fonction sera utilisée pour convertir les noms de colonnes d'une DataFrame PySpark avant de l'écrire dans Hive.
"""

import re

def to_snake_case(name):
    # convert camel case to snake case
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    name = re.sub('([a-z0-9])([A-Z])', r'\1_\2', name)
    # replace special characters with underscore
    name = re.sub('[^\w\s]', '_', name)
    # replace whitespace with underscore
    name = re.sub('\s+', '_', name)
    # convert to lowercase
    name = name.lower()
    return name