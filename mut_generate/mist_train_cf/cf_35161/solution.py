"""
QUESTION:
Implement the function `validateTradeCloseIndication` which takes a string `indication` and a float `openUnits` as parameters. The `indication` is either "ALL" or a decimal number representing the number of units of the open trade to close. The function should return `True` if the `indication` is valid and `False` otherwise. The `indication` is valid if it is "ALL" or if it is a positive decimal number not exceeding the magnitude of `openUnits`.
"""

def validateTradeCloseIndication(indication: str, openUnits: float) -> bool:
    if indication == "ALL":
        return True
    try:
        units_to_close = float(indication)
        if units_to_close > 0 and abs(units_to_close) <= abs(openUnits):
            return True
    except ValueError:
        pass
    return False