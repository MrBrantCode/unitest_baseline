"""
QUESTION:
Problem

In 1333, the greatest scientist in human history, Dr. Ushishi, developed an artificial intelligence with an ID of ai1333 in order to pass on his wisdom to posterity. For the next 100 years, ai1333 brought great benefits to humankind, but on the 100th anniversary of its birth, it created a new artificial intelligence with ID ai13333 as its successor and stopped its function permanently. did. Every 100 years since then, artificial intelligence has left a successor with an ID that concatenates '3' at the end of its own ID starting with'ai1333'.

Since the number of years elapsed from 1333 of the cow calendar is given as input, output the ID of the artificial intelligence created in that year. However, $ x $ is guaranteed to be a non-negative integer multiple of 100.

Ouput

Outputs the ID of the artificial intelligence created after $ x $ years from 1333 in the cow calendar on one line.

Constraints

The input satisfies the following conditions.

* $ 0 \ le x \ le 10000 $
* $ x $ is a non-negative integer multiple of 100

Input

The input is given in the following format.


$ x $


Age $ x $ is given on one line.

Examples

Input

0


Output

ai1333


Input

300


Output

ai1333333
"""

def generate_ai_id(years: int) -> str:
    """
    Generates the ID of the artificial intelligence created after a given number of years from 1333.

    Parameters:
    - years (int): The number of years elapsed from 1333, which is a non-negative integer multiple of 100.

    Returns:
    - str: The ID of the artificial intelligence created after the given number of years.
    """
    if years < 0 or years % 100 != 0:
        raise ValueError("Years must be a non-negative integer multiple of 100.")
    
    n = years // 100
    
    def recursive_id(n):
        if n == 0:
            return 'ai1333'
        else:
            return recursive_id(n - 1) + '3'
    
    return recursive_id(n)