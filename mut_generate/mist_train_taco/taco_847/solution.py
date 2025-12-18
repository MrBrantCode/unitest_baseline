"""
QUESTION:
Три брата договорились о встрече. Пронумеруем братьев следующим образом: пусть старший брат имеет номер 1, средний брат имеет номер 2, а младший брат — номер 3. 

Когда пришло время встречи, один из братьев опоздал. По заданным номерам двух братьев, которые пришли вовремя, вам предстоит определить номер опоздавшего брата.


-----Входные данные-----

В первой строке входных данных следуют два различных целых числа a и b (1 ≤ a, b ≤ 3, a ≠ b) — номера братьев, которые пришли на встречу вовремя. Номера даны в произвольном порядке.


-----Выходные данные-----

Выведите единственное целое число — номер брата, который опоздал на встречу.


-----Пример-----
Входные данные
3 1

Выходные данные
2
"""

def find_late_brother(a: int, b: int) -> int:
    """
    Determines the number of the brother who was late based on the numbers of the brothers who arrived on time.

    Parameters:
    a (int): The number of the first brother who arrived on time.
    b (int): The number of the second brother who arrived on time.

    Returns:
    int: The number of the brother who was late.
    """
    return 6 - (a + b)