"""
QUESTION:
---

# Story

The Pied Piper has been enlisted to play his magical tune and coax all the rats out of town.

But some of the rats are deaf and are going the wrong way!

# Kata Task

How many deaf rats are there?

# Legend

* ```P``` = The Pied Piper
* ```O~``` = Rat going left
* ```~O``` = Rat going right

# Example

* ex1 ```~O~O~O~O P``` has 0 deaf rats


* ex2 ```P O~ O~ ~O O~``` has 1 deaf rat


* ex3 ```~O~O~O~OP~O~OO~``` has 2 deaf rats

---

# Series

* [The deaf rats of Hamelin (2D)](https://www.codewars.com/kata/the-deaf-rats-of-hamelin-2d)
"""

def count_deaf_rats(town):
    # Remove all spaces from the input string
    town = town.replace(' ', '')
    
    # Find the position of the Pied Piper
    piper_index = town.index('P')
    
    # Initialize the count of deaf rats
    deaf_rats_count = 0
    
    # Iterate over the rats to the left of the Pied Piper
    for i in range(0, piper_index, 2):
        if town[i:i+2] == 'O~':
            deaf_rats_count += 1
    
    # Iterate over the rats to the right of the Pied Piper
    for i in range(piper_index + 1, len(town), 2):
        if town[i:i+2] == '~O':
            deaf_rats_count += 1
    
    return deaf_rats_count