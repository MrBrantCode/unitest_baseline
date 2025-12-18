"""
QUESTION:
Raju has a crush on girl of his class. He wanted to become close friend of her so he started trying to impress her. She came to know about raju and she also likes him but she is not ready to tell him about her feelings. She gave him a task,she will ask him a chocolate weighs x and raju has to get chocolate of exact weight from the series of chocolate stores which are present in the university. if he succeeds in it she will say "I Like You" else she will get anger and will tell "I Hate You". Raju came to know about his task and he don't want to loose his girl first impression so he wants a help from you to impress his crush.

NOTE: X weight should be one or only 2 different weights of other chocolates. 

SAMPLE INPUT
5
5 2 3 4 1
4
10
4
2
12

SAMPLE OUTPUT
I Hate You
I Like You
I Like You
I Hate You
"""

def can_impress_crush(chocolates, queries):
    chocolates.sort()
    results = []
    
    for w in queries:
        flag = 0
        if w in chocolates:
            flag = 1
        else:
            for j in range(len(chocolates) - 1):
                for k in range(j + 1, len(chocolates)):
                    if chocolates[j] + chocolates[k] == w:
                        flag = 1
                        break
                if flag == 1:
                    break
        
        if flag == 1:
            results.append("I Like You")
        else:
            results.append("I Hate You")
    
    return results