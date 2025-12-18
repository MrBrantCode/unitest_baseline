"""
QUESTION:
Bob gives you a list of  N strings and a task to solve. The task is to remove all the duplicate strings from the list and print the resulting list of strings in a sorted order.

Input:
The first line contains  an integer N. Then next N lines contain a  string Si.

Output:
Print the sorted list.

Constraints:
1 ≤ |N| ≤ 5000
1 ≤ |Si| ≤ 100

SAMPLE INPUT
16
nandu 
kanth
kalyan
dhiraj
kanth
kalyan
baala
kt
baala
jayanth
sampu
baala
kanth
kalyan
baala
kt

SAMPLE OUTPUT
baala
dhiraj
jayanth
kalyan
kanth
kt
nandu
sampu
"""

def remove_duplicates_and_sort(strings):
    """
    Removes duplicates from the input list of strings and returns the sorted list.

    Parameters:
    strings (list of str): A list of strings.

    Returns:
    list of str: A sorted list of strings with duplicates removed.
    """
    unique_strings = set(strings)
    sorted_strings = sorted(unique_strings)
    return sorted_strings