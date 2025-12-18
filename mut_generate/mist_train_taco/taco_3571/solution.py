"""
QUESTION:
Given the time in numerals we may convert it into words, as shown below:

5:00→ five o' clock

5:01→ one minute past five

5:10→ ten minutes past five

5:30→ half past five

5:40→ twenty minutes to six

5:45→ quarter to six

5:47→ thirteen minutes to six

5:28→ twenty eight minutes past five

Write a program which prints the time in words for the input given in the format mentioned above.

Input Format

There will be two lines of input:

H, representing the hours

M, representing the minutes

Constraints

1≤H≤12

0≤M<60

Output Format

Display the time in words.

SAMPLE INPUT
5  
47

SAMPLE OUTPUT
thirteen minutes to six
"""

def convert_time_to_words(H, M):
    words = {
        1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
        11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
        18: "eighteen", 19: "nineteen", 20: "twenty", 21: "twenty one", 22: "twenty two", 23: "twenty three",
        24: "twenty four", 25: "twenty five", 26: "twenty six", 27: "twenty seven", 28: "twenty eight", 29: "twenty nine"
    }
    
    if M == 0:
        return f"{words[H]} o' clock"
    elif M == 30:
        return f"half past {words[H]}"
    elif M < 30:
        if M == 1:
            return f"one minute past {words[H]}"
        elif M == 15:
            return f"quarter past {words[H]}"
        else:
            return f"{words[M]} minutes past {words[H]}"
    else:
        M = 60 - M
        H = H + 1 if H < 12 else 1
        if M == 1:
            return f"one minute to {words[H]}"
        elif M == 15:
            return f"quarter to {words[H]}"
        else:
            return f"{words[M]} minutes to {words[H]}"