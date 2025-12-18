"""
QUESTION:
Implement the function `extract_text_patterns(text)` that takes a string `text` as input and returns a dictionary containing the extracted patterns. The dictionary should have the keys "block_quotes", "code_spans", and "math_expressions" representing the corresponding patterns found in the text. Use the following regular expressions to identify and extract the patterns:
- `^bq\.\s.+` for block quotes
- ``[^`]*` ` for code spans
- `\\[\(\[].*?\\[\)\]]` for mathematical expressions

Restrictions:
- Remove the backticks from the code spans before returning the dictionary.
"""

import re

def extract_text_patterns(text):
    reTextileQuot  = re.compile(r'^bq\.\s.+')
    reMkdCodeSpans = re.compile('`[^`]*`')
    reMkdMathSpans = re.compile(r'\\[\(\[].*?\\[\)\]]')
    
    block_quotes = reTextileQuot.findall(text)
    code_spans = [span[1:-1] for span in reMkdCodeSpans.findall(text)]
    math_expressions = reMkdMathSpans.findall(text)
    
    return {
        "block_quotes": block_quotes,
        "code_spans": code_spans,
        "math_expressions": math_expressions
    }