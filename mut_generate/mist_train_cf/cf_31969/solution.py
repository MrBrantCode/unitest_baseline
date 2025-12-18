"""
QUESTION:
Implement the `call` method with the following parameters: `ret_type`, `func_id`, `types`, and `*args`. The method should check if the number of argument types (`types` string length) matches the number of arguments provided (`args` length). If there is a mismatch, print "Wrong number of args/type" and return 0. Otherwise, return `func_id`.
"""

def call(ret_type, func_id, types="", *args):
    if len(types) != len(args):
        print("Wrong number of args/type")
        return 0
    return func_id