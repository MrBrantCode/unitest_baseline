"""
QUESTION:
There was a test in your class and you passed it. Congratulations!
But you're an ambitious person. You want to know if you're better than the average student in your class.

You receive an array with your peers' test scores. Now calculate the average and compare your score!

~~~if-not:nasm,racket
Return `True` if you're better, else `False`!
~~~

~~~if:racket
Return #t if you're better, else #f.
~~~

~~~if:nasm
Return `1` if you're better, else `0`!
~~~

### Note:

Your points are not included in the array of your class's points. For calculating the average point you may add your point to the given array!
"""

def better_than_average(class_points, your_points):
    # Calculate the average score of the class
    average_score = sum(class_points) / len(class_points)
    
    # Compare your score with the average score
    return your_points > average_score