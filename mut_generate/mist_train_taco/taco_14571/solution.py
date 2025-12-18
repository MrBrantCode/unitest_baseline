"""
QUESTION:
You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck. 

$\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\$

Given a full name, your task is to capitalize the name appropriately.

Input Format

A single line of input containing the full name, $\mbox{S}$.

Constraints

$0<len(S)<1000$  
The string consists of alphanumeric characters and spaces.  

Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc. 

Output Format

Print the capitalized string, $\mbox{S}$.

Sample Input
chris alan

Sample Output
Chris Alan
"""

def capitalize_name(full_name: str) -> str:
    """
    Capitalizes the first letter of each word in the given full name.

    Parameters:
    full_name (str): The full name to be capitalized.

    Returns:
    str: The capitalized full name.
    """
    if not full_name:
        return full_name
    
    # Add a space at the beginning to handle the first word
    full_name = ' ' + full_name
    capitalized_name = ''
    
    for i in range(1, len(full_name)):
        if full_name[i - 1] == ' ' and full_name[i] != ' ':
            capitalized_name += full_name[i].upper()
        else:
            capitalized_name += full_name[i]
    
    return capitalized_name