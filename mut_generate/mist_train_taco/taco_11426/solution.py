"""
QUESTION:
The [half-life](https://en.wikipedia.org/wiki/Half-life) of a radioactive substance is the time it takes (on average) for one-half of its atoms to undergo radioactive decay.

# Task Overview
Given the initial quantity of a radioactive substance, the quantity remaining after a given period of time, and the period of time, return the half life of that substance. 

# Usage Examples

```if:csharp
Documentation:
Kata.HalfLife Method (Double, Double, Int32)

Returns the half-life for a substance given the initial quantity, the remaining quantity, and the elasped time.

Syntax


public
static
double HalfLife(
double quantityInitial,
    double quantityRemaining,
int time
    )
  



Parameters

quantityInitial

Type: System.Double
The initial amount of the substance.

quantityRemaining

Type: System.Double
The current amount of the substance.

time

Type: System.Int32
The amount of time elapsed.

Return Value

Type: System.Double
  A floating-point number representing the half-life of the substance.

```
"""

from math import log

def calculate_half_life(initial_quantity: float, remaining_quantity: float, elapsed_time: int) -> float:
    """
    Calculate the half-life of a radioactive substance given the initial quantity,
    the remaining quantity after a certain period of time, and the elapsed time.

    Parameters:
    - initial_quantity (float): The initial amount of the substance.
    - remaining_quantity (float): The current amount of the substance.
    - elapsed_time (int): The amount of time elapsed.

    Returns:
    - float: The half-life of the substance.
    """
    return elapsed_time / log(initial_quantity / remaining_quantity, 2)