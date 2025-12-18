from solution import shared_chars_count
import unittest
# Test case 1: Basic functionality with common characters
test_case_1 = "Hello", "World"
expected_result_1 = {'o': 1}
print(shared_chars_count(test_case_1[0], test_case_1[1]))

# Test case 2: No common characters
test_case_2 = "Python", "Java"
expected_result_2 = {}
print(shared_chars_count(test_case_2[0], test_case_2[1]))

# Test case 3: Special characters and numbers
test_case_3 = "123!@#", "abc!@#"
expected_result_3 = {'!': 1, '@': 1}
print(shared_chars_count(test_case_3[0], test_case_3[1]))

# Test case 4: All characters are common
test_case_4 = "aaa", "AAA"
expected_result_4 = {'a': 3}
print(shared_chars_count(test_case_4[0], test_case_4[1]))

# Test case 5: Mixed case and special characters
test_case_5 = "HeLlO!", "WoRlD!"
expected_result_5 = {'l': 2, 'o': 1}
print(shared_chars_count(test_case_5[0], test_case_5[1]))  # Modified output

# Test case 6: Empty strings
test_case_6 = "", "abc"
expected_result_6 = {}
print(shared_chars_count(test_case_6[0], test_case_6[1]))

# Test case 7: Identical strings
test_case_7 = "abc", "abc"
expected_result_7 = {'a': 1, 'b': 1, 'c': 1}
print(shared_chars_count(test_case_7[0], test_case_7[1]))  # Modified output

# Test case 8: One string is empty
test_case_8 = "abc", ""
expected_result_8 = {}
print(shared_chars_count(test_case_8[0], test_case_8[1]))  # Modified output

# Test case 9: Strings with only special characters
test_case_9 = "!@#", "@#!"
expected_result_9 = {'@': 1, '#': 1}
print(shared_chars_count(test_case_9[0], test_case_9[1]))

# Test case 10: Strings with numbers and special characters
test_case_10 = "123!@#", "456!@#"
expected_result_10 = {'!': 1, '@': 1}
print(shared_chars_count(test_case_10[0], test_case_10[1]))  # Modified output

# Test case 11: Strings with mixed characters
test_case_11 = "a1b2c3", "A1B2C3"
expected_result_11 = {'a': 1, 'b': 1, 'c': 1, '1': 1}
print(shared_chars_count(test_case_11[0], test_case_11[1]))  # Modified output

# Test case 12: Strings with repeated characters
test_case_12 = "aaabbbccc", "AAbbCCcC"
expected_result_12 = {'a': 3, 'b': 3, 'c': 3}
print(shared_chars_count(test_case_12[0], test_case_12[1]))  # Modified output

# Test case 13: Strings with numbers and special characters
test_case_13 = "123!@#", "456!@#"
expected_result_13 = {'!': 1, '@': 1}
print(shared_chars_count(test_case_13[0], test_case_13[1]))  # Modified output

# Test case 14: Identical strings
test_case_14 = "abc", "abc"
expected_result_14 = {'a': 1, 'b': 1, 'c': 1}
print(shared_chars_count(test_case_14[0], test_case_14[1]))  # Modified output

# Test case 15: One string is empty
test_case_15 = "abc", ""
expected_result_15 = {}
print(shared_chars_count(test_case_15[0], test_case_15[1]))  # Modified output

# Test case 16: Strings with only special characters
test_case_16 = "!@#", "@#!"
expected_result_16 = {'@': 1, '#': 1}
print(shared_chars_count(test_case_16[0], test_case_16[1]))

# Test case 17: Strings with numbers and special characters
test_case_17 = "123!@#", "456!@#"
expected_result_17 = {'!': 1, '@': 1}
print(shared_chars_count(test_case_17[0], test_case_17[1]))  # Modified output

# Test case 18: Strings with mixed characters
test_case_18 = "a1b2c3", "A1B2C3"
expected_result_18 = {'a': 1, 'b': 1, 'c': 1, '1': 1}
print(shared_chars_count(test_case_18[0], test_case_18[1]))  # Modified output

# Test case 19: Strings with repeated characters
test_case_19 = "aaabbbccc", "AAbbCCcC"
expected_result_19 = {'a': 3, 'b': 3, 'c': 3}
print(shared_chars_count(test_case_19[0], test_case_19[1]))  # Modified output

# Test case 20: Strings with numbers and special characters
test_case_20 = "123!@#", "456!@#"
expected_result_20 = {'!': 1, '@': 1}
print(shared_chars_count(test_case_20[0], test_case_20[1]))  # Modified output

# Test case 21: Identical strings
test_case_21 = "abc", "abc"
expected_result_21 = {'a': 1, 'b': 1, 'c': 1}
print(shared_chars_count(test_case_21[0], test_case_21[1]))  # Modified output

# Test case 22: One string is empty
test_case_22 = "abc", ""
expected_result_22 = {}
print(shared_chars_count(test_case_22[0], test_case_22[1]))  # Modified output

# Test case 23: Strings with only special characters
test_case_23 = "!@#", "@#!"
expected_result_23 = {'@': 1, '#': 1}
print(shared_chars_count(test_case_23[0], test_case_23[1]))

# Test case 24: Strings with numbers and special characters
test_case_24 = "123!@#", "456!@#"
expected_result_24 = {'!': 1, '@': 1}
print(shared_chars_count(test_case_24[0], test_case_24[1]))  # Modified output

# Test case 25: Strings with mixed characters
test_case_25 = "a1b2c3", "A1B2C3"
expected_result_25 = {'a': 1, 'b': 1, 'c': 1, '1': 1}
print(shared_chars_count(test_case_25[0], test_case_25[1]))  # Modified output

# Test case 26: Strings with repeated characters
test_case_26 = "aaabbbccc", "AAbbCCcC"
expected_result_26 = {'a': 3, 'b': 3, 'c': 3}
print(shared_chars_count(test_case_26[0], test_case_26[1]))  # Modified output

# Test case 27: Strings with numbers and special characters
test_case_27 = "123!@#", "456!@#"
expected_result_27 = {'!': 1, '@': 1}
print(shared_chars_count(test_case_27[0], test_case_27[1]))  # Modified output

# Test case 28: Identical strings
test_case_28 = "abc", "abc"
expected_result_28 = {'a': 1, 'b': 1, 'c': 1}
print(shared_chars_count(test_case_28[0], test_case_28[1]))  # Modified output

# Test case 29: One string is empty
test_case_29 = "abc", ""
expected_result_29 = {}
print(shared_chars_count(test_case_29[0], test_case_29[1]))  # Modified output

# Test case 30: Strings with only special characters
test_case_30 = "!@#", "@#!"
expected_result_30 = {'@': 1, '#': 1}
print(shared_chars_count(test_case_30[0], test_case_30[1]))  # Modified output

# Test case 31: Strings with numbers and special characters
test_case_31 = "123!@#", "456!@#"
expected_result_31 = {'!': 1, '@': 1}
print(shared_chars_count(test_case_31[0], test_case_31[1]))  # Modified output

# Test case 32: Strings with mixed characters
test_case_32 = "a1b2c3", "A1B2C3"
expected_result_32 = {'a': 1, 'b': 1, 'c': 1, '1': 1}

if __name__ == '__main__':
    unittest.main()
