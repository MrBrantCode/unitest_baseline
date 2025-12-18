"""
QUESTION:
Create a function named `add_qa` that takes three parameters: `my_list`, `qn`, and `ans`, where `my_list` is a list of dictionaries with keys "Qn" and "Ans", `qn` is a string representing a question, and `ans` is a string representing an answer. The function should insert a new dictionary with keys "Qn" and "Ans" and corresponding values `qn` and `ans` at the beginning of `my_list`, but only if `ans` is not already a value for the key "Ans" in any dictionary in `my_list`. If `ans` already exists, the function should return an error message.
"""

def add_qa(my_list, qn, ans):
    if any(dic.get('Ans') == ans for dic in my_list):
        return "Error: Answer already exists in the list"
    
    my_list.insert(0, {"Qn": qn, "Ans": ans})
    
    return "Successfully added question and answer to list"