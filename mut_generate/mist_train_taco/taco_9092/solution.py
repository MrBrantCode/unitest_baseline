"""
QUESTION:
Ronald's uncle left him 3 fertile chickens in his will. When life gives you chickens, you start a business selling chicken eggs which is exactly what Ronald decided to do. 

A chicken lays 300 eggs in its first year. However, each chicken's egg production decreases by 20% every following year (rounded down) until when it dies (after laying its quota of eggs). 

After his first successful year of business, Ronald decides to buy 3 more chickens at the start of each year.  


Your Task: 

For a given year, and life span of chicken span,  calculate how many eggs Ronald's chickens will lay him that year, whereby year=1 is when Ronald first got his inheritance and span>0.

If year=0, make sure to return "No chickens yet!".


Note: 
1. All chickens have the same life span regardless of when they are bought. 
2. Let's assume all calculations are made at the end of the year so don't bother taking eggs laid per month into consideration. 
3. Each chicken's egg production goes down by 20% each year, NOT the total number of eggs produced by each 'batch' of chickens. While this might appear to be the same thing, it doesn't once non-integers come into play so take care that this is reflected in your kata!
"""

def calculate_annual_eggs(year, span):
    if year == 0:
        return "No chickens yet!"
    
    total_eggs = 0
    eggs_per_chicken = 300
    
    for current_year in range(1, year + 1):
        # Calculate the number of chickens for the current year
        num_chickens = 3 * current_year
        
        # Calculate the number of eggs laid by each chicken in the current year
        if current_year <= span:
            total_eggs += num_chickens * eggs_per_chicken
        else:
            # Only chickens that are within their lifespan will lay eggs
            total_eggs += (num_chickens - 3 * (current_year - span)) * eggs_per_chicken
        
        # Update the number of eggs laid by each chicken for the next year
        eggs_per_chicken = int(eggs_per_chicken * 0.8)
    
    return total_eggs