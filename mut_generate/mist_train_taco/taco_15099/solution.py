"""
QUESTION:
This is an interactive problem. Refer to the Interaction section below for better understanding.

Ithea and Chtholly want to play a game in order to determine who can use the kitchen tonight.

<image>

Initially, Ithea puts n clear sheets of paper in a line. They are numbered from 1 to n from left to right.

This game will go on for m rounds. In each round, Ithea will give Chtholly an integer between 1 and c, and Chtholly needs to choose one of the sheets to write down this number (if there is already a number before, she will erase the original one and replace it with the new one).

Chtholly wins if, at any time, all the sheets are filled with a number and the n numbers are in non-decreasing order looking from left to right from sheet 1 to sheet n, and if after m rounds she still doesn't win, she loses the game.

Chtholly really wants to win the game as she wants to cook something for Willem. But she doesn't know how to win the game. So Chtholly finds you, and your task is to write a program to receive numbers that Ithea gives Chtholly and help her make the decision on which sheet of paper write this number.

Input

The first line contains 3 integers n, m and c (<image>, <image> means <image> rounded up) — the number of sheets, the number of rounds and the largest possible number Ithea can give to Chtholly respectively. The remaining parts of input are given throughout the interaction process.

Interaction

In each round, your program needs to read one line containing a single integer pi (1 ≤ pi ≤ c), indicating the number given to Chtholly.

Your program should then output a line containing an integer between 1 and n, indicating the number of sheet to write down this number in.

After outputting each line, don't forget to flush the output. For example: 

  * fflush(stdout) in C/C++; 
  * System.out.flush() in Java; 
  * sys.stdout.flush() in Python; 
  * flush(output) in Pascal; 
  * See the documentation for other languages. 



If Chtholly wins at the end of a round, no more input will become available and your program should terminate normally. It can be shown that under the constraints, it's always possible for Chtholly to win the game.

Example

Input

2 4 4
2
1
3


Output

1
2
2

Note

In the example, Chtholly initially knew there were 2 sheets, 4 rounds and each number was between 1 and 4. She then received a 2 and decided to write it in the 1st sheet. Then she received a 1 and wrote it in the 2nd sheet. At last, she received a 3 and replaced 1 with 3 in the 2nd sheet. At this time all the sheets were filled with a number and they were non-decreasing, so she won the game. 

Note that it is required that your program terminate immediately after Chtholly wins and do not read numbers from the input for the remaining rounds. If not, undefined behaviour may arise and it won't be sure whether your program will be accepted or rejected. Also because of this, please be careful when hacking others' codes. In the sample, Chtholly won the game after the 3rd round, so it is required that your program doesn't read the number of the remaining 4th round.

The input format for hacking: 

  * The first line contains 3 integers n, m and c; 
  * The following m lines each contains an integer between 1 and c, indicating the number given to Chtholly in each round.
"""

def determine_winning_sheet(n, m, c, numbers):
    a = [0] * (n + 1)  # Initialize the sheets with 0s
    cnt = 0  # Counter to track how many sheets are filled
    result = []  # List to store the results of each round
    
    for x in numbers:
        i = 0
        if x * 2 <= c:
            i = 1
            while a[i] and a[i] <= x:
                i += 1
        else:
            i = n
            while a[i] and a[i] >= x:
                i -= 1
        
        if a[i] == 0:
            cnt += 1
        a[i] = x
        result.append(i)
        
        # Check if Chtholly wins
        if cnt == n and all(a[j] <= a[j + 1] for j in range(1, n)):
            return result
    
    return result