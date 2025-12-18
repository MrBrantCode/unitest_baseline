"""
QUESTION:
Debug the functions
Should be easy, begin by looking at the code. Debug the code and the functions should work.
There are three functions: ```Multiplication (x)``` ```Addition (+)``` and ```Reverse (!esreveR)```

i {
  font-size:16px;
}

#heading {
  padding: 2em;
  text-align: center;
  background-color: #0033FF;
  width: 100%;
  height: 5em;
}
"""

from functools import reduce
from operator import mul

def perform_operations(operation, data):
    if operation == "multiplication":
        if not isinstance(data, list):
            raise ValueError("For multiplication, data must be a list of numbers.")
        return reduce(mul, data)
    
    elif operation == "addition":
        if not isinstance(data, list):
            raise ValueError("For addition, data must be a list of numbers.")
        return sum(data)
    
    elif operation == "reverse":
        if not isinstance(data, str):
            raise ValueError("For reverse, data must be a string.")
        return data[::-1]
    
    else:
        raise ValueError("Invalid operation. Supported operations are 'multiplication', 'addition', and 'reverse'.")