"""
QUESTION:
Create a recursive function `create_population_dict` that takes two lists, `countries` and `population`, as input and returns a dictionary. The function should handle cases where `countries` contains duplicate values, negative or zero population values, floating-point population values, country names with special characters or non-alphabetic characters, and empty or whitespace-only country names. The function should exclude invalid countries and population values, round floating-point population values to the nearest integer, sort the valid countries based on their population in descending order (and alphabetically in case of ties), and return a dictionary with the sorted countries and their populations. The function should have a time complexity of O(nlogn) and a space complexity of O(n).
"""

def create_population_dict(countries, population):
    # Create a list to store the valid countries and their populations
    valid_countries = []
    
    # Remove duplicate countries and exclude invalid countries from the list
    for i in range(len(countries)):
        # Exclude invalid countries
        if not countries[i] or not countries[i].strip() or not countries[i].isalpha():
            continue
            
        # Exclude negative or zero populations
        if population[i] <= 0:
            continue
        
        # Round floating-point populations to the nearest integer
        population[i] = round(population[i])
        
        # Store valid countries and their populations in the list
        valid_countries.append((countries[i], population[i]))
    
    # Sort the list based on population in descending order, and then alphabetically in case of tie
    valid_countries.sort(key=lambda x: (-x[1], x[0]))
    
    # Add the sorted valid countries and their populations to the dictionary
    return dict(valid_countries)