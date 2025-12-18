"""
QUESTION:
Implement a function `parse_job_step` that takes a dictionary `res_body` as input and returns a new dictionary containing the extracted information. The input dictionary `res_body` contains details about a job step, including its name, ID, type, action on failure, properties, and status. The function should extract the relevant information from the `res_body` dictionary and return a new dictionary with the specified keys: 'name', 'id', 'type', 'actionOnFailure', 'jarPath', 'jobType', 'inputPath', and 'outputPath'. 

The 'jarPath', 'jobType', 'inputPath', and 'outputPath' should be extracted from the 'properties' key in the `res_body` dictionary, where 'inputPath' and 'outputPath' are contained in the 'inputOutputPaths' value separated by ', '. If any key is missing in the `res_body` dictionary or its 'properties', the function should return an empty string for the corresponding key in the output dictionary.
"""

def parse_job_step(res_body):
    properties = res_body.get('properties', {})
    jar_path = properties.get('jarPath', '')
    job_type = properties.get('jobType', '')

    # Check if 'inputOutputPaths' exists before splitting
    input_output_paths = properties.get('inputOutputPaths', '')
    if input_output_paths:
        input_path, output_path = input_output_paths.split(', ')
    else:
        input_path = ''
        output_path = ''

    parsed_info = {
        'name': res_body.get('name', ''),
        'id': res_body.get('id', ''),
        'type': res_body.get('type', ''),
        'actionOnFailure': res_body.get('actionOnFailure', ''),
        'jarPath': jar_path,
        'jobType': job_type,
        'inputPath': input_path,
        'outputPath': output_path
    }

    return parsed_info