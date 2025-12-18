"""
QUESTION:
Create a function `new21Game(N, K, W, B, M)` that calculates the probability that Alice and Bob have `N` or less points and `M` or less points respectively when they stop drawing in the "New 21 Game". The function should take five parameters: `N`, `K`, `W`, `B`, and `M`, where `0 <= K <= N <= 10000`, `1 <= W <= 10000`, `0 <= B <= M <= 10000`. The function should return two floating point numbers representing the probability for Alice and Bob respectively, with an accuracy of `10^-5`.
"""

def new21Game(N, K, W, B, M):
    """
    Calculate the probability that Alice and Bob have N or less points and M or less points 
    respectively when they stop drawing in the "New 21 Game".

    Args:
    N (int): The maximum number of points Alice can have.
    K (int): The number of points Alice has before she stops drawing.
    W (int): The maximum number of points Alice can draw in one turn.
    B (int): The number of points Bob has before he stops drawing.
    M (int): The maximum number of points Bob can have.

    Returns:
    tuple: A tuple of two floating point numbers representing the probability for Alice and Bob respectively.
    """
    
    # Base case: If K is 0 or N is greater than or equal to K + W, Alice is guaranteed to win
    if K == 0 or N >= K + W: 
        return 1.0, 1.0

    # Initialize a dynamic programming table for Alice
    dp1 = [0.0] * (N + 1)
    dp1[0] = 1.0
    Wsum = 1.0

    # Calculate the probabilities for Alice
    for i in range(1, N + 1):
        dp1[i] = Wsum / W
        if i < K: 
            Wsum += dp1[i]
        if i - W >= 0: 
            Wsum -= dp1[i - W]

    # Calculate the probability for Alice to win
    alice = sum(dp1[K:])

    # Base case: If B is 0 or M is greater than or equal to B + W, Bob is guaranteed to win
    if B == 0 or M >= B + W: 
        return alice, 1.0

    # Initialize a dynamic programming table for Bob
    dp2 = [0.0] * (M + 1)
    dp2[B] = 1.0
    Wsum = dp2[B]

    # Calculate the probabilities for Bob
    for i in range(B + 1, M + 1):
        dp2[i] = Wsum / W
        if i < K: 
            Wsum += dp2[i]
        if i - W >= B: 
            Wsum -= dp2[i - W]

    # Calculate the probability for Bob to win
    bob = sum(dp2[K:])

    # Return the probabilities for Alice and Bob
    return alice, bob