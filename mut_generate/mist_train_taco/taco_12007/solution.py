"""
QUESTION:
Joker is back again with his destructive plan . He has set N bombs in various parts of Gotham city and has challenged the police department  to defuse all bombs in one day . City can be treated as a 1-D line with 'N'   bombs situated in such a manner that distance of 1^st bomb is 'x'  , 2nd bomb is  ' x^2 '  , 3rd bomb is  ' x^3  ' ....... nth bomb is  ' x^n '  , where  ' x ' is measured from the start (left end ) . Since the number of bombs planted is very large ,  Gordon and his team find it impossible to diffuse all the bombs in one day and once again Gordon asks for Batman's help . He keeps his bomb diffusing squad ready at the start and requests batman to bring all the bombs back to  the start . Since the bombs are very heavy ,  batman can carry only one bomb at a time  .  For each bomb ,  he first travels upto the bomb location and then carry it back upto the start and thus covering the same distance ( bomb's distance from the start ) twice .  For example for  N=4  , total distance covered by batman is 
x  +  x  +  x^2 + x^2  +  x^3  + x^3  +  x^4  +  x^4 where  x is the distance of the first bomb in kms.
Now Batman is wondering how much distance he has to cover in order to bring all bombs back to the start but he is little  weak in calculations involving large numbers  and asks for your help to calculate the total distance he has to cover . Since the total distance can be very large , he wants you to calculate the total distance mod  M , i.e he wants  total_distance % M.

Input 
First line of input contains integer t , number of test cases. Each t lines contains contains 3 integers  N - number of bombs planted in the city ,  x - distance of first bomb and  M -  modulo .

Output 
Each line of output contains a single integer , the required answer.

 Constraints 
1 ≤ T ≤ 50
1 ≤ N,x ≤ 10^9
1< M ≤ 100000 (10^5)

SAMPLE INPUT
5
1 1 10
2 2 10
2 5 3
2 8 100
10 1 10

SAMPLE OUTPUT
2
2
0
44
0

Explanation

For the 4th test case , i.e  2 8 100 , 
batman has to travel distance = 8 + 8 + 64 + 64
                                            = 144 mod 100 = 44
"""

def calculate_total_distance_mod_m(N, x, M):
    def get_mod_pow(a, b, m):
        ans = 1
        while b > 0:
            if b % 2 == 1:
                ans = (ans * a) % m
            a = (a ** 2) % m
            b = b // 2
        return ans

    def find(n, x, m):
        if n == 0:
            return 0
        if n == 1:
            return x
        poly = find(n // 2, x, m)
        if n % 2 == 1:
            return (poly + (1 + poly) * get_mod_pow(x, (n + 1) // 2, m)) % m
        else:
            return (poly + poly * get_mod_pow(x, n // 2, m)) % m

    if M < 3:
        return 0
    elif x == 1:
        return (2 * N) % M
    else:
        return (2 * find(N, x, M)) % M