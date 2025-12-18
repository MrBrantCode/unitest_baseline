"""
QUESTION:
What is the answer to life the universe and everything

Create a function that will make anything true

```python
    anything({}) != [],          'True'
    anything('Hello') < 'World', 'True'
    anything(80) > 81,           'True'
    anything(re) >= re,          'True'
    anything(re) <= math,        'True'
    anything(5) == ord,          'True'
```

Source: [CheckIO](https://checkio.org/mission/solution-for-anything/)
"""

def make_anything_true(value):
    class Anything:
        def __init__(self, foo):
            pass
        
        def __eq__(self, other):
            return True
        
        __ne__ = __lt__ = __le__ = __gt__ = __ge__ = __eq__
    
    return Anything(value)