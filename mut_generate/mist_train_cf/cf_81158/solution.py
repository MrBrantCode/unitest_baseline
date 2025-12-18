"""
QUESTION:
Develop a program that generates an array of strings containing the names of relatives, their relationship, and year of birth. The program should be able to sort the array in increasing order by birth year and provide the ability to find a relative by either name or relationship. The program should handle incorrect or unexpected input effectively. 

The program should include the following functions: 
- a function to add a relative's information 
- a function to sort relatives by birth year 
- a function to find relatives by name 
- a function to find relatives by relationship 
- a function to handle unexpected input
"""

def entrance(name, relationship, birth_year):
    return {
        'name': name,
        'relationship': relationship,
        'birth_year': birth_year
    }