"""
QUESTION:
Create a function `calculate_areas` that takes a list of radii as input and returns a list of corresponding circle areas calculated using the formula πr². 

The function should handle invalid input types and values. If a radius value is negative or non-numeric, it should print 'Invalid Input' and skip that value. If the input list is empty, it should return 'Empty List'. The function should accept both integer and floating-point values for radii.
"""

def calculate_areas(arr_radii):
    """
    Calculate the areas of circles given a list of radii.

    Args:
        arr_radii (list): A list of radii.

    Returns:
        list: A list of corresponding circle areas. If the input list is empty, returns 'Empty List'.
    """
    if len(arr_radii) == 0:
        return 'Empty List'
    areas = []
    for radius in arr_radii:
        if isinstance(radius, (int, float)):
            if radius >= 0:
                area = 3.14 * radius ** 2
                areas.append(area)
            else:
                print('Invalid Input')
        else:
            print('Invalid Input')
    return areas