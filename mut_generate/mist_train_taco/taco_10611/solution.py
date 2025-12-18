"""
QUESTION:
Curry making

As the ACM-ICPC domestic qualifying is approaching, you who wanted to put more effort into practice decided to participate in a competitive programming camp held at a friend's house. Participants decided to prepare their own meals.

On the first night of the training camp, the participants finished the day's practice and began preparing dinner. Not only in competitive programming, but also in self-catering, you are often said to be a "professional", and you have spared time because you have finished making the menu for your charge in a blink of an eye. Therefore, I decided to help other people make curry.

Now, there is a curry made by mixing R0 [g] roux with W0 [L] water. There is one type of roux used this time, and each roux is R [g]. Ru has a sufficient stockpile. When you use this roux, you think that the curry with a concentration of C [g / L] is the most delicious, so add some roux and water to this curry appropriately to make the concentration C [g / L]. I want to. Here, the concentration of curry in which roux R0 [g] is dissolved in water W0 [L] is R0 / W0 [g / L], and X roux of R [g] and water Y [L] are added to this curry. ] Is added, the concentration becomes (R0 + XR) / (W0 + Y) [g / L]. Although there are a lot of roux, you thought that it was not good to use too much, so you decided to make a curry with a concentration of C [g / L] by reducing the number of roux to be added as much as possible.

When making a curry with a concentration of C [g / L] by properly adding either roux, water, or both to a curry with a concentration of R0 / W0 [g / L], the number of roux X to be added Find the minimum value.

However, please note the following points regarding the curry making this time.

* Number of roux to be added The value of X must be an integer greater than or equal to 0. In other words, it is not possible to add only 1/3 of the roux.
* The value of the volume Y of water to be added can be a real number greater than or equal to 0, and does not have to be an integer.
* In some cases, it is possible to make curry with a concentration of C without adding either roux, water, or both.
* Since a sufficient amount of roux and water is secured, it is good that the situation that the curry with concentration C cannot be made due to lack of roux and water does not occur.



Input

The input consists of multiple datasets. Each dataset consists of one line and is expressed in the following format.

> R0 W0 C R

Here, R0, W0, C, and R are the mass of roux already dissolved in the curry that is being made [g], the volume of water contained in the curry [L], and the concentration of the curry you want to make [g / L]. , Represents the mass [g] per roux. All of these values ​​are integers between 1 and 100. The end of the input is indicated by a line of four zeros separated by blanks.

Output

For each dataset, one line is the minimum number of roux that needs to be added to make a curry with a concentration of C from a fake curry that is a mixture of W0 [L] water and R0 [g] roux. To output. Do not output the amount of water to add.

Note that due to input constraints, the minimum number of roux that is the answer for each dataset is guaranteed to be within the range represented by a 32-bit signed integer.

Sample Input


10 5 3 4
2 5 2 3
91 13 7 62
10 1 3 5
20 100 2 20
2 14 7 1
0 0 0 0

Output for Sample Input


2
3
0
0
9
96






Example

Input

10 5 3 4
2 5 2 3
91 13 7 62
10 1 3 5
20 100 2 20
2 14 7 1
0 0 0 0


Output

2
3
0
0
9
96
"""

def calculate_minimum_roux(R0, W0, C, R):
    # Calculate the current concentration
    current_concentration = R0 / W0
    
    # If the current concentration is already greater than or equal to C, no roux is needed
    if current_concentration >= C:
        return 0
    
    # Calculate the minimum number of roux needed
    for i in range(100000):
        new_concentration = (R0 + i * R) / W0
        if new_concentration >= C:
            return i
    
    # If no solution is found within the range, return -1 (though the problem guarantees a solution)
    return -1