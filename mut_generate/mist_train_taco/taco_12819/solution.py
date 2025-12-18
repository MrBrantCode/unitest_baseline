"""
QUESTION:
Chef will not be able to attend the birthday of his best friend Rock. He promised Rock that this will not be the case on his half birthday. To keep his promise Chef must know Rock’s next half birthday accurately. Being busy, he is assigning this work to you.
Half birthday is the day that occurs exactly between two subsequent birthdays. 
You will be provided with Rock’s birthdate and birth month, you will have to figure out his half birthday.
$Note$: Consider every year to be a leap year and all months are displayed in lowercase English characters.

-----Input:-----
- The first line of the input contains a single integer $T$ denoting the number of test cases. 
- The description of each of the $T$ test cases contains an integer $d$ followed by a string, denoting month $m$.
- Here $d$ denotes day of a month and $m$ denotes the month of a year respectively.

-----Output:-----
For each test case print an integer $d1$ followed by a string, denoting month $m1$, which overall denotes date and month of Rock’s half birthday.

-----Constraints:-----
- $1 \leq T \leq 10^5$
- $1 \leq d , d1 \leq 31$
- $january \leq m , m1 \leq december$

-----Sample Input:-----
3
15 january
31 august
10 october

-----Sample Output:-----
16 july
1 march
10 april
"""

def calculate_half_birthday(birth_day: int, birth_month: str) -> tuple:
    # Dictionary mapping months to their number of days
    month_days = {
        'january': 31, 'february': 29, 'march': 31, 'april': 30, 
        'may': 31, 'june': 30, 'july': 31, 'august': 31, 
        'september': 30, 'october': 31, 'november': 30, 'december': 31
    }
    
    # List of months in order
    months = list(month_days.keys())
    
    # Find the index of the birth month
    birth_month_index = months.index(birth_month)
    
    # Calculate the remaining days from the birth day to the end of the birth month
    remaining_days = month_days[birth_month] - birth_day
    
    # Calculate the total days to add to reach the half birthday (183 days)
    days_to_add = 183 - remaining_days
    
    # Initialize the index for the half birthday month
    half_birth_month_index = birth_month_index
    
    # Loop to find the half birthday month and day
    while days_to_add > 0:
        if half_birth_month_index == 11:
            half_birth_month_index = 0
        else:
            half_birth_month_index += 1
        
        if days_to_add <= month_days[months[half_birth_month_index]]:
            half_birth_day = days_to_add
            break
        
        days_to_add -= month_days[months[half_birth_month_index]]
    
    # Return the half birthday day and month
    return half_birth_day, months[half_birth_month_index]