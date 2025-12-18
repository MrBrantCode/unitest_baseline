"""
QUESTION:
Everyone knows that computers become faster and faster. Recently Berland scientists have built a machine that can move itself back in time!

More specifically, it works as follows. It has an infinite grid and a robot which stands on one of the cells. Each cell of the grid can either be empty or contain 0 or 1. The machine also has a program which consists of instructions, which are being handled one by one. Each instruction is represented by exactly one symbol (letter or digit) and takes exactly one unit of time (say, second) to be performed, except the last type of operation (it's described below). Here they are:

  * 0 or 1: the robot places this number into the cell he is currently at. If this cell wasn't empty before the operation, its previous number is replaced anyway. 
  * e: the robot erases the number into the cell he is at. 
  * l, r, u or d: the robot goes one cell to the left/right/up/down. 
  * s: the robot stays where he is for a unit of time. 
  * t: let x be 0, if the cell with the robot is empty, otherwise let x be one more than the digit in this cell (that is, x = 1 if the digit in this cell is 0, and x = 2 if the digit is 1). Then the machine travels x seconds back in time. Note that this doesn't change the instructions order, but it changes the position of the robot and the numbers in the grid as they were x units of time ago. You can consider this instruction to be equivalent to a Ctrl-Z pressed x times. 



For example, let the board be completely empty, and the program be sr1t0. Let the robot initially be at (0, 0).

  * [now is the moment 0, the command is s]: we do nothing. 
  * [now is the moment 1, the command is r]: we are now at (1, 0). 
  * [now is the moment 2, the command is 1]: we are at (1, 0), and this cell contains 1. 
  * [now is the moment 3, the command is t]: we travel 1 + 1 = 2 moments back, that is, to the moment 1. 
  * [now is the moment 1, the command is 0]: we are again at (0, 0), and the board is clear again, but after we follow this instruction, this cell has 0 in it. We've just rewritten the history. The consequences of the third instruction have never happened. 



Now Berland scientists want to use their machine in practice. For example, they want to be able to add two integers.

Assume that the initial state of the machine is as follows:

  * One positive integer is written in binary on the grid in such a way that its right bit is at the cell (0, 1), from left to right from the highest bit to the lowest bit. 
  * The other positive integer is written in binary on the grid in such a way that its right bit is at the cell (0, 0), from left to right from the highest bit to the lowest bit. 
  * All the other cells are empty. 
  * The robot is at (0, 0). 
  * We consider this state to be always in the past; that is, if you manage to travel to any negative moment, the board was always as described above, and the robot was at (0, 0) for eternity. 



You are asked to write a program after which

  * The robot stands on a non-empty cell, 
  * If we read the number starting from the cell with the robot and moving to the right until the first empty cell, this will be a + b in binary, from the highest bit to the lowest bit. 



Note that there are no restrictions on other cells. In particular, there may be a digit just to the left to the robot after all instructions.

In each test you are given up to 1000 pairs (a, b), and your program must work for all these pairs. Also since the machine's memory is not very big, your program must consist of no more than 10^5 instructions.

Input

The first line contains the only integer t (1≤ t≤ 1000) standing for the number of testcases. Each of the next t lines consists of two positive integers a and b (1≤ a, b < 2^{30}) in decimal.

Output

Output the only line consisting of no more than 10^5 symbols from 01eslrudt standing for your program.

Note that formally you may output different programs for different tests.

Example

Input

2
123456789 987654321
555555555 555555555


Output

0l1l1l0l0l0l1l1l1l0l1l0l1l1l0l0l0l1l0l1l1l1l0l0l0l1l0l0l0l0l1l0lr
"""

def generate_program_for_addition(t, test_cases):
    def C(x, y):
        return x + '10' + y + 't' + y

    def CBF(x, y):
        return x + '01' + y + 't' + y

    Cr = C('r', 'l')
    Cl = C('l', 'r')
    Cu = C('u', 'd')
    Cd = C('d', 'u')
    CBFr = CBF('r', 'l')
    CBFl = CBF('l', 'r')
    CBFu = CBF('u', 'd')
    CBFd = CBF('d', 'u')

    def CE(x, y):
        return x + x + '0' + x + '1' + y + y + '10' + y + 't' + x + x + 't' + y + x + x + 'e' + x + 'e' + y + y + y

    def MNE(x, y):
        return CE(x, y) + x + C(y, x) + 'e' + y

    def MNEall(n):
        return (MNE('d', 'u') + 'l') * n + 'r' * n + 'u' + (MNE('u', 'd') + 'l') * n + 'r' * n + 'd'

    def ADD():
        return 'u' + Cu + 'u' + Cu + 'dd' + Cu + 'u' + Cu + 'u' + Cl + '010ltut' + Cd + 'dd'

    def ADDc():
        return ADD() + '0ulrtd' + ADD() + 'lltr'

    def ADDbit():
        return 'u' + Cu + 'u' + Cl + 'll0l1rrr' + ADDc() + 'dd' + Cu + 'u' + Cu + 'u' + Cl + ADDc() + 'dd'

    def full(n):
        return MNEall(n) + 'uuu' + '0l' * (n + 1) + 'r' * (n + 1) + 'ddd' + (ADDbit() + 'l') * n + 'uuu'

    # Determine the maximum number of bits needed for any test case
    max_bits = max(max(len(bin(a)[2:]), len(bin(b)[2:])) for a, b in test_cases)

    # Generate the program for the maximum number of bits
    program = full(max_bits)

    return program