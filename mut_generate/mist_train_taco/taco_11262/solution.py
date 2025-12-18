"""
QUESTION:
On some day in January 2018, Takaki is writing a document. The document has a column where the current date is written in yyyy/mm/dd format. For example, January 23, 2018 should be written as 2018/01/23.
After finishing the document, she noticed that she had mistakenly wrote 2017 at the beginning of the date column. Write a program that, when the string that Takaki wrote in the date column, S, is given as input, modifies the first four characters in S to 2018 and prints it.

-----Constraints-----
 - S is a string of length 10.
 - The first eight characters in S are 2017/01/.
 - The last two characters in S are digits and represent an integer between 1 and 31 (inclusive).

-----Input-----
Input is given from Standard Input in the following format:
S

-----Output-----
Replace the first four characters in S with 2018 and print it.

-----Sample Input-----
2017/01/07

-----Sample Output-----
2018/01/07
"""

def update_date_to_2018(S: str) -> str:
    """
    Updates the date string from 2017 to 2018.

    Parameters:
    S (str): A string of length 10 representing the date in the format 'yyyy/mm/dd'.
             The first eight characters must be '2017/01/'.

    Returns:
    str: The updated date string with the first four characters replaced by '2018'.
    """
    return S.replace('2017', '2018')