"""
QUESTION:
Create a function `calculate_total_stars(input_str)` that takes an input string consisting of multiple lines, each containing information about a GitHub repository in the format `<repository_name><tab><stars_range>`. The function should process the input and return a dictionary with the total number of stars for each repository, where the total number of stars is the sum of all numbers in the range specified by `<stars_range>`. The function should handle empty lines and invalid input.
"""

def calculate_total_stars(input_str):
    """
    This function takes an input string consisting of multiple lines, 
    each containing information about a GitHub repository in the format 
    <repository_name><tab><stars_range>. It processes the input and returns 
    a dictionary with the total number of stars for each repository.

    Args:
        input_str (str): A string containing repository information.

    Returns:
        dict: A dictionary with repository names as keys and total stars as values.
    """

    repo_stars = {}
    lines = input_str.split('\n')
    for line in lines:
        if line.strip() != '':
            repo, stars_range = line.split('\t')
            start, end = map(int, stars_range.split('-'))
            total_stars = sum(range(start, end + 1))
            repo_stars[repo] = total_stars
    return repo_stars