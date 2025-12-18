"""
QUESTION:
Calculate the number of large and small trucks needed to transport a given tonnage of goods, assuming an equal number of large and small trucks must be used. The weights moved by the trucks are defined by the system of linear equations: 4a + 7b = 17 and 8a + 15b = 52, where 'a' represents the tonnage moved by a large truck, and 'b' represents the tonnage moved by a small truck. The function should take the desired tonnage as input and return the number of large and small trucks needed, or -1 if an equal number of large and small trucks cannot meet the required tonnage.
"""

def calculate_trucks(tonnage):
    # calculating a and b from the system of linear equations
    a = (17-7*(35-4*7)/8)/4
    b = (35-4*a)/8

    # verify if the tonnage can be achieved with equal number of large and small trucks
    num_trucks = tonnage / (a+b)
    
    if num_trucks.is_integer():
        return num_trucks
    else:
        return -1  # if it's not an integer, return -1