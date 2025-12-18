"""
QUESTION:
The Quarkgo Empire Expeditionary Force is an evil organization that plans to invade the Earth. In keeping with the tradition of the invaders, they continued to send monsters at a pace of one every week, targeting the area around Tokyo in Japan. However, each time, five warriors calling themselves the Human Squadron Earth Five appeared, and the monster who was rampaging in the city was easily defeated.

Walzard Thru (Earth name: Genmasa) is a female executive of the Quarkgo Empire Expeditionary Force who is seriously worried about such a situation. She had a headache under a commander who wouldn't learn anything from her weekly defeat, or a genius scientist who repeated some misplaced inventions.

Meanwhile, the next operation was decided to send the blood-sucking monster Dracula to Japan. Dracula is a terrifying monster who turns a blood-sucking human into Dracula. Humans who have been sucked by Dracula also suck the blood of other humans to increase their fellow Dracula. In this way, the strategy is to fill the entire earth with Dracula.

Upon hearing this, Walzard soon realized. This strategy is different from the usual sequel strategy such as taking over a kindergarten bus. It's rare for that bad commander to have devised it, and it has the potential to really conquer the Earth.

The momentum of the game is terrifying. Dracula, who landed on the ground, quickly increased the number of friends. If we went on like this, the invasion of the earth seemed to be just a stone's throw away. However, at that moment, a strong and unpleasant premonition ran through Walzard's mind. No way, if this monster, the original is defeated, his friends will not be wiped out, right?

When I asked the scientist who designed and developed Dracula in a hurry, he was still worried about Walzard. It is designed so that when the original Dracula is destroyed, all humans who have sucked blood will return to their original state. Don't be foolish developer. Why did you add such an extra function!

Walzard jumped to the developer and decided to kick his knee, and immediately started the original recovery work. No matter how much the original and the fake look exactly the same, if nothing is done, it is visible that the rushed Earth Five will see through the original for some reason and be defeated.

According to the developers, all Draculaized humans weigh the same, but the original Dracula is a little heavier. Then you should be able to find the original by using only the balance. You must find and retrieve the original Dracula as soon as possible before the Earth Five appears.



Input

N

The integer N (2 ≤ N ≤ 2,000,000,000) is written on the first line of the input. This represents the total number of Draculas, both original and fake.

Output

In the worst case, how many times is it enough to use the balance to find one original from the N Draculas using the balance? Output the minimum value. However, comparing the weights of several Draculas placed on the left and right plates of the balance is counted as one time.

Examples

Input

8


Output

2


Input

30


Output

4


Input

2000000000


Output

20
"""

def find_original_dracula(N: int) -> int:
    """
    Calculate the minimum number of times the balance needs to be used to find the original Dracula
    from N Draculas in the worst case.

    Parameters:
    N (int): The total number of Draculas, both original and fake.

    Returns:
    int: The minimum number of times the balance needs to be used.
    """
    n = 1
    ans = 1
    while True:
        n *= 3
        if n >= N:
            return ans
        ans += 1