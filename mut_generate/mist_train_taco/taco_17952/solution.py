"""
QUESTION:
Darth Vader, the lord of the dark side has created a Death-Star (it can destroy any star). You have to deactivate the Death-star. To deactivate the death-star one must find the unique most powerful Lightsaber.  Lightsaber’s power is associated with a number. You ask for Lightsaber from your friendly Jedis(person).  You should choose the Lightsaber which has the unique power as well as it is  powerful enough.

Input::: 
First line of input contains N,denoting the number of Lightsabers. Next  line contains N  space separated numbers denoting the power(Ai) of each Lightsaber.

Output :::
Print power of the unique most powerful Lightsaber.If there is no such lightsaber present  then print -1. 

Constraints:::
1 ≤ N ≤ 10^6,
0 ≤ Ai ≤ 10^9.

SAMPLE INPUT
5
9 8 8 9 5

SAMPLE OUTPUT
5
"""

def find_unique_most_powerful_lightsaber(N, powers):
    # Dictionary to count occurrences of each power
    power_count = {}
    
    # Count the occurrences of each power
    for power in powers:
        if power in power_count:
            power_count[power] += 1
        else:
            power_count[power] = 1
    
    # List to store unique powers
    unique_powers = []
    
    # Collect powers that occur exactly once
    for power in power_count:
        if power_count[power] == 1:
            unique_powers.append(power)
    
    # If no unique powers, return -1
    if not unique_powers:
        return -1
    
    # Return the maximum of the unique powers
    return max(unique_powers)