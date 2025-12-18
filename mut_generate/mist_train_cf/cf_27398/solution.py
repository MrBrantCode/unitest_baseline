"""
QUESTION:
Write a function `extract_file_info(file_list)` that takes a list of file names as input and returns a dictionary containing the name extracted from each file name as the key and the count of files with that name as the value. The file names follow a specific pattern: they start with a name, followed by a space, then a date in the format "YYYY-MM-DD", and finally end with the file extension ".xlsx" or ".xls". The function should handle different file names and extensions correctly and be case-sensitive.
"""

def extract_file_info(file_list):
    file_info = {}
    for file_name in file_list:
        name = file_name.split(" ")[0].split("-")[0].split(".")[0]
        if name in file_info:
            file_info[name] += 1
        else:
            file_info[name] = 1
    return file_info