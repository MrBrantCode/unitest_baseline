"""
QUESTION:
Write a function `analyze_license(license_text)` that takes a string `license_text` as input and returns a dictionary containing two keys: "permissions" and "limitations". The value for each key should be a list of strings, where each string represents a permission or limitation extracted from the license text. 

Permissions are denoted by the phrase "distributed under the License" and are followed by a specific language governing permissions. Limitations are denoted by the phrase "WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND" and are followed by either "either express or implied". The extracted permission or limitation should be the text between these phrases, and the returned dictionary should have these extracted texts as values for the corresponding keys.
"""

import re

def analyze_license(license_text):
    permissions = re.findall(r'distributed under the License(.*?)governing permissions', license_text, re.DOTALL)
    limitations = re.findall(r'WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND(.*?)either express or implied', license_text, re.DOTALL)
    
    permissions = [permission.strip() for permission in permissions]
    limitations = [limitation.strip() for limitation in limitations]
    
    return {"permissions": permissions, "limitations": limitations}