"""
QUESTION:
Construct a function `fibonacci_prime` that takes an integer `n` as input where 2 ≤ n ≤ 50. The function should generate the first n terms of the Fibonacci sequence, print each term, and label it as "prime" if it is a prime number. The function should return the sum of all the prime terms in the sequence.
"""

def fibonacci_prime(n):
    fib_seq = [0, 1] 
    prime_sum = 0 
    output = "" 
    
    if n < 2 or n > 50:
        return "Input must be between 2 and 50"
    
    for i in range(2, n):
        fib_seq.append(fib_seq[i-1] + fib_seq[i-2]) 
        
        if fib_seq[i] > 1: 
            is_prime = True
            for j in range(2, int(fib_seq[i]**0.5) + 1): 
                if fib_seq[i] % j == 0:
                    is_prime = False
                    break
            
            if is_prime: 
                prime_sum += fib_seq[i]
                output += str(fib_seq[i]) + " (prime), "
            else:
                output += str(fib_seq[i]) + ", "
    
    print(output[:-2]) 
    return prime_sum