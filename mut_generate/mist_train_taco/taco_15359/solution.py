"""
QUESTION:
Everyone who is involved with HackerEarth in what so ever form knows who Little Kuldeep is. He's not so little, but he's called that. (No one knows why!) He's pretty efficient at organizing, mentoring, managing various hiring challenges, contests happening on HackerEarth all the time. But age has caught up with him, finally. He's turned into little, old Kuldeep from little Kuldeep.

Earlier, he could've handled multiple contests like a piece of cake, but it is not possible for him now. In the present scenario, he needs other people to moderate contests, because he's busy moderating some other contest which is happening at the same time. 

Given the timings of the contests happening, can you check and tell little, old Kuldeep if he would need a moderator to help him out, or not?

Input format:
The input starts with a number, t, denoting the number of contests in a single day. On the next n lines, the time at which a contest starts and finishes is given. 

Output format:
For every case, you need to print a single line stating "Will need a moderator!" if contests are clashing, or "Who needs a moderator?" if the events are NOT clashing.

Constraints:
1 ≤ N ≤ 100
Time will be given in HoursHours:MinutesMinutes format.  (HH:MM)
The end time will (Surely!) be after the start time.

Example Input:
2
09:30-11:00
11:00-12:00  

Example Output:
Who needs a moderator?  

SAMPLE INPUT
2
11:00-13:30
13:00-13:45

SAMPLE OUTPUT
Will need a moderator!
"""

def check_contest_overlap(contests):
    art = [0] * 1440  # Initialize a list to track time slots in minutes
    for contest in contests:
        start_time, end_time = contest
        ah, am = start_time.split(':')
        bh, bm = end_time.split(':')
        final1 = int(ah) * 60 + int(am)
        final2 = int(bh) * 60 + int(bm)
        
        for minute in range(final1, final2):
            if art[minute] == 1:
                return "Will need a moderator!"
            art[minute] = 1
    
    return "Who needs a moderator?"