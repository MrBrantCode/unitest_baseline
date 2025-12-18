"""
QUESTION:
# Convergents of e
The square root of 2 can be written as an infinite continued fraction.
![img](http://img0.ph.126.net/x1Hyc4iHQg0Jz2EInmT3ag==/6597639313681841979.png)  
The infinite continued fraction can be written, √2 = [1;(2)], (2) indicates that 2 repeats ad infinitum. In a similar way, √23 = [4;(1,3,1,8)].

It turns out that the sequence of partial values of continued fractions for square roots provide the best rational approximations. Let us consider the convergents for √2.
![img](http://img1.ph.126.net/xme9gNBQdA7bvQkwIftznQ==/6597819633588793645.png)  
Hence the sequence of the first ten convergents for √2 are:

1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, …

What is most surprising is that the important mathematical constant,
e = [2; 1,2,1, 1,4,1, 1,6,1 , … , 1,2k,1, …].

The first ten terms in the sequence of convergents for e are:

2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, …

The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.

Find the sum of digits in the numerator of the mth convergent of the continued fraction for e.


- Powered by [Project Euler](https://projecteuler.net/problem=65)
"""

def sum_of_numerator_digits_of_e_convergent(m):
    # Initialize the list to store the numerators of the convergents
    e = [1, 2]
    
    # Generate the numerators up to the mth convergent
    for n in range(1, m):
        for f in (1, 2 * n, 1):
            e.append(f * e[-1] + e[-2])
    
    # Get the numerator of the mth convergent
    numerator = e[m - 1]
    
    # Calculate the sum of the digits in the numerator
    sum_of_digits = sum(map(int, str(numerator)))
    
    return sum_of_digits