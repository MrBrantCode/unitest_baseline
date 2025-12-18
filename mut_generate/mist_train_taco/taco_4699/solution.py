"""
QUESTION:
Find the last element of the given argument(s).

## Examples

```python
last([1, 2, 3, 4]) ==>  4
last("xyz")        ==> "z"
last(1, 2, 3, 4)   ==>  4
```
In **javascript** and **CoffeeScript** a **list** will be an `array`, a `string` or the list of `arguments`.

(courtesy of [haskell.org](http://www.haskell.org/haskellwiki/99_questions/1_to_10))
"""

def find_last_element(*args):
    if len(args) == 1 and hasattr(args[0], '__getitem__'):
        return args[0][-1]
    else:
        return args[-1]