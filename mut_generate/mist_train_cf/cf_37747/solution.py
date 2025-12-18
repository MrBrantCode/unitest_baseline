"""
QUESTION:
Write a function `constructFunction` that takes four parameters: `decl_code`, `function_code`, `catch_code`, and `return_code`. The function should return a string representing a complete C++ function constructed by replacing placeholders with the given code snippets. The C++ function format should be as follows:
```
<decl_code>
{
    /* inline code */
    <function_code>
    /*I would like to fill in changed locals and globals here...*/
}
catch(...)
{
    <catch_code>
}
<return_code>
```
"""

def constructFunction(decl_code, function_code, catch_code, return_code):
    complete_function = f"{decl_code}\n{{\n    /* inline code */\n    {function_code}\n    /*I would like to fill in changed locals and globals here...*/\n}}\ncatch(...)\n{{\n    {catch_code}\n}}\n{return_code}"
    return complete_function