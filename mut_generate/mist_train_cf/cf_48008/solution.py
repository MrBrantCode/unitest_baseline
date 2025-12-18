"""
QUESTION:
Design a function `is_semver(version)` that checks if a given string `version` is a valid Semantic Versioning number according to the Semantic Versioning specification. A valid Semantic Versioning number consists of three parts (major, minor, and patch) separated by periods, where each part is a non-negative integer without leading zeros. The string may also include an optional prerelease identifier (separated by a hyphen) and/or an optional build metadata (separated by a plus), each consisting of alphanumeric characters and hyphens, but not all numeric and without leading zeros.
"""

import re

def is_semver(version):
    pattern = r'^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(-(0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(\.(0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*)?(\+[0-9a-zA-Z-]+(\.[0-9a-zA-Z-]+)*)?$'
    return bool(re.match(pattern, version))