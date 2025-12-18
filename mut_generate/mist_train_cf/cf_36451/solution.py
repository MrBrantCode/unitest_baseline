"""
QUESTION:
Implement the function `process_receivers(models, signal_name)` that takes a dictionary `models` and a `signal_name` as input. The `models` dictionary has string keys representing models, with corresponding values being dictionaries containing signal names as keys and lists of receiver function dictionaries as values. Each receiver function dictionary has keys `name`, `module`, and `line` for the name of the receiver function, its module, and line number, respectively. Return a list of formatted strings containing the details of receiver functions for the given `signal_name` in the format: "Receiver: {name}, Module: {module}, Line: {line}". Handle the cases where the `models` dictionary is empty or the `signal_name` is not found in any model or has no receivers.
"""

def process_receivers(models, signal_name):
    result = []
    for model in models.values():
        if signal_name in model:
            for receiver in model[signal_name]:
                result.append("Receiver: {name}, Module: {module}, Line: {line}".format(
                    name=receiver['name'],
                    module=receiver['module'],
                    line=receiver['line']
                ))
    return result