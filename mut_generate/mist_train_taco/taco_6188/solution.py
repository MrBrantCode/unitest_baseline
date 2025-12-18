"""
QUESTION:
Vasya wants to turn on Christmas lights consisting of m bulbs. Initially, all bulbs are turned off. There are n buttons, each of them is connected to some set of bulbs. Vasya can press any of these buttons. When the button is pressed, it turns on all the bulbs it's connected to. Can Vasya light up all the bulbs?

If Vasya presses the button such that some bulbs connected to it are already turned on, they do not change their state, i.e. remain turned on.


-----Input-----

The first line of the input contains integers n and m (1 ≤ n, m ≤ 100) — the number of buttons and the number of bulbs respectively. 

Each of the next n lines contains x_{i} (0 ≤ x_{i} ≤ m) — the number of bulbs that are turned on by the i-th button, and then x_{i} numbers y_{ij} (1 ≤ y_{ij} ≤ m) — the numbers of these bulbs.


-----Output-----

If it's possible to turn on all m bulbs print "YES", otherwise print "NO".


-----Examples-----
Input
3 4
2 1 4
3 1 3 1
1 2

Output
YES

Input
3 3
1 1
1 2
1 1

Output
NO



-----Note-----

In the first sample you can press each button once and turn on all the bulbs. In the 2 sample it is impossible to turn on the 3-rd lamp.
"""

def can_light_all_bulbs(n, m, buttons):
    # Initialize a set to keep track of all bulbs that can be turned on
    turned_on_bulbs = set()
    
    # Iterate over each button and add the bulbs it controls to the set
    for button in buttons:
        bulb_count = button[0]
        for k in range(1, bulb_count + 1):
            turned_on_bulbs.add(button[k])
    
    # Create a set of all bulb numbers from 1 to m
    all_bulbs = set(range(1, m + 1))
    
    # Check if the set of turned on bulbs covers all bulbs
    if turned_on_bulbs == all_bulbs:
        return "YES"
    else:
        return "NO"