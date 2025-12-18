"""
QUESTION:
Chef is fan of pairs and he likes all things that come in pairs. He even has a doll collection in which the dolls come in pairs. One day while going through his collection he found that there are odd number of dolls. Someone had stolen a doll!!!  
Help chef find which type of doll is missing..

------ Input ------ 

The first line contains an integer T, the number of test cases. 

The first line of each test case contains an integer N, the number of dolls. 

The next N lines are the types of dolls that are left.

------ Output ------ 

For each test case, display the type of doll that doesn't have a pair, in a new line.

------ Constraints ------ 

1≤T≤10 

1≤N≤100000 (10^{5}) 

0≤type≤100000 

----- Sample Input 1 ------ 
1
3
1 
2
1
----- Sample Output 1 ------ 
2
----- explanation 1 ------ 

----- Sample Input 2 ------ 
1
5
1
1
2
2
3
----- Sample Output 2 ------ 
3
----- explanation 2 ------
"""

def find_missing_doll_type(test_cases):
    results = []
    for dolls in test_cases:
        doll_count = {}
        for doll in dolls:
            if doll in doll_count:
                doll_count[doll] += 1
            else:
                doll_count[doll] = 1
        
        for doll, count in doll_count.items():
            if count % 2 == 1:
                results.append(doll)
                break
    return results