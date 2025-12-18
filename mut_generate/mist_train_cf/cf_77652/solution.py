"""
QUESTION:
Design three functions, `scarf_length`, `hat_diameter`, and `mitten_length`, to calculate the total length or diameter of each knitting item. Each function should take two arguments: the initial length or diameter that has been knitted and the additional amount that has been knitted since. The initial length or diameter is a proportion of the remaining length, and the function should return the total length or diameter based on the given proportions and additional lengths. 

The proportions for each item are as follows: 
- Scarf: initial length is 3/4 of the remaining length, and after knitting more, it becomes 4/5 of the remaining length.
- Hat: initial diameter is 2/3 of the remaining diameter, and after knitting more, it becomes 3/4 of the remaining diameter.
- Mitten: initial length is 1/2 of the remaining length, and after knitting more, it becomes 3/5 of the remaining length.

The additional lengths are 10 cm for the scarf, 2 cm for the hat, and 5 cm for the mitten. The functions should be designed with efficiency in mind to handle a large amount of knitting data.
"""

def scarf_length(initial_length, additional):
    total_length = (initial_length + additional) / (4/5)
    return total_length

def hat_diameter(initial_diameter, additional):
    total_diameter = (initial_diameter + additional) / (3/4)
    return total_diameter

def mitten_length(initial_length, additional):
    total_length = (initial_length + additional) / (3/5)
    return total_length