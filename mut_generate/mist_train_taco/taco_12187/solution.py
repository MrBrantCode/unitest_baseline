"""
QUESTION:
```if:python,php
In this kata you will have to write a function that takes `litres` and `price_per_litre` as arguments. Purchases of 2 or more litres get a discount of 5 cents per litre, purchases of 4 or more litres get a discount of 10 cents per litre, and so on every two litres, up to a maximum discount of 25 cents per litre. But total discount per litre cannot be more than 25 cents. Return the toal cost rounded to 2 decimal places. Also you can guess that there will not be negative or non-numeric inputs.

Good Luck!
```

```if:csharp,java,javascript
In this kata you will have to write a function that takes `litres` and `pricePerLitre` as arguments. Purchases of 2 or more litres get a discount of 5 cents per litre, purchases of 4 or more litres get a discount of 10 cents per litre, and so on every two litres, up to a maximum discount of 25 cents per litre. But total discount per litre cannot be more than 25 cents. Return the toal cost rounded to 2 decimal places. Also you can guess that there will not be negative or non-numeric inputs.

Good Luck!
```
"""

def calculate_fuel_cost(litres, price_per_litre):
    # Calculate the discount based on the number of litres
    discount_per_litre = int(min(litres, 10) / 2) * 0.05
    
    # Ensure the discount does not exceed the maximum allowed
    discount_per_litre = min(discount_per_litre, 0.25)
    
    # Calculate the final price per litre after discount
    final_price_per_litre = price_per_litre - discount_per_litre
    
    # Calculate the total cost
    total_cost = final_price_per_litre * litres
    
    # Return the total cost rounded to 2 decimal places
    return round(total_cost, 2)