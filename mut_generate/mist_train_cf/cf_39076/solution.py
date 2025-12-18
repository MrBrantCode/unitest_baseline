"""
QUESTION:
Implement the `processFlagActions` function to process a list of flag action properties and perform specific operations based on the provided actions. The function should take a list of dictionaries as input, where each dictionary contains an "action" key and additional properties specific to that action. The possible actions are "enable_feature", "disable_feature", and "set_threshold". The function should return a dictionary with the outcomes of the operations.

The function signature is `def processFlagActions(flagActions: List[Dict[str, Union[str, int]]]) -> Dict[str, Union[str, int]]`. The input list contains dictionaries with the following possible structures:
- {"action": "enable_feature", "feature_name": str}
- {"action": "disable_feature", "feature_name": str}
- {"action": "set_threshold", "threshold_value": int}
"""

from typing import List, Dict, Union

def processFlagActions(flagActions: List[Dict[str, Union[str, int]]]) -> Dict[str, Union[str, int]]:
    result = {}
    for action_property in flagActions:
        action = action_property.get("action")
        if action == "enable_feature":
            feature_name = action_property.get("feature_name")
            result[feature_name] = "enabled"
        elif action == "disable_feature":
            feature_name = action_property.get("feature_name")
            result[feature_name] = "disabled"
        elif action == "set_threshold":
            threshold_value = action_property.get("threshold_value")
            result["threshold"] = threshold_value
    return result