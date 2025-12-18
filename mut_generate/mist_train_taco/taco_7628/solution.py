"""
QUESTION:
# Definition (Primorial Of a Number)

*Is similar to factorial of a number*, **_In primorial_**, not all the natural numbers get multiplied, **_only prime numbers are multiplied to calculate the primorial of a number_**. It's denoted with **_P_****_#_** and it is the product of the first n prime numbers.
___ 

# Task

**_Given_** *a number N* , **_calculate its primorial_**. ![!alt](https://i.imgur.com/mdX8dJP.png)  ![!alt](https://i.imgur.com/mdX8dJP.png)  
___

# Notes

* **_Only positive_** numbers *will be passed (N > 0)* .
___

# Input >> Output Examples:

``` cpp
1- numPrimorial (3) ==> return (30)
```

## **_Explanation_**:

**_Since_** *the passed number is (3)* ,**_Then_** **_the primorial_** *should obtained by multiplying*  ```2 * 3 * 5 = 30 .```

### Mathematically written as , **_P_**3**_#_** = 30 .
___ 

## **_Explanation_**:

**_Since_** *the passed number is (5)* ,**_Then_** **_the primorial_** *should obtained by multiplying*  ``` 2 * 3 * 5 * 7 * 11 = 2310 .```

### Mathematically written as , **_P_**5**_#_** = 2310 .
___

## **_Explanation_**: 

**_Since_** *the passed number is (6)* ,**_Then_** **_the primorial_** *should obtained by multiplying*  ``` 2 * 3 * 5 * 7 * 11 * 13 = 30030 .```

### Mathematically written as , **_P_**6**_#_** = 30030 .
___
___
___

# [Playing with Numbers Series](https://www.codewars.com/collections/playing-with-numbers)

# [Playing With Lists/Arrays Series](https://www.codewars.com/collections/playing-with-lists-slash-arrays)

# [For More Enjoyable Katas](http://www.codewars.com/users/MrZizoScream/authored)
___

## ALL translations are welcomed

## Enjoy Learning !!
# Zizou
"""

def calculate_primorial(n):
    # Initialize the primorial product with the first prime number
    primorial = 2
    # Start checking from the next prime number
    x = 3
    # Decrease n by 1 since we already included 2 in the primorial
    n -= 1
    
    # Loop until we have found n prime numbers
    while n > 0:
        # Check if x is a prime number
        if all(x % d != 0 for d in range(3, int(x ** 0.5) + 1, 2)):
            # Multiply the primorial by the prime number
            primorial *= x
            # Decrease the count of primes needed
            n -= 1
        # Move to the next odd number to check for primality
        x += 2
    
    return primorial