"""
QUESTION:
John is developing a system to report fuel usage but needs help with the coding.

First, he needs you to write a function that, given the actual consumption (in l/100 km) and remaining amount of petrol (in l), will give you how many kilometers you'll be able to drive.

Second, he needs you to write a function that, given a distance (in km), a consumption (in l/100 km), and an amount of petrol (in l), will return one of the following: If you can't make the distance without refueling, it should return the message "You will need to refuel". If you can make the distance, the function will check every 100 km and produce an array with [1:kilometers already driven. 2: kilometers till end. 3: remaining amount of petrol] and return all the arrays inside another array ([[after 100km], [after 200km], [after 300km]...])

PLEASE NOTE: any of the values with decimals that you return should be rounded to 2 decimals.
"""

def calculate_driving_range(consumption: float, petrol: float) -> float:
    """
    Calculate the total number of kilometers that can be driven with the given petrol and consumption.

    :param consumption: The actual consumption in liters per 100 km.
    :param petrol: The remaining amount of petrol in liters.
    :return: The total number of kilometers that can be driven, rounded to 2 decimal places.
    """
    return round(100 * petrol / consumption, 2)

def check_driving_progress(distance: float, consumption: float, petrol: float) -> [str, list]:
    """
    Check the driving progress and return the status or progress details.

    :param distance: The total distance to be driven in kilometers.
    :param consumption: The actual consumption in liters per 100 km.
    :param petrol: The remaining amount of petrol in liters.
    :return: If the distance cannot be covered without refueling, it returns "You will need to refuel".
             Otherwise, it returns a list of lists with progress details.
    """
    if distance > calculate_driving_range(consumption, petrol):
        return "You will need to refuel"
    else:
        return [
            [n * 100, distance - 100 * n, round(petrol - consumption * n, 2)]
            for n in range(int(distance // 100) + 1)
        ]