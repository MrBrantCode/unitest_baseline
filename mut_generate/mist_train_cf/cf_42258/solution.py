"""
QUESTION:
Implement a function `process_alarms` that takes a dictionary `metric_data` as input, where keys are endpoint names and values are the corresponding metric values, and returns a list of triggered alarm names. The function should evaluate the metric values against the alarm parameters defined in `self.params` and consider the following rules: 

- For each alarm, check if any of its specified endpoints have metric values that satisfy the threshold condition within the specified evaluation period. 
- If the condition is satisfied for a particular endpoint, add the alarm name to the list of triggered alarms. 

The alarm parameters are defined as a dictionary where each key represents the alarm name and the corresponding value is a dictionary containing 'endpoints', 'threshold', and 'period'. 

Restrictions:
- The 'threshold' value is a string representing the threshold condition for triggering the alarm (e.g., '>10', '<5', '==100').
- The 'period' value is a string representing the evaluation period in the format 'NxM', where N is the number of periods and M is the period duration in seconds.
- The 'metric_data' dictionary will only contain keys that are present in the 'self.params' and 'self.app_region.alarm_endpoints' dictionaries.
"""

from typing import Dict, List

def process_alarms(params: Dict[str, Dict[str, str]], metric_data: Dict[str, float]) -> List[str]:
    """
    Evaluate metric values against alarm parameters and return a list of triggered alarm names.

    Args:
        params (Dict[str, Dict[str, str]]): A dictionary of alarm parameters where each key represents the alarm name
            and the corresponding value is a dictionary containing 'endpoints', 'threshold', and 'period'.
        metric_data (Dict[str, float]): A dictionary where keys are endpoint names and values are the corresponding metric values.

    Returns:
        List[str]: A list of triggered alarm names.
    """
    triggered_alarms = []
    for alarm_name, alarm_info in params.items():
        for endpoint in alarm_info['endpoints']:
            if endpoint in metric_data:
                operator = alarm_info['threshold'][0]
                threshold = float(alarm_info['threshold'][1:])
                if (operator == '>' and metric_data[endpoint] > threshold) or \
                   (operator == '<' and metric_data[endpoint] < threshold) or \
                   (operator == '=' and metric_data[endpoint] == threshold):
                    triggered_alarms.append(alarm_name)
                    break
    return triggered_alarms