"""
QUESTION:
Food contains three nutrients called "protein", "fat" and "carbohydrate", which are called three major nutrients. It is calculated that protein and carbohydrate are 4 kcal (kilocalories) and fat is 9 kcal per 1 g (gram). For example, according to the table below, the number 1 cake contains 7 g of protein, 14 g of fat and 47 g of carbohydrates. If you calculate the calories contained based on this, it will be 4 x 7 + 9 x 14 + 4 x 47 = 342 kcal. Others are calculated in the same way.

Number | Name | Protein (g) | Lipids (g) | Carbohydrates (g) | Calories (kcal)
--- | --- | --- | --- | --- | ---
1 | Cake | 7 | 14 | 47 | 342
2 | Potato Chips | 5 | 35 | 55 | 555
3 | Dorayaki | 6 | 3 | 59 | 287
4 | Pudding | 6 | 5 | 15 | 129



Input the number of sweets to be classified n, the information of each sweet, and the limit information, and output a list of sweets that do not exceed the limit (may be eaten) if only one sweet is used. Create a program.

The candy information consists of the candy number s, the weight p of the protein contained in the candy, the weight q of the lipid, and the weight r of the carbohydrate. The limit information consists of the maximum protein weight P that can be included, the fat weight Q, the carbohydrate weight R, and the maximum calorie C that can be consumed, of protein, fat, carbohydrate, and calories. If any one of them is exceeded, the restriction will be violated and it will be judged as "sweets that should not be eaten".

For a list of sweets that you can eat, output the numbers of sweets that you can eat in the order in which you entered them. If there are no sweets you can eat, please output "NA". For the four sweets in the table above, if the limit is P = 10, Q = 15, R = 50, C = 400, cake and pudding may be eaten as their respective nutrients and calories are below the limit. Although it is classified as sweets, potato chips are classified as sweets that should not be eaten because the amount of carbohydrates exceeds the limit value.



input

Given a sequence of multiple datasets. The end of the input is indicated by a single line of zeros. Each dataset is given in the following format:


n
s1 p1 q1 r1
s2 p2 q2 r2
::
sn pn qn rn
P Q R C


The first line gives the number of sweets n (1 ≤ n ≤ 1000). The next n lines are given the number si (1 ≤ si ≤ 1000) of the i-th candy and the integers pi, qi, ri (0 ≤ pi, qi, ri ≤ 100) representing the weight of each nutrient.

The following lines are given the integers P, Q, R (0 ≤ P, Q, R ≤ 100), C (0 ≤ C ≤ 1700) representing the limits for each nutrient and calorie.

The number of datasets does not exceed 100.

output

For each dataset, it outputs the number of sweets you can eat or "NA".

Example

Input

4
1 7 14 47
2 5 35 55
3 6 3 59
4 6 5 15
10 15 50 400
2
1 8 10 78
2 4 18 33
10 10 50 300
0


Output

1
4
NA
"""

def filter_edible_sweets(sweets_info, limits):
    (P, Q, R, C) = limits
    edible_sweets = []
    
    for (s, p, q, r) in sweets_info:
        if p <= P and q <= Q and r <= R and (4 * p + 9 * q + 4 * r <= C):
            edible_sweets.append(s)
    
    return edible_sweets