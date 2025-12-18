"""
QUESTION:
The cat Snuke wants to play a popular Japanese game called ÅtCoder, so Iroha has decided to teach him Japanese.
When counting pencils in Japanese, the counter word "本" follows the number. The pronunciation of this word varies depending on the number. Specifically, the pronunciation of "本" in the phrase "N 本" for a positive integer N not exceeding 999 is as follows:
 - hon when the digit in the one's place of N is 2, 4, 5, 7, or 9;
 - pon when the digit in the one's place of N is 0, 1, 6 or 8;
 - bon when the digit in the one's place of N is 3.
Given N, print the pronunciation of "本" in the phrase "N 本".

-----Constraints-----
 - N is a positive integer not exceeding 999.

-----Input-----
Input is given from Standard Input in the following format:
N

-----Output-----
Print the answer.

-----Sample Input-----
16

-----Sample Output-----
pon

The digit in the one's place of 16 is 6, so the "本" in "16 本" is pronounced pon.
"""

def pronounce_counter_word(N: int) -> str:
    # Ensure N is within the valid range
    if N < 1 or N > 999:
        raise ValueError("N must be a positive integer not exceeding 999")
    
    # Get the last digit of N
    last_digit = N % 10
    
    # Determine the pronunciation based on the last digit
    if last_digit in [0, 1, 6, 8]:
        return 'pon'
    elif last_digit == 3:
        return 'bon'
    else:
        return 'hon'