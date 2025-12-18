"""
QUESTION:
Alex has a board game consisting of:

A chip for marking his current location on the board.
$n$ fields numbered from $1$ to $n$. Each position $\boldsymbol{i}$ has a value, $f_i$, denoting the next position for the chip to jump to from that field.
A die with $m$ faces numbered from $\mbox{o}$ to $m-1$. Each face $j$ has a probability, $p_j$, of being rolled.

Alex then performs the following actions:

Begins the game by placing the chip at a position in a field randomly and with equiprobability. 
Takes $\boldsymbol{\mbox{k}}$ turns; during each turn he:
Rolls the die. We'll denote the number rolled during a turn as $\boldsymbol{d}$.
Jumps the chip $\boldsymbol{d}$ times. Recall that each field contains a value denoting the next field number to jump to.
After completing $\boldsymbol{\mbox{k}}$ turns, the game ends and he must calculate the respective probabilities for each field as to whether the game ended with the chip in that field.

Given $n$, $m$, $\boldsymbol{\mbox{k}}$, the game board, and the probabilities for each die face, print $n$ lines where each line $\boldsymbol{i}$ contains the probability that the chip is on field $\boldsymbol{i}$ at the end of the game.

Note: All the probabilities in this task are rational numbers modulo $M=998244353$. That is, if the probability can be expressed as the irreducible fraction $\frac{p}{q}$ where $q\ \text{mod}\ M\neq0$, then it corresponds to the number $(p\times q^{-1})\:\text{mod}\:M$ (or, alternatively, $p\times q^{-1}\equiv x(\:\text{mod}\:M)$). Click here to learn about Modular Multiplicative Inverse.

Input Format

The first line contains three space-separated integers describing the respective values of $n$ (the number of positions), $m$ (the number of die faces), and $\boldsymbol{\mbox{k}}$ (the number of turns). 

The second line contains $n$ space-separated integers describing the respective values of each $f_i$ (i.e., the index of the field that field $\boldsymbol{i}$ can transition to). 

The third line contains $m$ space-separated integers describing the respective values of each $p_j$ (where $0\leq p_j<M$) describing the probabilities of the faces of the $m$-sided die.  

Constraints

$1\leq n\leq6\times10^4$  
$4\leq m\leq10^5$  
$1\leq k\leq1000$  
$1\leq i,f_i\leq n$
$0\leq p_j<M$
The sum of $p_j\:\text{mod}\:M$ is $1$  

Note: The time limit for this challenge is doubled for all languages. Read more about standard time limits at our environment page.

Output Format

Print $n$ lines of output in which each line $\boldsymbol{i}$ contains a single integer, $x_i$ (where $0\leq x_i<M$), denoting the probability that the chip will be on field $\boldsymbol{i}$ after $\boldsymbol{\mbox{k}}$ turns.

Sample Input 0
4 5 1
2 3 2 4
332748118 332748118 332748118 0 0

Sample Output 0
582309206
332748118
332748118
748683265

Explanation 0

The diagram below depicts the respective probabilities of each die face being rolled:

The diagram below depicts each field with an arrow pointing to the next field:

There are four equiprobable initial fields, so each field has a $\frac{1}{4}$ probability of being the chip's initial location. Next, we calculate the probability that the chip will end up in each field after $k=1$ turn:

The only way the chip ends up in this field is if it never jumps from the field, which only happens if Alex rolls a $0$. So, this field's probability is $\frac{1}{4}\cdot\frac{1}{3}=\frac{1}{12}$. We then calculate and print the result of $\frac{1}{12}\ \text{mod}\ 998244353=582309206$ on a new line.

The chip can end up in field $2$ after one turn in the following scenarios:

Start in field $1$ and roll a $1$, the probability for which is $\frac{1}{4}\cdot\frac{1}{3}=\frac{1}{12}$.
Start in field $2$ and roll a $0$ or a $2$, the probability for which is $\frac{1}{4}\cdot\frac{2}{3}=\frac{2}{12}$.
Start in field $3$ and roll a $1$, the probability for which is $\frac{1}{4}\cdot\frac{1}{3}=\frac{1}{12}$.

After summing these probabilities, we get a total probability of $\frac1{12}+\frac2{12}+\frac1{12}=\frac13$ for the field. We then calculate and print the result of $\frac{1}{3}\ \text{mod}\ 998244353=332748118$ on a new line.

The chip can end up in field $3$ after one turn in the following scenarios:

Start in field $1$ and roll a $2$, the probability for which is $\frac{1}{4}\cdot\frac{1}{3}=\frac{1}{12}$.
Start in field $2$ and roll a $1$, the probability for which is $\frac{1}{4}\cdot\frac{1}{3}=\frac{1}{12}$.
Start in field $3$ and roll a $0$ or a $2$, the probability for which is $\frac{1}{4}\cdot\frac{2}{3}=\frac{2}{12}$.

After summing these probabilities, we get a total probability of $\frac1{12}+\frac1{12}+\frac2{12}=\frac13$ for the field. We then calculate and print the result of $\frac{1}{3}\ \text{mod}\ 998244353=332748118$ on a new line.

If the chip is initially placed in field $4$, it will always end up in field $4$ regardless of how many turns are taken (because this field loops back onto itself). Thus, this field's probability is $\frac{1}{4}$. We then calculate and print the result of $\frac{1}{4}\ \text{mod}\ 998244353=748683265$ on a new line.
"""

MOD = 998244353

def inv(v):
    return pow(v % MOD, MOD - 2, MOD) % MOD

class Node(object):
    def __init__(self, i, p0, rolls):
        self.child = None
        self.parents = []
        self.lastProb = p0
        self.currentProb = 0
        self.index = i

    def clear(self):
        (self.lastProb, self.currentProb) = (self.currentProb, 0)

    def update(self, diceProbs, depth=0, baseProb=None):
        if baseProb is None:
            baseProb = self.lastProb
        if baseProb == 0 or depth >= len(diceProbs):
            return
        self.currentProb += diceProbs[depth] * baseProb
        self.currentProb %= MOD
        self.child.update(diceProbs, depth + 1, baseProb)

def calculate_final_probabilities(n, m, k, next_positions, die_probabilities):
    p0 = inv(n)
    nodes = [Node(i, p0, k) for i in range(n)]
    for i, c in enumerate(next_positions):
        nodes[i].child = nodes[c]
        nodes[c].parents.append(nodes[i])
    for r in range(1, k + 1):
        for n in nodes:
            n.update(die_probabilities)
        for n in nodes:
            n.clear()
    return [n.lastProb for n in nodes]