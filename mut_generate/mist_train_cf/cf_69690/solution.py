"""
QUESTION:
Create a function `fertilizer_bags(nitrogen_level1, nitrogen_level2, target_nitrogen)` that determines the number of bags of each fertilizer type needed to reach a target nitrogen level in the soil. The function takes three parameters: the nitrogen levels of the two fertilizer types (`nitrogen_level1` and `nitrogen_level2`) and the target nitrogen level (`target_nitrogen`). The function should return the minimum number of bags of each type that adds up to the target nitrogen level, or a message if no such combination is found.
"""

def fertilizer_bags(nitrogen_level1, nitrogen_level2, target_nitrogen):
    """
    Determine the number of bags of each fertilizer type needed to reach a target nitrogen level in the soil.

    Args:
        nitrogen_level1 (int): Nitrogen level of the first fertilizer type.
        nitrogen_level2 (int): Nitrogen level of the second fertilizer type.
        target_nitrogen (int): Target nitrogen level.

    Returns:
        tuple or str: A tuple containing the minimum number of bags of each type, or a message if no combination is found.
    """
    for total_bags in range(target_nitrogen // min(nitrogen_level1, nitrogen_level2) + 1):
        for bags1 in range(total_bags + 1):
            bags2 = total_bags - bags1
            if nitrogen_level1 * bags1 + nitrogen_level2 * bags2 == target_nitrogen:
                return (bags1, bags2)
    return "No combination found"