"""
QUESTION:
Samu had got N fruits. Sweetness of i^th fruit is given by A[i]. Now she wants to eat all the fruits , in such a way that total taste is maximised.

Total Taste is calculated as follow (Assume fruits sweetness array uses 1-based indexing) : 

int taste=0;
for(int i=2;i ≤ N;i++){
    if (A[i]-A[i-1] ≥ 0){
       taste = taste + i*(A[i]-A[i-1]);
    }
    else{
       taste = taste + i*(A[i-1]-A[i]);   
    }
}

So, obviously the order in which she eat the fruits changes the Total taste. She can eat the fruits in any order. Also once she start eating a fruit she will finish that one before moving to some other fruit.

Now she got confused in deciding the order in which she should eat them so that her Total taste is maximized. So she ask for help from you. Help her find the maximum taste she can have , if she can eat the fruits in any order.

Input Format :   First line contain number of test cases T. First line of each test case contains N, denoting the number of fruits. Next line contain N space separated integers denoting the sweetness of each fruit. 

Output Format :   For each test case you need to print the maximum taste Samu can have by eating the fruits in any order she want to.

Constraints :
1 ≤ T ≤ 10
1 ≤ N ≤ 15
Sweetness of each fruit, A[i] lies between 1 to 100 for 1 ≤ i ≤ N

SAMPLE INPUT
1
3
2 5 4

SAMPLE OUTPUT
13

Explanation

[2,4,5] -> 2*(2) + 3*(1) = 7
[2,5,4] -> 2*(3) + 3*(1) = 9
[5,4,2] -> 2*(1) + 3*(2) = 8
[5,2,4] -> 2*(3) + 3*(2) = 12
[4,5,2] -> 2*(1) + 3*(3) = 11
[4,2,5] -> 2*(2) + 3*(3) = 13

So maximum is 13 that can be obtained by eating the fruits according to sweetness order [4,2,5].
"""

def maximize_taste(sweetness_list):
    def taste(x, y, j):
        return j * abs(x - y)

    def greed(arr, j, N):
        max1 = 0
        op = []
        k = 0
        chk = [0] * N
        N1 = N
        sol = 0
        seed = arr[j]
        
        op.append(arr[j])
        chk[j] = 1
        flag = 0
        
        while N1 >= 2:
            flag = 0
            for i in range(N):
                if chk[i] != 1:
                    t = taste(seed, arr[i], N1)
                    if max1 < t:
                        max1 = t
                        k = i
                        flag = 1
            
            N1 -= 1
            chk[k] = 1
            seed = arr[k]
            op.append(arr[k])
            sol += max1
            max1 = 0
        
        return sol

    N = len(sweetness_list)
    solution = []
    for i in range(N):
        sol = greed(sweetness_list, i, N)
        solution.append(sol)
    
    return max(solution)