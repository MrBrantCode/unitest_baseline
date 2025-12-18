"""
QUESTION:
Write a function named `get_specific_date_file` that takes no arguments and returns a solution to filter files in Azure Data Factory data flow based on a specific date in the file name, with a file naming convention of "name_dateX.csv". The function should exclude any irrelevant files and only load the data of the specified date ("name_date1.csv") into the sink database.
"""

import glob

def get_specific_date_file(date_value):
    """
    This function filters files based on a specific date in the file name.
    
    Parameters:
    date_value (str): The specific date to be searched in the file name.
    
    Returns:
    list: A list of files with the specified date in their names.
    """
    
    # Assuming the files are in the same directory as the script
    # If not, specify the path to the directory
    files = glob.glob("name_date*.csv")
    
    # Filter the files based on the specified date
    specific_date_files = [file for file in files if f"date{date_value}" in file]
    
    return specific_date_files

# Example usage:
date_value = "1"
specific_date_files = get_specific_date_file(date_value)
print(specific_date_files)