"""
QUESTION:
Given a time in $12$-hour AM/PM format, convert it to military (24-hour) time.  

Note: 
- 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock. 

- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.  

Example  

$\textbf{s}=\textbf{'12:01:00PM'}$   

Return '12:01:00'.

$\mathbf{s}=\text{'12:01:00AM'}$   

Return '00:01:00'.

Function Description  

Complete the timeConversion function in the editor below.  It should return a new string representing the input time in 24 hour format.  

timeConversion has the following parameter(s):

string s: a time in $12$ hour format  

Returns

string: the time in $24$ hour format

Input Format

A single string $\boldsymbol{\mathrm{~S~}}$ that represents a time in $12$-hour clock format (i.e.: $\textbf{hh:mm:ssAM}$ or $\textbf{hh:mm:ssPM}$).

Constraints

All input times are valid

Sample Input 0
07:05:45PM

Sample Output 0
19:05:45
"""

def time_conversion(s):
    is_pm = s[-2:].lower() == 'pm'
    time_list = list(map(int, s[:-2].split(':')))
    
    if is_pm and time_list[0] < 12:
        time_list[0] += 12
    if not is_pm and time_list[0] == 12:
        time_list[0] = 0
    
    return ':'.join(map(lambda x: str(x).rjust(2, '0'), time_list))