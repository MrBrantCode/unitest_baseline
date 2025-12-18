"""
QUESTION:
A mischievous notice has arrived from the primitive slow-life organization "Akaruda". Akaruda is famous for mischief such as throwing a pie at the face of a VIP, but recently it has become more radical, such as using gunpowder to sprinkle rat fireworks at the reception venue. The notice is the following text.


--- Personal computer Takes human time. not good.
When the short and long hands of the clock meet, Akaruda justice is done.
Slow life great.


It's terrifying and I'm not sure, but it seems to mean that the mischief is carried out when the minute hand and the minute hand of the clock overlap.

To be wary of this mischief, create a program that inputs the time and outputs "alert" if the short hand and the long hand are close, "safe" if they are far, and "warning" otherwise. However, "close" means that the angle between the short hand and the long hand is 0 ° or more and less than 30 °, and "far" means that the angle is 90 ° or more and 180 ° or less. The time should be between 00:00 and 11:59.



Input

The input is given in the following format:


n
hh1: mm1
hh2: mm2
::
hhn: mmn


The number of times to be judged on the first line n (1 ≤ n ≤ 10000), and the i-th time hhi: mmi on the second and subsequent lines are given to each line.

Output

Output the judgment result of the i-th time safe, warning, or alert in order on one line.

Example

Input

4
02:15
06:01
11:55
10:40


Output

alert
safe
alert
warning
"""

def check_clock_hand_position(h: int, m: int) -> str:
    # Calculate the angle of the minute hand
    minute_angle = m * 6
    
    # Calculate the angle of the hour hand
    hour_angle = 30 * (h + m / 60)
    
    # Determine the smaller and larger angle
    if minute_angle < hour_angle:
        larger_angle, smaller_angle = hour_angle, minute_angle
    else:
        larger_angle, smaller_angle = minute_angle, hour_angle
    
    # Calculate the difference between the two angles
    if larger_angle - smaller_angle > 180:
        angle_difference = 360 - larger_angle + smaller_angle
    else:
        angle_difference = larger_angle - smaller_angle
    
    # Determine the status based on the angle difference
    if angle_difference < 30:
        return 'alert'
    elif angle_difference < 90:
        return 'warning'
    else:
        return 'safe'