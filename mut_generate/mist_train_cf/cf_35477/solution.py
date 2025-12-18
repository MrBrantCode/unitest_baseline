"""
QUESTION:
Write a function `validate_stream_payload` that takes a JSON payload as input. The function should assert the presence of certain keys and their corresponding values within the JSON payload and handle any potential errors that may occur during the validation process. 

The function should validate the following conditions: 
- The payload contains a key "streams" which is a list with at least one element.
- The first element of "streams" contains a key "stream" which is a dictionary.
- The "stream" dictionary contains the keys "test", "chaostoolkit_lib_version", "chaostoolkit_run_trace_id", "chaostoolkit_experiment_ref", "One", and "source".
- The value of "test" key in the "stream" dictionary is "yes".
- The "source" key in the "stream" dictionary is "chaostoolkit".

If any of the assertions fail, the function should raise a `ValidationException` with an appropriate error message. If the payload is valid, the function should return True.
"""

class ValidationException(Exception):
    pass

def validate_stream_payload(payload):
    try:
        assert "streams" in payload and isinstance(payload["streams"], list) and len(payload["streams"]) > 0, "Invalid 'streams' key or value"
        stream = payload["streams"][0].get("stream", {})
        assert isinstance(stream, dict) and all(key in stream for key in ["test", "chaostoolkit_lib_version", "chaostoolkit_run_trace_id", "chaostoolkit_experiment_ref", "One", "source"]), "Invalid 'stream' dictionary or missing keys"
        assert stream["test"] == "yes", "Invalid value for 'test' key"
        assert stream["source"] == "chaostoolkit", "Invalid value for 'source' key"
        return True
    except AssertionError as e:
        raise ValidationException(str(e))