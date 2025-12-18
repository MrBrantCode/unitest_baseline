"""
QUESTION:
Write a function named `validate_z_test` that determines whether a two-proportion z-test is valid for a given set of poll results. The function should take the number of male and female students and the number of male and female students objecting to the dress code as parameters. The function should return True if the two-proportion z-test is valid and False otherwise.

Restrictions: The two-proportion z-test is invalid if the number of successes or failures in either group is less than 10.
"""

def validate_z_test(male_total, female_total, male_objecting, female_objecting):
    """
    Determine whether a two-proportion z-test is valid for a given set of poll results.

    Parameters:
    male_total (int): The total number of male students.
    female_total (int): The total number of female students.
    male_objecting (int): The number of male students objecting to the dress code.
    female_objecting (int): The number of female students objecting to the dress code.

    Returns:
    bool: True if the two-proportion z-test is valid, False otherwise.
    """
    male_proportion = male_objecting / male_total if male_total > 0 else 0
    female_proportion = female_objecting / female_total if female_total > 0 else 0

    male_successes = male_total * male_proportion
    male_failures = male_total * (1 - male_proportion)
    female_successes = female_total * female_proportion
    female_failures = female_total * (1 - female_proportion)

    return (male_successes >= 10 and male_failures >= 10 and 
            female_successes >= 10 and female_failures >= 10)