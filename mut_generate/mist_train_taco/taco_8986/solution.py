"""
QUESTION:
Vasya is choosing a laptop. The shop has n laptops to all tastes.

Vasya is interested in the following properties: processor speed, ram and hdd. Vasya is a programmer and not a gamer which is why he is not interested in all other properties.

If all three properties of a laptop are strictly less than those properties of some other laptop, then the first laptop is considered outdated by Vasya. Among all laptops Vasya does not consider outdated, he chooses the cheapest one.

There are very many laptops, which is why Vasya decided to write a program that chooses the suitable laptop. However, Vasya doesn't have his own laptop yet and he asks you to help him.

Input

The first line contains number n (1 ≤ n ≤ 100).

Then follow n lines. Each describes a laptop as speed ram hdd cost. Besides, 

  * speed, ram, hdd and cost are integers 
  * 1000 ≤ speed ≤ 4200 is the processor's speed in megahertz 
  * 256 ≤ ram ≤ 4096 the RAM volume in megabytes 
  * 1 ≤ hdd ≤ 500 is the HDD in gigabytes 
  * 100 ≤ cost ≤ 1000 is price in tugriks 



All laptops have different prices.

Output

Print a single number — the number of a laptop Vasya will choose. The laptops are numbered with positive integers from 1 to n in the order in which they are given in the input data.

Examples

Input

5
2100 512 150 200
2000 2048 240 350
2300 1024 200 320
2500 2048 80 300
2000 512 180 150


Output

4

Note

In the third sample Vasya considers the first and fifth laptops outdated as all of their properties cannot match those of the third laptop. The fourth one is the cheapest among the laptops that are left. Thus, Vasya chooses the fourth laptop.
"""

def choose_laptop(n, laptops):
    # List to store valid (non-outdated) laptops
    valid_laptops = []
    
    # Iterate over each laptop
    for i in range(n):
        current_laptop = laptops[i]
        is_outdated = False
        
        # Check if the current laptop is outdated by any other laptop
        for j in range(n):
            if i != j:
                other_laptop = laptops[j]
                if (current_laptop[0] < other_laptop[0] and
                    current_laptop[1] < other_laptop[1] and
                    current_laptop[2] < other_laptop[2]):
                    is_outdated = True
                    break
        
        # If the laptop is not outdated, add it to the valid list
        if not is_outdated:
            valid_laptops.append(current_laptop)
    
    # Sort the valid laptops by cost (the 4th element in the list)
    valid_laptops.sort(key=lambda x: x[3])
    
    # Find the index of the cheapest valid laptop in the original list
    chosen_laptop = valid_laptops[0]
    chosen_index = laptops.index(chosen_laptop) + 1
    
    return chosen_index