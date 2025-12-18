"""
QUESTION:
Dima, Inna and Seryozha have gathered in a room. That's right, someone's got to go. To cheer Seryozha up and inspire him to have a walk, Inna decided to cook something. 

Dima and Seryozha have n fruits in the fridge. Each fruit has two parameters: the taste and the number of calories. Inna decided to make a fruit salad, so she wants to take some fruits from the fridge for it. Inna follows a certain principle as she chooses the fruits: the total taste to the total calories ratio of the chosen fruits must equal k. In other words, $\frac{\sum_{j = 1}^{m} a_{j}}{\sum_{j = 1}^{m} b_{j}} = k$ , where a_{j} is the taste of the j-th chosen fruit and b_{j} is its calories.

Inna hasn't chosen the fruits yet, she is thinking: what is the maximum taste of the chosen fruits if she strictly follows her principle? Help Inna solve this culinary problem — now the happiness of a young couple is in your hands!

Inna loves Dima very much so she wants to make the salad from at least one fruit.


-----Input-----

The first line of the input contains two integers n, k (1 ≤ n ≤ 100, 1 ≤ k ≤ 10). The second line of the input contains n integers a_1, a_2, ..., a_{n} (1 ≤ a_{i} ≤ 100) — the fruits' tastes. The third line of the input contains n integers b_1, b_2, ..., b_{n} (1 ≤ b_{i} ≤ 100) — the fruits' calories. Fruit number i has taste a_{i} and calories b_{i}.


-----Output-----

If there is no way Inna can choose the fruits for the salad, print in the single line number -1. Otherwise, print a single integer — the maximum possible sum of the taste values of the chosen fruits.


-----Examples-----
Input
3 2
10 8 1
2 7 1

Output
18

Input
5 3
4 4 4 4 4
2 2 2 2 2

Output
-1



-----Note-----

In the first test sample we can get the total taste of the fruits equal to 18 if we choose fruit number 1 and fruit number 2, then the total calories will equal 9. The condition $\frac{18}{9} = 2 = k$ fulfills, that's exactly what Inna wants.

In the second test sample we cannot choose the fruits so as to follow Inna's principle.
"""

def max_fruit_salad_taste(n, k, taste, cal):
    # Calculate the difference between taste and k times calories for each fruit
    w = [taste[i] - k * cal[i] for i in range(n)]
    
    # Initialize a list to store the maximum taste for each possible difference sum
    taste_per_diff = [-1] * 50000
    shift = 20000
    taste_per_diff[shift] = 0
    
    # Update the maximum taste for each possible difference sum
    for i in range(n):
        new_tpd = taste_per_diff[:]
        for j in range(0, 40000):
            if taste_per_diff[j] != -1:
                new_tpd[j + w[i]] = max(new_tpd[j + w[i]], taste_per_diff[j] + taste[i])
        taste_per_diff = new_tpd
    
    # If the maximum taste at the shift is 0, it means no valid combination was found
    if taste_per_diff[shift] == 0:
        return -1
    else:
        return taste_per_diff[shift]