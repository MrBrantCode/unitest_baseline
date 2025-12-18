"""
QUESTION:
In this kata the function returns an array/list of numbers without its last element. The function is already written for you and the basic tests pass, but random tests fail. Your task is to figure out why and fix it.

Good luck!

Hint: watch out for side effects.

~~~if:javascript
Some good reading: [MDN Docs about arrays](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
~~~
~~~if:python
Some good reading: [Python Lists](http://www.compciv.org/guides/python/fundamentals/lists-mutability/)
~~~
"""

def remove_last_element(lst):
    """
    Returns a new list that is a copy of the input list but without the last element.

    Parameters:
    lst (list): The input list.

    Returns:
    list: A new list without the last element.
    """
    return lst[:-1]