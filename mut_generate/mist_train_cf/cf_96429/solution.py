"""
QUESTION:
Write a function `generate_html_table` that takes two parameters: an array of survey results in percentage format and the number of options in the survey. The function should return an HTML table that displays the survey results, including the average, median, and standard deviation. The deviation is calculated as the difference between each option's percentage and the average percentage. The average, median, and standard deviation should be calculated according to the provided formulas. The number of options should be greater than or equal to the number of elements in the survey results array.
"""

import math

def generate_html_table(results, options):
    """
    Generates an HTML table displaying survey results, including average, median, and standard deviation.

    Parameters:
    results (list): An array of survey results in percentage format.
    options (list): The number of options in the survey.

    Returns:
    str: An HTML table displaying the survey results.
    """

    # Calculate average
    average = sum(results) / len(results)

    # Calculate median
    sorted_results = sorted(results)
    if len(sorted_results) % 2 == 0:
        mid = len(sorted_results) // 2
        median = (sorted_results[mid] + sorted_results[mid - 1]) / 2
    else:
        median = sorted_results[len(sorted_results) // 2]

    # Calculate standard deviation
    deviation_sum = sum([(x - average) ** 2 for x in results])
    standard_deviation = math.sqrt(deviation_sum / (len(results) - 1))

    # Generate HTML table
    table = "<table>\n"
    table += "<tr><th>Option</th><th>Percentage</th><th>Deviation</th></tr>\n"

    for i in range(len(results)):
        deviation = results[i] - average
        table += f"<tr><td>{options[i]}</td><td>{results[i]}%</td><td>{deviation}%</td></tr>\n"

    table += "</table>\n"

    table += f"Average: {average}%<br>\n"
    table += f"Median: {median}%<br>\n"
    table += f"Standard Deviation: {standard_deviation:.2f}%<br>\n"

    return table