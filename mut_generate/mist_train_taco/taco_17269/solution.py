"""
QUESTION:
Your task in this kata is to implement the function `create_number_class` which will take a string parameter `alphabet` and return a class representing a number composed of this alphabet.

The class number will implement the four classical arithmetic operations (`+`, `-`, `*`, `//`), a method to convert itself to string, and a `convert_to` method which will take another class number as parameter and will return the value of the actual class number converted to the equivalent value with tha alphabet of the parameter class (return a new instance of this one).

Example:

```python
BinClass = create_number_class('01')
HexClass = create_number_class('0123456789ABCDEF')

x = BinClass('1010')
y = BinClass('10')

print(x+y)                   => '1100'
isinstance(x+y, BinClass)    => True
print(x.convert_to(HexClass) => 'A'
```

___Notes:___

* Only positives integers will be used (either as parameters or results of calculations).
* You'll never encounter invalid calculations (divisions by zero or things like that).
* Alphabets will contain at least 2 characters.
"""

def create_number_class(alphabet):
    n = len(alphabet)

    class Number(object):

        def __init__(self, s):
            if isinstance(s, str):
                v = 0
                for c in s:
                    v = v * n + alphabet.index(c)
            else:
                v = s
            self.value = v

        def __add__(self, other):
            return Number(self.value + other.value)

        def __sub__(self, other):
            return Number(self.value - other.value)

        def __mul__(self, other):
            return Number(self.value * other.value)

        def __floordiv__(self, other):
            return Number(self.value // other.value)

        def __str__(self):
            ret = []
            v = int(self.value)
            while v:
                (v, r) = divmod(v, n)
                ret.append(alphabet[r])
            return ''.join(reversed(ret or alphabet[0]))

        def convert_to(self, cls):
            return cls(self.value)
    
    return Number