"""
QUESTION:
Alice and Bob decided to eat some fruit. In the kitchen they found a large bag of oranges and apples. Alice immediately took an orange for herself, Bob took an apple. To make the process of sharing the remaining fruit more fun, the friends decided to play a game. They put multiple cards and on each one they wrote a letter, either 'A', or the letter 'B'. Then they began to remove the cards one by one from left to right, every time they removed a card with the letter 'A', Alice gave Bob all the fruits she had at that moment and took out of the bag as many apples and as many oranges as she had before. Thus the number of oranges and apples Alice had, did not change. If the card had written letter 'B', then Bob did the same, that is, he gave Alice all the fruit that he had, and took from the bag the same set of fruit. After the last card way removed, all the fruit in the bag were over.

You know how many oranges and apples was in the bag at first. Your task is to find any sequence of cards that Alice and Bob could have played with.


-----Input-----

The first line of the input contains two integers, x, y (1 ≤ x, y ≤ 10^18, xy > 1) — the number of oranges and apples that were initially in the bag.


-----Output-----

Print any sequence of cards that would meet the problem conditions as a compressed string of characters 'A' and 'B. That means that you need to replace the segments of identical consecutive characters by the number of repetitions of the characters and the actual character. For example, string AAABAABBB should be replaced by string 3A1B2A3B, but cannot be replaced by 2A1A1B2A3B or by 3AB2A3B. See the samples for clarifications of the output format. The string that you print should consist of at most 10^6 characters. It is guaranteed that if the answer exists, its compressed representation exists, consisting of at most 10^6 characters. If there are several possible answers, you are allowed to print any of them.

If the sequence of cards that meet the problem statement does not not exist, print a single word Impossible.


-----Examples-----
Input
1 4

Output
3B

Input
2 2

Output
Impossible

Input
3 2

Output
1A1B



-----Note-----

In the first sample, if the row contained three cards with letter 'B', then Bob should give one apple to Alice three times. So, in the end of the game Alice has one orange and three apples, and Bob has one apple, in total it is one orange and four apples.

In second sample, there is no answer since one card is not enough for game to finish, and two cards will produce at least three apples or three oranges.

In the third sample, cards contain letters 'AB', so after removing the first card Bob has one orange and one apple, and after removal of second card Alice has two oranges and one apple. So, in total it is three oranges and two apples.
"""

def find_card_sequence(x: int, y: int) -> str:
    """
    Finds a sequence of cards that Alice and Bob could have played with, given the initial number of oranges and apples.

    Parameters:
    x (int): The initial number of oranges.
    y (int): The initial number of apples.

    Returns:
    str: A compressed string representing the sequence of cards or "Impossible" if no valid sequence exists.
    """
    
    def gcd(a: int, b: int) -> int:
        """Helper function to compute the greatest common divisor (GCD) of two numbers."""
        if b == 0:
            return a
        else:
            return gcd(b, a % b)

    # Check if the GCD of x and y is greater than 1
    if gcd(x, y) > 1:
        return 'Impossible'

    # Initialize the answer string
    ans = ''
    a, b = 'A', 'B'

    # Loop until either x or y becomes 1
    while x != 1 or y != 1:
        if x < y:
            # Swap x and y, and also swap the characters a and b
            x, y, a, b = y, x, b, a
        # Append the number of times the current character should be repeated
        ans += str((x - 1) // y) + a
        # Update x to reflect the remaining number of fruits after the current operation
        x = x - (x - 1) // y * y

    return ans