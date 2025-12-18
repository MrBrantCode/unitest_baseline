"""
QUESTION:
Implement a function `simulateBouncingBall` that takes three parameters: `iterations`, `spaceWidth`, and `spaceHeight`, representing the number of iterations for the animation, the width of the space, and the height of the space respectively. The function should return a string representing the animation of a bouncing ball, with the ball moving up and down within the defined space for the specified number of iterations. The ball's position is represented by 'O', and the space is represented by underscores and vertical bars. The ball starts at the top of the space and moves in a bouncing motion.
"""

def simulateBouncingBall(iterations, spaceWidth, spaceHeight):
    ball = "O"
    space = "_" * spaceWidth
    animation = []
    for i in range(iterations):
        for j in range(spaceHeight):
            if j == 0 or j == spaceHeight - 1:
                animation.append(space)
            else:
                if j == i % (spaceHeight - 2) + 1:
                    animation.append(" " * (spaceWidth // 2 - j) + "\\" + ball + " " * (j - 1) + "/" + " " * (spaceWidth // 2 - j))
                else:
                    animation.append(" " * spaceWidth)
    return "\n".join(animation)