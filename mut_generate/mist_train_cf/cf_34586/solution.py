"""
QUESTION:
Create a function `calculate_fine` that takes the driver's velocity as input and returns a string based on the following rules:
- If the driver's velocity is less than or equal to the speed limit (80 km/h), return "Boa Tarde, cuidado na estrada, siga viagem!"
- If the driver's velocity exceeds the speed limit, calculate the fine using the formula: (velocity - speed limit) * fine rate (7 reais per km/h over the speed limit), and return the fine amount with a precision of 2 decimal places in the format: "Você ultrapassou o limite de velocidade e foi multado em {fine_amount} reais!"
"""

def calculate_fine(velocity):
    """
    Calculate the fine for a driver based on their velocity.

    Args:
        velocity (float): The driver's velocity in km/h.

    Returns:
        str: A message indicating whether the driver is within the speed limit or the amount of the fine.
    """
    speed_limit = 80
    fine_rate = 7

    if velocity <= speed_limit:
        return "Boa Tarde, cuidado na estrada, siga viagem!"
    else:
        fine_amount = (velocity - speed_limit) * fine_rate
        return f"Você ultrapassou o limite de velocidade e foi multado em {fine_amount:.2f} reais!"