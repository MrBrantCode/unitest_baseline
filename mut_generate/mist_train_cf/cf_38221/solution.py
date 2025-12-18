"""
QUESTION:
Write a function `extract_metadata` that takes a string containing a PHP script as input and returns a dictionary containing the extracted metadata information from the comment block. The function should be able to handle various formats of the comment block and extract the metadata accurately. The comment block is formatted as follows:

/**
 * @author     <NAME> <<EMAIL>>
 * @copyright  <YEARS> <COPYRIGHT_INFO>
 * @license    <LICENSE_URL> <LICENSE_NAME>
 * @version    <VERSION_NUMBER>
 * @link       <LINK_URL>
 * @notes      <ADDITIONAL_NOTES>
 */

The output dictionary should contain the extracted metadata with the following keys: author, copyright, license, version, link, and notes.
"""

import re

def extract_metadata(php_script):
    metadata = {}
    comment_block = re.search(r'/\*\*(.*?)\*/', php_script, re.DOTALL)
    if comment_block:
        metadata_lines = comment_block.group(1).strip().split('\n')
        for line in metadata_lines:
            match = re.match(r'\s*\*\s*@(\w+)\s+(.*)', line)
            if match:
                key, value = match.group(1), match.group(2)
                metadata[key] = value.strip()
    return metadata