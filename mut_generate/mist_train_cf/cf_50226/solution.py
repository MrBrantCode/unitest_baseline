"""
QUESTION:
We are conducting a study with 20 participants, each tested over 3 sessions with 3 types of food. The goal is to compare the effect of the 3 food types on hunger levels, a non-normal dependent variable. We need to choose between the Friedman test and the Kruskal-Wallis test to analyze the data, taking into account the repeated measures design and the non-normal distribution of the data. 

The function should determine which non-parametric test is most suitable for the given data and experimental design.
"""

def choose_test(experimental_design, data_distribution):
    """
    Determine the most suitable non-parametric test for the given data and experimental design.

    Parameters:
    experimental_design (str): The type of experimental design. Can be 'between-subjects' or 'within-subjects'.
    data_distribution (str): The distribution of the data. Can be 'normal' or 'non-normal'.

    Returns:
    str: The most suitable non-parametric test.
    """
    if experimental_design == 'within-subjects' and data_distribution == 'non-normal':
        return 'Friedman test'
    elif experimental_design == 'between-subjects' and data_distribution == 'non-normal':
        return 'Kruskal-Wallis test'
    else:
        return 'Unknown'