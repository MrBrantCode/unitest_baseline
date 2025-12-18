"""
QUESTION:
Create a function named `process_text_explanations` that takes a list of text-based SHAP values and a label index, parses the text SHAP values, filters them based on the specified label index, and returns a dictionary of explanations sorted in descending order of importance.

The function should accept two parameters: `text_shap_values` (a list of strings representing text-based SHAP values in the format "word: SHAP value") and `label_index` (an integer specifying the index of the label to explain). The function should return a dictionary where the keys are words and the values are their corresponding SHAP values.

The function should not filter out any words based on the label index in the current code, since it incorrectly assumes the word to be filtered is of the format `word{label_index + 1}`. The correct implementation should consider all words in the text_shap_values regardless of the label_index, since SHAP values do not have a specific format that relates to the label_index. 

The correct function signature is:
```python
def process_text_explanations(text_shap_values: List[str], label_index: int) -> Dict[str, float]:
```
"""

from typing import List, Dict

def process_text_explanations(text_shap_values: List[str], label_index: int) -> Dict[str, float]:
    # Parse text SHAP values
    text_exp = {
        k: float(v)
        for k, v in (exp.split(": ") for exp in text_shap_values)
    }

    # Sort explanations in descending order of importance
    sorted_exp = dict(sorted(text_exp.items(), key=lambda item: item[1], reverse=True))

    return sorted_exp