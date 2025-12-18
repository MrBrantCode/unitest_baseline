"""
QUESTION:
Approximate N(d1) and N(d2) in the Black-Scholes framework without using implied volatility. 

Create a function called approximate_n_d1_d2() that takes the following parameters: 
- C: the option price 
- S: the price of the underlying asset 
- K: the exercise price of the option 

Assume the option is a European call option and the approximation should hold the correct limit behavior, i.e., N(d1) or N(d2) goes to 0 as C goes to 0.
"""

def approximate_n_d1_d2(C, S, K):
    """
    Approximate N(d1) and N(d2) in the Black-Scholes framework without using implied volatility.
    
    This function uses rough approximations of N(d1) and N(d2) based on the moneyness of the option.
    
    Parameters:
    C (float): The option price.
    S (float): The price of the underlying asset.
    K (float): The exercise price of the option.
    
    Returns:
    tuple: A tuple containing the approximated N(d1) and N(d2) values.
    """

    # Approximate N(d1) as 1 if the option is in the money, 0 otherwise
    N_d1 = 1 if S > K else 0
    
    # Approximate N(d2) as 1 if the option is in the money, 0 otherwise
    N_d2 = 1 if S > K else 0
    
    return N_d1, N_d2