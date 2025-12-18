"""
QUESTION:
-----General Statement:-----
Given the actual high and low temperatures for the day and the normal high and low temperatures for that day, calculate the average difference from normal.

-----Input:-----
The first line of the data set for this problem is an integer that represents the number of data sets that follow. Each data set is on a separate line and consists of today’s high, today’s low, normal high, and normal low – in that order.

-----Output:-----
If the average difference is negative, do not output the negative sign (-).
Output the amount of deviation from normal, followed by the words
DEGREE(S) ABOVE NORMAL, or by the words
DEGREE(S) BELOW NORMAL.
Round to 1 decimal place. A trailing zero is required if the average is an integer.
The output is to be formatted exactly like that for the sample output given below.

-----Assumptions:-----
Temperatures are in the range –15..100 degrees.
The average temperature difference will not be zero.

-----Discussion:-----
Determine the average of the difference of the high temperatures and the difference of the low temperatures.

-----Sample Input:-----
3
75 45 78 40
50 32 45 30
56 48 62 45

-----Sample Output:-----
1.0 DEGREE(S) ABOVE NORMAL
3.5 DEGREE(S) ABOVE NORMAL
1.5 DEGREE(S) BELOW NORMAL
"""

def calculate_average_deviation(today_high, today_low, normal_high, normal_low):
    # Calculate the average temperatures
    today_avg = (today_high + today_low) / 2
    normal_avg = (normal_high + normal_low) / 2
    
    # Calculate the deviation
    deviation = today_avg - normal_avg
    
    # Determine the direction of the deviation
    if deviation > 0:
        deviation_direction = "ABOVE NORMAL"
    else:
        deviation_direction = "BELOW NORMAL"
        deviation = abs(deviation)  # Ensure deviation is positive for output
    
    # Round the deviation to 1 decimal place
    deviation = round(deviation, 1)
    
    return deviation, deviation_direction