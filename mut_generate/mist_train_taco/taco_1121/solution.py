"""
QUESTION:
problem

AOR Ika is studying to pass the test.

AOR Ika-chan solved the $ N $ question. After that, round the solved problem according to the following procedure.

1. Check the correctness of the answer.
2. If the answer is correct, write a circle mark, and if it is incorrect, write a cross mark on the answer sheet.



AOR Ika faints because of the fear of failing the test the moment she finds that the answer is wrong for $ 2 $ in a row. And no further rounding is possible.

Syncope occurs between steps $ 1 $ and $ 2 $.

You will be given an integer $ N $, which represents the number of questions AOR Ika has solved, and a string $ S $, which is a length $ N $ and represents the correctness of the answer. The string consists of'o'and'x', with'o' indicating the correct answer and'x' indicating the incorrect answer. The $ i $ letter indicates the correctness of the $ i $ question, and AOR Ika-chan rounds the $ 1 $ question in order.

Please output the number of questions that AOR Ika-chan can write the correctness.



output

Output the number of questions that AOR Ika-chan could write in the $ 1 $ line. Also, output a line break at the end.

Example

Input

3
oxx


Output

2
"""

def count_correctness_before_syncope(N: int, S: str) -> int:
    try:
        # Find the index of the first occurrence of 'xx'
        syncope_index = S.index('xx')
        # Return the number of questions before syncope occurs
        return syncope_index
    except ValueError:
        # If no 'xx' is found, AOR Ika-chan can write the correctness for all questions
        return N