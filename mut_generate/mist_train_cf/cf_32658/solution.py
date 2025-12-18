"""
QUESTION:
Create a function `generate_prediction_query` that takes in three parameters: `prediction_query` (a string representing the BQML prediction query), `enable_logging` (a boolean indicating whether logging and error monitoring should be enabled), and `error_table_schema` (a string representing the schema for the error table in BigQuery). The function should return the complete BQML prediction query along with the logging setup if enabled. If logging is enabled, the function should include the logging setup in the output with the specified error table schema.
"""

def generate_prediction_query(prediction_query: str, enable_logging: bool, error_table_schema: str) -> str:
    if enable_logging:
        logging_setup = f"\n\n# Options for logging & error monitoring\n# LOGGING: Create BQ Table for logs with schema as follows -\n# {error_table_schema}\nENABLE_BQ_LOGGING = True"
        return prediction_query + logging_setup
    else:
        return prediction_query + "\nENABLE_BQ_LOGGING = False"