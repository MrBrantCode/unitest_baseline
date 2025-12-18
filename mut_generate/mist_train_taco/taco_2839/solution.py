"""
QUESTION:
There are several (or no) spiders, butterflies, and dragonflies. 

In this kata, a spider has eight legs. A dragonfly or a butterfly has six legs. A __dragonfly__ has __two__ pairs of wings, while a __butterfly__ has __one__ pair of wings. __I am not sure whether they are biologically correct, but the values apply here. __

Given the number of total heads, legs, and __pairs of__ wings, please calculate numbers of each kind of bugs. Of course they are integers. 
_However, I do not guarantee that they are positive in the test cases. 
Please regard the minus numbers as cases that does not make sense. _

If answers make sense, return [n\_spider, n\_butterfly, n\_dragonfly]; 
else, please return [-1, -1, -1]. 

Example: 

cal\_n\_bug(3, 20, 3) = [1, 1, 1]
One spider, one butterfly, one dragonfly in total have three heads, twenty legs (8 for the spider, 6 for the butterfly, and 6 for the dragonfly), and _three pairs_ of wings (1 for the butterfly and 2 for the dragonfly).
"""

def calculate_bug_counts(n_head, n_leg, n_wing):
    # Calculate the number of spiders
    spider = (n_leg - n_head * 6) // (8 - 6)
    
    # Calculate the number of butterflies
    butterfly = n_wing - (n_head - spider)
    
    # Calculate the number of dragonflies
    dragonfly = n_head - spider - butterfly
    
    # Check if the solution makes sense
    if spider >= 0 and butterfly >= 0 and dragonfly >= 0:
        return [spider, butterfly, dragonfly]
    else:
        return [-1, -1, -1]