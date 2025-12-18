"""
QUESTION:
Tattah is asleep if and only if Tattah is attending a lecture. This is a well-known formula among Tattah's colleagues.

On a Wednesday afternoon, Tattah was attending Professor HH's lecture. At 12:21, right before falling asleep, he was staring at the digital watch around Saher's wrist. He noticed that the digits on the clock were the same when read from both directions i.e. a palindrome.

In his sleep, he started dreaming about such rare moments of the day when the time displayed on a digital clock is a palindrome. As soon as he woke up, he felt destined to write a program that finds the next such moment.

However, he still hasn't mastered the skill of programming while sleeping, so your task is to help him.

Input

The first and only line of the input starts with a string with the format "HH:MM" where "HH" is from "00" to "23" and "MM" is from "00" to "59". Both "HH" and "MM" have exactly two digits.

Output

Print the palindromic time of day that comes soonest after the time given in the input. If the input time is palindromic, output the soonest palindromic time after the input time.

Examples

Input

12:21


Output

13:31


Input

23:59


Output

00:00
"""

def find_next_palindromic_time(current_time: str) -> str:
    def is_palindromic(h: str, m: str) -> bool:
        if len(h) == 1:
            h = '0' + h
        if len(m) == 1:
            m = '0' + m
        return h[0] == m[1] and h[1] == m[0]

    h, m = current_time.split(':')
    
    while True:
        if int(m) + 1 == 60:
            h = str((int(h) + 1) % 24)
            m = '00'
        else:
            m = str(int(m) + 1).zfill(2)
        
        if is_palindromic(h, m):
            return f"{h.zfill(2)}:{m}"