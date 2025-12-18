"""
QUESTION:
Brave Ponta and his best friend, Brave Gonta, have come to Luida's bar in search of friends to embark on an epic adventure. There are many warriors, monks and wizards in the tavern who are itching to go on an adventure.

Gonta, who is kind-hearted, cared for Ponta and said, "You can choose your friends first."

On the other hand, don't worry about Ponta and Gonta. "No, you can choose first."

We continued to give in to each other, and finally Luida proposed: "Then, I'll divide the n registrants here with this" party division machine "so that the total fighting power of each party is as even as possible."

The task given to you is to create a program that is built into the partying machine.

This program inputs n integers and outputs the minimum difference between the total value of the integers contained in A and the total value of the integers contained in B when they are divided into two groups A and B. Must be.

Thanks to this machine, Ponta and Gonta got along well and went on an epic adventure ...



Input

Multiple datasets are given as input. Each dataset is given in the following format:

n (number of registrants: integer)
a1 a2 ... an (combat power of each registrant: blank-separated integer)

n is 20 or less, and each registrant's combat power does not exceed 1 million.

When n is 0, it is the end of input.

Output

Print the minimum value on one line for each dataset.

Example

Input

5
1 2 3 4 5
4
2 3 5 7
0


Output

1
1
"""

def minimum_combat_power_difference(n, combat_powers):
    if n == 0:
        return 0
    
    total_sum = sum(combat_powers)
    doubled_powers = [power * 2 for power in combat_powers]
    possible_sums = [-total_sum]
    
    for power in doubled_powers:
        possible_sums.extend([i + power for i in possible_sums])
    
    return min(map(abs, possible_sums))