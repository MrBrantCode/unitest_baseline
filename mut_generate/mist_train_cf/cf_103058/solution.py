"""
QUESTION:
Create a function named `calculate_bulk_density` that takes mass in grams and volume in cubic centimeters as parameters and returns the bulk density in milligrams per milliliter (mg/mL). The function should not consider the polyhedron's faces and edges information.
"""

def calculate_bulk_density(mass_in_grams, volume_in_cubic_cm):
    """
    Calculate the bulk density in milligrams per milliliter (mg/mL).
    
    Parameters:
    mass_in_grams (float): The mass in grams.
    volume_in_cubic_cm (float): The volume in cubic centimeters.
    
    Returns:
    float: The bulk density in milligrams per milliliter (mg/mL).
    """
    # Convert grams to milligrams and cubic centimeters to milliliters
    mass_in_milligrams = mass_in_grams * 1000
    volume_in_milliliters = volume_in_cubic_cm
    
    # Calculate bulk density
    bulk_density = mass_in_milligrams / volume_in_milliliters
    
    return bulk_density