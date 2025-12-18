"""
QUESTION:
Implement the `get_context_key_references` function, which takes a `pipeline_id` and a set of `context_key_references` as input. The function should return a set of context key references that are present in the pipeline configuration for the given `pipeline_id`. The pipeline configuration is assumed to be a dictionary mapping pipeline IDs to their configurations. Context key references are denoted by the `${}` syntax.
"""

def get_context_key_references(pipeline_id, context_key_references):
    pipeline_config = pipeline_configurations.get(pipeline_id, {})
    
    pipeline_context_keys = set()
    for key, value in pipeline_config.items():
        if isinstance(value, str) and value.startswith("${") and value.endswith("}"):
            pipeline_context_keys.add(value)
    
    references_in_config = context_key_references.intersection(pipeline_context_keys)
    return references_in_config