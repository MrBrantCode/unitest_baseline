"""
QUESTION:
Write a function named 'calculate_allele_percentage' that calculates the percentage of specific alleles in a population or within a specific group. The function should take three parameters: the number of a specific allele (either CC, CT, or TT), the total number of alleles in the population or group, and a flag indicating whether to calculate the percentage for the entire population or within a specific group.
"""

def calculate_allele_percentage(specific_allele_count, total_alleles, within_group=False):
    """
    Calculate the percentage of specific alleles in a population or within a specific group.

    Parameters:
    specific_allele_count (int): The number of a specific allele (either CC, CT, or TT).
    total_alleles (int): The total number of alleles in the population or group.
    within_group (bool): A flag indicating whether to calculate the percentage for the entire population (False) or within a specific group (True).

    Returns:
    float: The percentage of specific alleles.
    """
    if within_group:
        # Calculate total alleles within the specific group if necessary
        # This part is not implemented as it depends on the actual data structure and logic
        pass
    
    # Calculate the percentage of specific alleles
    percentage = (specific_allele_count / total_alleles) * 100
    
    return percentage