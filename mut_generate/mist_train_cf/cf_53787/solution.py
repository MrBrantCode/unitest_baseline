"""
QUESTION:
Write a recursive function `printFib` that prints the sequence of Fibonacci numbers from the initial one up to 144, with each individual number printed on a separate line. The function should not take any arguments.
"""

def printFib(n = 0):
    def fibHelper(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibHelper(n - 1) + fibHelper(n - 2)

    fibNum = fibHelper(n)
    if fibNum <= 144:
        print(fibNum)
        printFib(n + 1)