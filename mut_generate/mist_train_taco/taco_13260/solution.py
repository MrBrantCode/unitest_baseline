"""
QUESTION:
An English booklet has been created for publicizing Aizu to the world. When you read it carefully, you found a misnomer (an error in writing) on the last name of Masayuki Hoshina, the lord of the Aizu domain. The booklet says "Hoshino" not "Hoshina".

Your task is to write a program which replace all the words "Hoshino" with "Hoshina". You can assume that the number of characters in a text is less than or equal to 1000.



Input

The input consists of several datasets. There will be the number of datasets n in the first line. There will be n lines. A line consisting of english texts will be given for each dataset.

Output

For each dataset, print the converted texts in a line.

Example

Input

3
Hoshino
Hashino
Masayuki Hoshino was the grandson of Ieyasu Tokugawa.


Output

Hoshina
Hashino
Masayuki Hoshina was the grandson of Ieyasu Tokugawa.
"""

def replace_hoshino_with_hoshina(texts):
    """
    Replaces all occurrences of "Hoshino" with "Hoshina" in each string of the input list.

    Parameters:
    texts (list of str): A list of strings where each string represents a dataset.

    Returns:
    list of str: A list of strings with "Hoshino" replaced by "Hoshina".
    """
    return [text.replace('Hoshino', 'Hoshina') for text in texts]