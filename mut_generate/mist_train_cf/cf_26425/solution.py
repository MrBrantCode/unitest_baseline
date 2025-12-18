"""
QUESTION:
Create a function named `extract_emr_studio_config` that takes a string representing a CloudFormation template and returns a dictionary containing the EMR Studio configuration details. The function should extract the following information from the template:
- Authentication mode used for the EMR Studio (`auth_mode`)
- Default S3 location for the EMR Studio (`default_s3_location`)
- Engine security group ID associated with the EMR Studio (`engine_security_group_id`)
- Name of the EMR Studio (`name`)
- Service role ARN used for the EMR Studio (`service_role`)

The function should be able to parse the template and extract the required information even if the template contains multiple resources and properties. The extracted information should be returned as a dictionary with the corresponding keys.
"""

import re

def extract_emr_studio_config(template: str) -> dict:
    emr_studio_config = {}

    # Extracting auth_mode
    auth_mode_match = re.search(r'auth_mode\s*=\s*["\']([^"\']+)["\']', template)
    if auth_mode_match:
        emr_studio_config["auth_mode"] = auth_mode_match.group(1)

    # Extracting default_s3_location
    default_s3_location_match = re.search(r'default_s3_location\s*=\s*["\']([^"\']+)["\']', template)
    if default_s3_location_match:
        emr_studio_config["default_s3_location"] = default_s3_location_match.group(1)

    # Extracting engine_security_group_id
    engine_security_group_id_match = re.search(r'engine_security_group_id\s*=\s*["\']([^"\']+)["\']', template)
    if engine_security_group_id_match:
        emr_studio_config["engine_security_group_id"] = engine_security_group_id_match.group(1)

    # Extracting name
    name_match = re.search(r'name\s*=\s*["\']([^"\']+)["\']', template)
    if name_match:
        emr_studio_config["name"] = name_match.group(1)

    # Extracting service_role
    service_role_match = re.search(r'service_role\s*=\s*["\']([^"\']+)["\']', template)
    if service_role_match:
        emr_studio_config["service_role"] = service_role_match.group(1)

    return emr_studio_config