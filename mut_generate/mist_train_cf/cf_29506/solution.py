"""
QUESTION:
Implement a function `compare_datasets` that compares the behavior of two datasets when calling a `get_next` method. The function takes `get_next`, `dataset1`, `dataset2`, `exception_class`, and optional `replacements` as parameters. It should raise an exception if the two datasets do not raise the same error on the first call to `get_next`.

The function should first apply the replacements to the datasets if provided, then call `get_next` on both datasets. If both calls raise the same exception of type `exception_class`, return `True`. If the exceptions are different, raise an exception of type `exception_class` with an error message. If no exceptions are raised, raise an exception of type `exception_class` with an error message.
"""

def compare_datasets(get_next, dataset1, dataset2, exception_class, replacements=None):
    if replacements:
        dataset1 = [replacements.get(item, item) for item in dataset1]
        dataset2 = [replacements.get(item, item) for item in dataset2]

    next1 = get_next(dataset1)
    next2 = get_next(dataset2)

    if type(next1) == type(next2) == exception_class:
        if str(next1) == str(next2):
            return True
        else:
            raise exception_class("Different exceptions raised by dataset1 and dataset2")
    else:
        raise exception_class("No exception raised by dataset1 and dataset2")