"""
QUESTION:
Create a function `copy_deformer_weights` that takes four inputs: `source_object`, `source_deformer`, `target_object`, and `target_deformer`. The function should copy the weight map from `source_deformer` to `target_deformer`. 

The function should verify that `source_deformer` exists on `source_object` and `target_deformer` exists on `target_object` before attempting to copy the weight map. If either deformer is missing, the function should print an error message and return without copying the weight map. 

The function should also handle any potential errors that occur during the weight map copying process and print an error message if an exception occurs.
"""

def copy_deformer_weights(source_object, source_deformer, target_object, target_deformer):
    # Verify that the source and target deformers exist on their respective objects
    if source_deformer not in source_object.deformers:
        print(f"Error: Source deformer '{source_deformer}' not found on source object '{source_object}'.")
        return
    if target_deformer not in target_object.deformers:
        print(f"Error: Target deformer '{target_deformer}' not found on target object '{target_object}'.")
        return

    # Copy the weight map from the source deformer to the target deformer
    try:
        target_deformer.weight_map = source_deformer.weight_map
        print(f"Weight map copied successfully from '{source_deformer}' to '{target_deformer}'.")
    except Exception as e:
        print(f"Error occurred while copying weight map: {e}")