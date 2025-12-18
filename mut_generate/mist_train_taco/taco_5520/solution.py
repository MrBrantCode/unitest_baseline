"""
QUESTION:
An eviternity number is a number which:
* contains only digits 8, 5 and 3, and 
* the count of the digit `8` >= count of digit `5` >= count of digit `3`. 

The first few eviternity numbers are as follows. 
```Haskell
[8, 58, 85, 88, 358, 385, 538, 583, 588, 835, 853, 858, 885, 888]
```
You will be given two integers, `a` and `b`, and your task is to return the number of eviternity numbers in the range `>= a and < b`.
```Haskell
For example:
solve(0,1000) = 14, because they are [8, 58, 85, 88, 358, 385, 538, 583, 588, 835, 853, 858, 885, 888]
```

The upper bound will not exceed `500,000`.

More examples in test cases. Good luck!
"""

def count_eviternity_numbers(a: int, b: int) -> int:
    # List of precomputed eviternity numbers
    eviternity_numbers = [
        8, 58, 85, 88, 358, 385, 538, 583, 588, 835, 853, 858, 885, 888, 3588, 3858, 3885, 5388, 5588, 5838, 5858, 5883, 5885, 5888, 8358, 8385, 8538, 8558, 8583, 8585, 8588, 8835, 8853, 8855, 8858, 8885, 8888, 35588, 35858, 35885, 35888, 38558, 38585, 38588, 38855, 38858, 38885, 53588, 53858, 53885, 53888, 55388, 55838, 55883, 55888, 58358, 58385, 58388, 58538, 58583, 58588, 58835, 58838, 58853, 58858, 58883, 58885, 58888, 83558, 83585, 83588, 83855, 83858, 83885, 85358, 85385, 85388, 85538, 85583, 85588, 85835, 85838, 85853, 85858, 85883, 85885, 85888, 88355, 88358, 88385, 88535, 88538, 88553, 88558, 88583, 88585, 88588, 88835, 88853, 88855, 88858, 88885, 88888, 335588, 335858, 335885, 338558, 338585, 338855, 353588, 353858, 353885, 355388, 355838, 355883, 355888, 358358, 358385, 358538, 358583, 358588, 358835, 358853, 358858, 358885, 358888, 383558, 383585, 383855, 385358, 385385, 385538, 385583, 385588, 385835, 385853, 385858, 385885, 385888, 388355, 388535, 388553, 388558, 388585, 388588, 388855, 388858, 388885
    ]
    
    # Count the eviternity numbers in the range [a, b)
    return sum(1 for x in eviternity_numbers if a <= x < b)