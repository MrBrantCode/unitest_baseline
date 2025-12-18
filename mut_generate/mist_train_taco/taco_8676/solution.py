"""
QUESTION:
This is related to my other Kata about cats and dogs.

# Kata Task

I have a cat and a dog which I got as kitten / puppy.

I forget when that was, but I do know their current ages as `catYears` and `dogYears`.

Find how long I have owned each of my pets and return as a list [`ownedCat`, `ownedDog`]

NOTES:
* Results are truncated whole numbers of "human" years

## Cat Years

* `15` cat years for first year
* `+9` cat years for second year
* `+4` cat years for each year after that

## Dog Years

* `15` dog years for first year
* `+9` dog years for second year
* `+5` dog years for each year after that



**References**

* http://www.catster.com/cats-101/calculate-cat-age-in-cat-years
* http://www.slate.com/articles/news_and_politics/explainer/2009/05/a_dogs_life.html
"""

def calculate_pet_ownership_years(catYears, dogYears):
    # Calculate the number of human years the cat has been owned
    ownedCat = 0 if catYears < 15 else 1 if catYears < 24 else 2 + (catYears - 24) // 4
    
    # Calculate the number of human years the dog has been owned
    ownedDog = 0 if dogYears < 15 else 1 if dogYears < 24 else 2 + (dogYears - 24) // 5
    
    # Return the result as a list
    return [ownedCat, ownedDog]