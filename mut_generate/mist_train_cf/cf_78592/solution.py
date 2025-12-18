"""
QUESTION:
Classify the demand pattern based on Average Demand Interval (ADI) and squared coefficient of variation of demand sizes (CV²). Implement a function `classify_demand_pattern` that takes ADI and CV² as input and returns the corresponding demand pattern: 'Smooth', 'Intermittent', 'Erratic', or 'Lumpy'. The classification thresholds are ADI < 1.32 and CV² < 0.49 for 'Smooth', ADI >= 1.32 and CV² < 0.49 for 'Intermittent', ADI < 1.32 and CV² >= 0.49 for 'Erratic', and ADI >= 1.32 and CV² >= 0.49 for 'Lumpy'.
"""

def classify_demand_pattern(adi, cv_squared):
    """
    Classify the demand pattern based on Average Demand Interval (ADI) and squared coefficient of variation of demand sizes (CV²).

    Args:
        adi (float): Average Demand Interval.
        cv_squared (float): Squared coefficient of variation of demand sizes.

    Returns:
        str: The corresponding demand pattern: 'Smooth', 'Intermittent', 'Erratic', or 'Lumpy'.
    """

    if adi < 1.32 and cv_squared < 0.49:
        return 'Smooth'
    elif adi >= 1.32 and cv_squared < 0.49:
        return 'Intermittent'
    elif adi < 1.32 and cv_squared >= 0.49:
        return 'Erratic'
    else:
        return 'Lumpy'