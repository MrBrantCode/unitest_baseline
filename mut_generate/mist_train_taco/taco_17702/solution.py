"""
QUESTION:
The accounts of the "Fat to Fit Club (FFC)" association are supervised by John as a volunteered accountant.
The association is funded through financial donations from generous benefactors. John has a list of
the first `n` donations: `[14, 30, 5, 7, 9, 11, 15]`
He wants to know how much the next benefactor should give to the association so that the 
average of the first `n + 1` donations should reach an average of `30`.
After doing the math he found `149`. He thinks that he made a mistake.
Could you help him?

if `dons = [14, 30, 5, 7, 9, 11, 15]` then `new_avg(dons, 30) --> 149`

The function `new_avg(arr, navg)` should return the expected donation
(rounded up to the next integer) that will permit to reach the average `navg`. 

Should the last donation be a non positive number `(<= 0)` John wants us to throw (or raise) an error or

- return Nothing in Haskell
- return None in F#, Ocaml, Scala
- return `-1` in C, Fortran,  Nim, PowerShell, Go, Prolog
- echo `ERROR` in Shell
- raise-argument-error in Racket

so that he clearly sees that his expectations are not great enough.

Notes: 

- all donations and `navg` are numbers (integers or floats), `arr` can be empty.
- See examples below and "Test Samples" to see which return is to be done.

```
new_avg([14, 30, 5, 7, 9, 11, 15], 92) should return 645
new_avg([14, 30, 5, 7, 9, 11, 15], 2) 
should raise an error (ValueError or invalid_argument or argument-error or DomainError) 
or return `-1` or ERROR or Nothing or None depending on the language.
```
"""

from math import ceil

def calculate_next_donation(donations, target_avg):
    """
    Calculate the next donation amount needed to reach the target average.

    Parameters:
    - donations (list of int or float): The list of current donations.
    - target_avg (int or float): The desired average after the next donation.

    Returns:
    - int: The next donation amount, rounded up to the nearest integer.
    
    Raises:
    - ValueError: If the calculated donation amount is non-positive.
    """
    next_donation = ceil((len(donations) + 1) * target_avg - sum(donations))
    if next_donation <= 0:
        raise ValueError("The calculated donation amount is non-positive.")
    return next_donation