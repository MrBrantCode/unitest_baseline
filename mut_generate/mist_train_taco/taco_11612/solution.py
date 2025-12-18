"""
QUESTION:
How much bigger is a 16-inch pizza compared to an 8-inch pizza? A more pragmatic question is: How many 8-inch pizzas "fit" in a 16-incher?

The answer, as it turns out, is exactly four 8-inch pizzas. For sizes that don't correspond to a round number of 8-inchers, you must round the number of slices (one 8-inch pizza = 8 slices), e.g.:

```python
how_many_pizzas(16) -> "pizzas: 4, slices: 0"
how_many_pizzas(12) -> "pizzas: 2, slices: 2"
how_many_pizzas(8) -> "pizzas: 1, slices: 0"
how_many_pizzas(6) -> "pizzas: 0, slices: 4"
how_many_pizzas(0) -> "pizzas: 0, slices: 0"
```
Get coding quick, so you can choose the ideal size for your next meal!
"""

def calculate_pizza_proportions(large_pizza_diameter, small_pizza_diameter, slices_per_small_pizza=8):
    # Calculate the area of the large pizza
    large_pizza_area = (large_pizza_diameter / 2) ** 2 * 3.14159
    
    # Calculate the area of the small pizza
    small_pizza_area = (small_pizza_diameter / 2) ** 2 * 3.14159
    
    # Calculate the number of small pizzas that fit into the large pizza
    total_small_pizzas = large_pizza_area / small_pizza_area
    
    # Calculate the number of full pizzas and remaining slices
    number_of_small_pizzas, remaining_area = divmod(total_small_pizzas, 1)
    number_of_slices = int(remaining_area * slices_per_small_pizza)
    
    return f"pizzas: {int(number_of_small_pizzas)}, slices: {number_of_slices}"