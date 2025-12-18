"""
QUESTION:
Develop a function named `replace_n_instances` that takes four arguments: `main_string`, `searching_substring`, `replacement_string`, and `instances_to_replace`. The function should return `main_string` with the first `instances_to_replace` instances of `searching_substring` replaced by `replacement_string`.
"""

def replace_n_instances(main_string, searching_substring, replacement_string, instances_to_replace):
    count = 0
    start = 0
    while count < instances_to_replace:
        pos = main_string.find(searching_substring, start)
        if pos != -1: 
            main_string = main_string[:pos] + replacement_string + main_string[pos+len(searching_substring):]
            count += 1
            start = pos + len(replacement_string) 
        else:
            break
    return main_string