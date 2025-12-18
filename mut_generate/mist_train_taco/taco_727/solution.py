"""
QUESTION:
Akaki, a patissier, can make N kinds of doughnut using only a certain powder called "Okashi no Moto" (literally "material of pastry", simply called Moto below) as ingredient. These doughnuts are called Doughnut 1, Doughnut 2, ..., Doughnut N. In order to make one Doughnut i (1 ≤ i ≤ N), she needs to consume m_i grams of Moto. She cannot make a non-integer number of doughnuts, such as 0.5 doughnuts.
Now, she has X grams of Moto. She decides to make as many doughnuts as possible for a party tonight. However, since the tastes of the guests differ, she will obey the following condition:
 - For each of the N kinds of doughnuts, make at least one doughnut of that kind.
At most how many doughnuts can be made here? She does not necessarily need to consume all of her Moto. Also, under the constraints of this problem, it is always possible to obey the condition.

-----Constraints-----
 - 2 ≤ N ≤ 100
 - 1 ≤ m_i ≤ 1000
 - m_1 + m_2 + ... + m_N ≤ X ≤ 10^5
 - All values in input are integers.

-----Input-----
Input is given from Standard Input in the following format:
N X
m_1
m_2
:
m_N

-----Output-----
Print the maximum number of doughnuts that can be made under the condition.

-----Sample Input-----
3 1000
120
100
140

-----Sample Output-----
9

She has 1000 grams of Moto and can make three kinds of doughnuts. If she makes one doughnut for each of the three kinds, she consumes 120 + 100 + 140 = 360 grams of Moto. From the 640 grams of Moto that remains here, she can make additional six Doughnuts 2. This is how she can made a total of nine doughnuts, which is the maximum.
"""

def max_doughnuts(N, X, m):
    # Calculate the total grams of Moto required to make at least one of each kind of doughnut
    total_minimum_moto = sum(m)
    
    # Find the minimum grams of Moto required to make one doughnut of any kind
    min_moto = min(m)
    
    # Calculate the remaining grams of Moto after making at least one of each kind
    remaining_moto = X - total_minimum_moto
    
    # Calculate the additional number of doughnuts that can be made with the remaining Moto
    additional_doughnuts = remaining_moto // min_moto
    
    # The total number of doughnuts is the initial N (one of each kind) plus the additional doughnuts
    return N + additional_doughnuts