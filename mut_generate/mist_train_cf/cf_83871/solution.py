"""
QUESTION:
Construct a function named `create_html_table` that takes a 2D list of student scores as input where each sublist contains a subject and a score. The function should return an HTML table string representing the 2D list and include an additional row at the end with the average score. The input 2D list should have at least one sublist. The function should not take any other inputs.
"""

import pandas as pd

def create_html_table(studentScores):
    """
    This function takes a 2D list of student scores as input where each sublist contains a subject and a score.
    It returns an HTML table string representing the 2D list and includes an additional row at the end with the average score.

    Args:
        studentScores (list): A 2D list of student scores.

    Returns:
        str: An HTML table string.
    """
    # Create a dataframe
    df = pd.DataFrame(studentScores, columns=["Subject", "Scores"])

    # Compute average score
    average_score = df['Scores'].mean()

    # Add a new row for average score
    df = df._append({'Subject' : 'Average','Scores' : average_score}, ignore_index=True)

    # Convert dataframe to HTML
    html_table = df.to_html(index=False)
    
    return html_table