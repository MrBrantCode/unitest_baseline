"""
QUESTION:
Write a function named `calculate_volume` that takes in four parameters: `mass` (in grams), `height` (in inches), `diameter` (in inches), and `density` (in pounds per cubic inch), and returns the volume of a cylinder in teaspoons. The density table contains the following substances: Sugar (0.875 lb/in^3), Water (1.000 g/mL), and Flour (0.593 lb/in^3). 1 teaspoon is equal to 0.0208333 cubic inches.
"""

def calculate_volume(mass, height, diameter, density):
    # Calculate the radius of the cylinder in inches
    radius = diameter / 2
    
    # Calculate the volume of the cylinder in cubic inches
    volume = (3.14159265359) * (radius ** 2) * height
    
    # Convert the mass to pounds if the density is in pounds per cubic inch
    if "lb" in str(density):
        mass = mass / 16
    
    # Calculate the volume in teaspoons
    volume_tsp = volume / 0.0208333
    
    # Calculate the mass of the substance in pounds
    mass_lb = mass / 453.592
    
    # Calculate the density in pounds per cubic inch
    if "lb" not in str(density):
        density = density * 0.0361273
    
    # Calculate the volume of the substance in cubic inches
    volume_substance = mass_lb / density
    
    # Calculate the volume of the substance in teaspoons
    volume_substance_tsp = volume_substance / 0.0208333
    
    # Calculate the total volume in teaspoons
    total_volume_tsp = volume_tsp + volume_substance_tsp
    
    return total_volume_tsp