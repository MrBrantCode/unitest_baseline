"""
QUESTION:
Create a `JobSchema` class with attributes `schema_name` and `schema_fields` and methods `__init__` and `validate`. The `__init__` method should initialize `schema_name` and `schema_fields`, and the `validate` method should check if the given dictionary data conforms to the schema defined by `schema_fields`. 

Additionally, create two subclasses `ExpectationSweepJobContextSchema` and `JobProgressSchema` that inherit from `JobSchema`. `ExpectationSweepJobContextSchema` should have an additional attribute `context_type` and `JobProgressSchema` should have an additional attribute `progress_status`. The `__init__` method of each subclass should initialize the attributes of the subclass and call the `__init__` method of the `JobSchema` class.
"""

def job_schema(schema_name, schema_fields):
    def validate(data):
        return all(field in data for field in schema_fields)
    return {'schema_name': schema_name, 'schema_fields': schema_fields, 'validate': validate}


def expectation_sweep_job_context_schema(schema_name, schema_fields, context_type):
    schema = job_schema(schema_name, schema_fields)
    schema['context_type'] = context_type
    return schema


def job_progress_schema(schema_name, schema_fields, progress_status):
    schema = job_schema(schema_name, schema_fields)
    schema['progress_status'] = progress_status
    return schema