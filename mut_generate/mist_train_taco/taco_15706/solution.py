"""
QUESTION:
Pandaland is a place full of strings. One day Panda visited Pandaland and get confused wether Pandaland is a lucky place or not. According to Panda a place is lucky if all the strings in that place follows the following property 'P' : - 
P:A place is lucky if, for any string S, the prefix of S should not be present in that place. For example, if the string 'panda' is present in Pandaland, then for Pandaland to be lucky, strings like 'pan', 'pandaland', 'pandacakes', 'pand' etc should not be present in the Pandaland, but strings like 'da', 'nda' etc can be present. 

INPUT:
The first line contains an integer T denoting the number of test cases.
First line of each test case contains an integer  N denoting the number of strings present in Pandaland.
Next N lines contains N strings.

OUTPUT:
For each test case output "YES"(without quotes) if Pandaland is Lucky otherwise "NO"(without quotes).

CONSTRAINTS:
T ≤ 10
N ≤ 100
sizeofString ≤ 100    

SAMPLE INPUT
1
3
pan
panda
lucky

SAMPLE OUTPUT
NO
"""

class Node:
    def __init__(self, c):
        self.c = c
        self.next = {}
        self.cnt = 0
        self.ends = 0

def insert(node, word):
    for w in word:
        if w not in node.next:
            node.next[w] = Node(w)
        node = node.next[w]
        node.cnt += 1
    node.ends += 1

def traverse(node, path):
    global flag
    if len(path) > 0:
        if len(node.next) > 0 and node.ends != 0:
            flag = False
    for w in node.next:
        traverse(node.next[w], path + w)

def is_lucky_place(test_cases):
    results = []
    for case in test_cases:
        root = Node("$")
        flag = True
        for s in case:
            insert(root, s)
        traverse(root, "")
        if flag:
            results.append("YES")
        else:
            results.append("NO")
    return results