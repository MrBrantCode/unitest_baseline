"""
QUESTION:
You are given a string representing an attendance record for a student. The record only contains the following three characters:



'A' : Absent. 
'L' : Late.
 'P' : Present. 




A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).    

You need to return whether the student could be rewarded according to his attendance record.

Example 1:

Input: "PPALLP"
Output: True



Example 2:

Input: "PPALLL"
Output: False
"""

def can_be_rewarded(attendance_record: str) -> bool:
    count_A = 0
    for i in range(len(attendance_record)):
        if attendance_record[i] == 'A':
            count_A += 1
            if count_A == 2:
                return False
        elif i >= 2 and attendance_record[i] == 'L' and attendance_record[i - 1] == 'L' and attendance_record[i - 2] == 'L':
            return False
    return True