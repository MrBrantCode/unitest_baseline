"""
QUESTION:
Write a function `generate_html_table` that takes two inputs: an array of survey results in percentage format and the number of options in the survey. The function should calculate the average, median, and standard deviation of the survey results, and then return an HTML table displaying the results, including the average, median, and standard deviation. The deviation for each option is calculated as the difference between the option's percentage and the average percentage. The average is calculated by summing all the percentages and dividing by the number of options. The median is calculated as the middle value of the sorted survey results array. The standard deviation is calculated using the formula `sqrt(sum((percentage - average)^2) / (number of options - 1))`. The number of options should be greater than or equal to the number of elements in the survey results array.
"""

import math

def generate_html_table(results, options):
    """
    This function generates an HTML table displaying the survey results, 
    including the average, median, and standard deviation of the results.

    Args:
        results (list): A list of survey results in percentage format.
        options (list): A list of options in the survey.

    Returns:
        str: An HTML table displaying the results, including the average, median, and standard deviation.
    """

    # Calculate the average of the survey results
    average = sum(results) / len(results)

    # Calculate the median of the survey results
    sorted_results = sorted(results)
    if len(sorted_results) % 2 == 0:
        mid = len(sorted_results) // 2
        median = (sorted_results[mid] + sorted_results[mid - 1]) / 2
    else:
        median = sorted_results[len(sorted_results) // 2]

    # Calculate the standard deviation of the survey results
    deviation_sum = sum([(x - average) ** 2 for x in results])
    if len(results) > 1:
        standard_deviation = math.sqrt(deviation_sum / (len(results) - 1))
    else:
        standard_deviation = 0

    # Generate the HTML table
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