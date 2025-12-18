"""
QUESTION:
Design a function `determine_normalization_level` to help determine how far a database should be normalized. The function should consider factors such as data understanding, performance needs, current and future requirements, premature optimization, scalability, and data consistency and integrity. The function should return a recommended normalization level for the given database.
"""

def determine_normalization_level(data_understanding, performance_needs, current_requirements, future_requirements, premature_optimization, scalability, data_integrity):
    """
    Determine the recommended normalization level for a database based on various factors.

    Args:
    - data_understanding (int): Level of understanding of the data (1-5)
    - performance_needs (int): Level of performance needs (1-5)
    - current_requirements (int): Level of current requirements (1-5)
    - future_requirements (int): Level of future requirements (1-5)
    - premature_optimization (int): Level of premature optimization (1-5)
    - scalability (int): Level of scalability needs (1-5)
    - data_integrity (int): Level of data integrity needs (1-5)

    Returns:
    - int: Recommended normalization level (1-5)
    """

    # Calculate the total score based on the given factors
    total_score = data_understanding + performance_needs + current_requirements + future_requirements + premature_optimization + scalability + data_integrity

    # Determine the normalization level based on the total score
    if total_score <= 14:
        return 1  # Low normalization level
    elif 15 <= total_score <= 21:
        return 2  # Medium normalization level
    elif 22 <= total_score <= 28:
        return 3  # Medium-high normalization level
    else:
        return 4  # High normalization level