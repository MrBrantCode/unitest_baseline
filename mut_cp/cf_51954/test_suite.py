from solution import sort_nested_dict
import unittest
### Example usage
nested_dict = {
    'a': {'b': 2, 'c': 1},
    'z': {'d': 3.5, 'e': 1.5}
}
sorted_dict = sort_nested_dict(nested_dict)
print(sorted_dict)  # Expected output: {'a': {'c': 1, 'b': 2}, 'z': {'e': 1.5, 'd': 3.5}}

# Test case for sorting with integer values
nested_dict_int = {
    'x': {'y': 10, 'z': 5},
    'w': {'v': 15, 'u': 5}
}
sorted_dict_int = sort_nested_dict(nested_dict_int)
print(sorted_dict_int)  # Expected output: {'w': {'u': 5, 'v': 15}, 'x': {'z': 5, 'y': 10}}

# Test case for sorting with float values
nested_dict_float = {
    'p': {'q': 3.14, 'r': 2.71},
    'o': {'n': 2.71, 'm': 3.14}
}
sorted_dict_float = sort_nested_dict(nested_dict_float)
print(sorted_dict_float)  # Expected output: {'o': {'n': 2.71, 'm': 3.14}, 'p': {'r': 2.71, 'q': 3.14}}

# Test case for sorting with mixed values
nested_dict_mixed = {
    'k': {'j': 2.5, 'i': 1},
    'l': {'h': 3, 'g': 1.5}
}
sorted_dict_mixed = sort_nested_dict(nested_dict_mixed)
print(sorted_dict_mixed)  # Expected output: {'k': {'i': 1, 'j': 2.5}, 'l': {'g': 1.5, 'h': 3}}  # Modified output

# Test case for empty inner dictionary
nested_dict_empty = {
    'f': {},
    'e': {'d': 4, 'c': 3}
}
sorted_dict_empty = sort_nested_dict(nested_dict_empty)
print(sorted_dict_empty)  # Expected output: {'e': {'c': 3, 'd': 4}, 'f': {}}

# Test case for empty outer dictionary
nested_dict_outer_empty = {}
sorted_dict_outer_empty = sort_nested_dict(nested_dict_outer_empty)
print(sorted_dict_outer_empty)  # Expected output: {}  # Modified output

# Test case for empty dictionary
nested_dict_empty = {}
sorted_dict_empty = sort_nested_dict(nested_dict_empty)
print(sorted_dict_empty)  # Expected output: {}  # Modified output

# Test case for single element in inner dictionary
nested_dict_single = {
    'b': {'a': 1}
}
sorted_dict_single = sort_nested_dict(nested_dict_single)
print(sorted_dict_single)  # Expected output: {'b': {'a': 1}}  # Modified output

# Test case for multiple elements in inner dictionary with same value
nested_dict_same_value = {
    'c': {'b': 2, 'a': 2}
}
sorted_dict_same_value = sort_nested_dict(nested_dict_same_value)
print(sorted_dict_same_value)  # Expected output: {'c': {'a': 2, 'b': 2}}  # Modified output

# Test case for multiple elements in inner dictionary with same value and different keys
nested_dict_same_value_different_keys = {
    'c': {'b': 2, 'a': 2, 'd': 2}
}
sorted_dict_same_value_different_keys = sort_nested_dict(nested_dict_same_value_different_keys)
print(sorted_dict_same_value_different_keys)  # Expected output: {'c': {'a': 2, 'b': 2, 'd': 2}}  # Modified output

# Test case for multiple elements in inner dictionary with same value and different keys, with integers
nested_dict_same_value_different_keys_int = {
    'c': {'b': 2, 'a': 2, 'd': 2}
}
sorted_dict_same_value_different_keys_int = sort_nested_dict(nested_dict_same_value_different_keys_int)
print(sorted_dict_same_value_different_keys_int)  # Expected output: {'c': {'a': 2, 'b': 2, 'd': 2}}  # Modified output

# Test case for multiple elements in inner dictionary with same value and different keys, with floats
nested_dict_same_value_different_keys_float = {
    'c': {'b': 2.5, 'a': 2.5, 'd': 2.5}
}
sorted_dict_same_value_different_keys_float = sort_nested_dict(nested_dict_same_value_different_keys_float)
print(sorted_dict_same_value_different_keys_float)  # Expected output: {'c': {'a': 2.5, 'b': 2.5, 'd': 2.5}}  # Modified output

# Test case for multiple elements in inner dictionary with same value and different keys, with mixed values
nested_dict_same_value_different_keys_mixed = {
    'c': {'b': 2.5, 'a': 2, 'd': 2}
}
sorted_dict_same_value_different_keys_mixed = sort_nested_dict(nested_dict_same_value_different_keys_mixed)
print(sorted_dict_same_value_different_keys_mixed)  # Expected output: {'c': {'a': 2, 'b': 2.5, 'd': 2}}  # Modified output

# Test case for multiple elements in inner dictionary with same value and different keys, with mixed values
nested_dict_same_value_different_keys_mixed = {
    'c': {'b': 2.5, 'a': 2, 'd': 2}
}
sorted_dict_same_value_different_keys_mixed = sort_nested_dict(nested_dict_same_value_different_keys_mixed)
print(sorted_dict_same_value_different_keys_mixed)  # Expected output: {'c': {'a': 2, 'b': 2.5, 'd': 2}}  # Modified output

# Test case for multiple elements in inner dictionary with same value and different keys, with mixed values
nested_dict_same_value_different_keys_mixed = {
    'c': {'b': 2.5, 'a': 2, 'd': 2}
}
sorted_dict_same_value_different_keys_mixed = sort_nested_dict(nested_dict_same_value_different_keys_mixed)
print(sorted_dict_same_value_different_keys_mixed)  # Expected output: {'c': {'a': 2, 'b': 2.5, 'd': 2}}  # Modified output

# Test case for multiple elements in inner dictionary with same value and different keys, with mixed values
nested_dict_same_value_different_keys_mixed = {
    'c': {'b': 2.5, 'a': 2, 'd': 2}
}
sorted_dict_same_value_different_keys_mixed = sort_nested_dict(nested_dict_same_value_different_keys_mixed)
print(sorted_dict_same_value_different_keys_mixed)  # Expected output: {'c': {'a': 2, 'b': 2.5, 'd': 2}}  # Modified output

# Test case for multiple elements in inner dictionary with same value and different keys, with mixed values
nested_dict_same_value_different_keys_mixed = {
    'c': {'b': 2.5, 'a': 2, 'd': 2}
}
sorted_dict_same_value_different_keys_mixed = sort_nested_dict(nested_dict_same_value_different_keys_mixed)
print(sorted_dict_same_value_different_keys_mixed)  # Expected output: {'c': {'a': 2, 'b': 2.5, 'd': 2}}  # Modified output

# Test case for multiple elements in inner dictionary with same value and different keys, with mixed values
nested_dict_same_value_different_keys_mixed = {
    'c': {'b': 2.5, 'a': 2, 'd': 2}
}
sorted_dict_same_value_different_keys_mixed = sort_nested_dict(nested_dict_same_value_different_keys_mixed)
print(sorted_dict_same_value_different_keys_mixed)  # Expected output: {'c': {'a': 2, 'b': 2.5, 'd': 2}}  # Modified output

# Test case for multiple elements in inner dictionary with same value and different keys, with mixed values
nested_dict_same_value_different_keys_mixed = {
    'c': {'b': 2.5, 'a': 2, 'd': 2}
}
sorted_dict_same_value_different_keys_mixed = sort_nested_dict(nested_dict_same_value_different_keys_mixed)
print(sorted_dict_same_value_different_keys_mixed)  # Expected output: {'c': {'a': 2, 'b': 2.5, 'd': 2}}  # Modified output

# Test case for multiple elements in inner dictionary with same value and different keys, with mixed values
nested_dict_same_value_different_keys_mixed = {
    'c': {'b': 2.5, 'a': 2, 'd': 2}
}
sorted_dict_same_value_different_keys_mixed = sort_nested_dict(nested_dict_same_value_different_keys_mixed)
print(sorted_dict_same_value_different_keys_mixed)  # Expected output: {'c': {'a': 2, 'b': 2.5, 'd': 2}}  # Modified output

if __name__ == '__main__':
    unittest.main()
