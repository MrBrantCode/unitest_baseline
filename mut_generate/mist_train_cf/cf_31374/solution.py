"""
QUESTION:
Implement a function `monkey_patch_dataset_computation` that takes a `tf_computation` as input, monkey patches its `result` type by setting `is_sequence` to `True` and returns the patched `tf_computation`. Ensure the original state is restored after the patch is applied, by setting `is_sequence` back to `False` when the function execution is complete. The function must handle the restoration of the original state even if exceptions occur.
"""

def monkey_patch_dataset_computation(tf_computation):
    original_is_sequence = tf_computation.type_signature.result.is_sequence
    try:
        # Monkey-patch tf_computation's result type.
        tf_computation.type_signature.result.is_sequence = lambda: True
        return tf_computation
    finally:
        # Monkey-unpatch tf_computation's result type.
        tf_computation.type_signature.result.is_sequence = original_is_sequence