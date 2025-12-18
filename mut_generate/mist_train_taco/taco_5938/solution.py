"""
QUESTION:
Complete the function/method so that it takes CamelCase string and returns the string in snake_case notation. Lowercase characters can be numbers. If method gets number, it should return string.

Examples:

``` javascript
//  returns test_controller
toUnderscore('TestController');

// returns movies_and_books
toUnderscore('MoviesAndBooks');

// returns app7_test
toUnderscore('App7Test');

// returns "1"
toUnderscore(1);
```

``` coffeescript  
#  returns test_controller
toUnderscore 'TestController'

# returns movies_and_books
toUnderscore 'MoviesAndBooks'

# returns app7_test
toUnderscore 'App7Test'

# returns "1"
toUnderscore 1
```
"""

import re

def convert_camel_to_snake(input_string):
    """
    Converts a CamelCase string to a snake_case string.
    If the input is a number, it returns the string representation of that number.
    
    Parameters:
    input_string (str or int): The input string or number to be converted.
    
    Returns:
    str: The converted snake_case string.
    """
    return re.sub('(.)([A-Z])', '\\1_\\2', str(input_string)).lower()