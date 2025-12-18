"""
QUESTION:
Create a function called `retrieve_gdp_population` to extract 'GDP' and 'population' values from a given dictionary. The dictionary may contain nested dictionaries and may have unlabeled or missing information. The function should return the extracted 'GDP' and 'population' values, or an error message if either value is missing.
"""

def retrieve_gdp_population(data):
    try:
        population = data['details']['population']
        gdp = data['details']['GDP']
        return population, gdp
    except KeyError as e:
        return f'Missing information: {e}'