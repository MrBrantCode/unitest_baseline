"""
QUESTION:
Create a function `fruit_characteristics` that takes a list of fruit names and a dictionary of their characteristics as input, where each characteristic dictionary includes 'color', 'taste', 'size', 'origin', and 'seeds'. If the fruit's origin is 'imported', the dictionary should also include 'country_of_origin'. The function should return a dictionary where the keys are the fruit names and the values are their corresponding characteristic dictionaries. The function should also print the fruit names in alphabetical order along with their characteristics. 

Note: The input list of fruit names and the dictionary of characteristics will be provided. The function should not take any additional inputs.
"""

def fruit_characteristics(fruits, characteristics):
    """
    This function takes a list of fruit names and a dictionary of their characteristics.
    It returns a dictionary where the keys are the fruit names and the values are their corresponding characteristic dictionaries.
    It also prints the fruit names in alphabetical order along with their characteristics.

    Parameters:
    fruits (list): A list of fruit names.
    characteristics (dict): A dictionary of fruit characteristics.

    Returns:
    dict: A dictionary where the keys are the fruit names and the values are their corresponding characteristic dictionaries.
    """
    
    # Initialize an empty dictionary to store the fruit characteristics
    fruit_characteristics_dict = {}

    # Iterate over the sorted list of fruits
    for fruit in sorted(fruits):
        # Add the fruit characteristics to the dictionary
        fruit_characteristics_dict[fruit] = characteristics[fruit]
        
        # Print the fruit name and its characteristics
        print(fruit + ":")
        print("Color:", characteristics[fruit]["color"])
        print("Taste:", characteristics[fruit]["taste"])
        print("Size:", characteristics[fruit]["size"])
        print("Origin:", characteristics[fruit]["origin"])
        
        # Check if the fruit's origin is 'imported' and print the country of origin if it is
        if characteristics[fruit]["origin"] == "imported":
            print("Country of Origin:", characteristics[fruit]["country_of_origin"])
        
        print("Seeds:", characteristics[fruit]["seeds"])
        print()

    # Return the dictionary of fruit characteristics
    return fruit_characteristics_dict