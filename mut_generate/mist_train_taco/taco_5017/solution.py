"""
QUESTION:
Vasiliy spent his vacation in a sanatorium, came back and found that he completely forgot details of his vacation! 

Every day there was a breakfast, a dinner and a supper in a dining room of the sanatorium (of course, in this order). The only thing that Vasiliy has now is a card from the dining room contaning notes how many times he had a breakfast, a dinner and a supper (thus, the card contains three integers). Vasiliy could sometimes have missed some meal, for example, he could have had a breakfast and a supper, but a dinner, or, probably, at some days he haven't been at the dining room at all.

Vasiliy doesn't remember what was the time of the day when he arrived to sanatorium (before breakfast, before dinner, before supper or after supper), and the time when he left it (before breakfast, before dinner, before supper or after supper). So he considers any of these options. After Vasiliy arrived to the sanatorium, he was there all the time until he left. Please note, that it's possible that Vasiliy left the sanatorium on the same day he arrived.

According to the notes in the card, help Vasiliy determine the minimum number of meals in the dining room that he could have missed. We shouldn't count as missed meals on the arrival day before Vasiliy's arrival and meals on the departure day after he left.


-----Input-----

The only line contains three integers b, d and s (0 ≤ b, d, s ≤ 10^18,  b + d + s ≥ 1) — the number of breakfasts, dinners and suppers which Vasiliy had during his vacation in the sanatorium. 


-----Output-----

Print single integer — the minimum possible number of meals which Vasiliy could have missed during his vacation. 


-----Examples-----
Input
3 2 1

Output
1


Input
1 0 0

Output
0


Input
1 1 1

Output
0


Input
1000000000000000000 0 1000000000000000000

Output
999999999999999999





-----Note-----

In the first sample, Vasiliy could have missed one supper, for example, in case he have arrived before breakfast, have been in the sanatorium for two days (including the day of arrival) and then have left after breakfast on the third day. 

In the second sample, Vasiliy could have arrived before breakfast, have had it, and immediately have left the sanatorium, not missing any meal.

In the third sample, Vasiliy could have been in the sanatorium for one day, not missing any meal.
"""

def calculate_minimum_missed_meals(b, d, s):
    # Initialize the answer to a large number
    ans = 10 ** 22
    
    # Iterate over possible start and finish times
    for st in range(4):
        for fin in range(4):
            # Create a copy of the meal counts
            new_l = [b, d, s]
            
            # Adjust the meal counts based on the start time
            if st < 3:
                for i in range(st + 1):
                    new_l[i] += 1
            
            # Adjust the meal counts based on the finish time
            if fin < 3:
                for i in range(fin + 1):
                    new_l[i] -= 1
            
            # Calculate the current number of missed meals
            cur_ans = 0
            max_meals = max(new_l)
            for i in range(3):
                cur_ans += abs(max_meals - new_l[i])
            
            # Update the minimum number of missed meals
            ans = min(ans, cur_ans)
    
    return ans