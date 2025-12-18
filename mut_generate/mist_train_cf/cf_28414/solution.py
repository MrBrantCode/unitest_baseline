"""
QUESTION:
Write a function `parse_instruction_tests` that takes a code snippet as input and returns a list of dictionaries. Each dictionary represents the parsed information for a test case and contains the keys: `mnemonic`, `operand1`, `operand2`, `operand3`, `operand4`, `lock`, `rounding_mode`, `merge_mode`, `sae`, `mask`, and `broadcast`. The function should use regular expressions to extract the required information from the code snippet. The input code snippet is in the format of x86 assembly language test cases.
"""

from typing import List, Dict, Union
import re

def parse_instruction_tests(code_snippet: str) -> List[Dict[str, Union[str, bool, None]]]:
    test_cases = re.findall(r'fn\s+(\w+)\(\)\s*{\s*run_test\(&Instruction\s*{\s*mnemonic:\s*Mnemonic::(\w+),\s*operand1:\s*Some\(([^)]*)\),\s*operand2:\s*Some\(([^)]*)\),\s*operand3:\s*Some\(([^)]*)\),\s*operand4:\s*([^,]*),\s*lock:\s*(true|false),\s*rounding_mode:\s*([^,]*),\s*merge_mode:\s*Some\(MergeMode::(\w+)\),\s*sae:\s*(true|false),\s*mask:\s*Some\(MaskReg::(\w+)\),\s*broadcast:\s*([^)]*)\s*},\s*&\[\d+,\s*\d+,\s*\d+,\s*\d+,\s*\d+,\s*\d+,\s*\d+\],\s*OperandSize::(\w+)\)\s*}', code_snippet)

    parsed_tests = []
    for test_case in test_cases:
        parsed_test = {
            'mnemonic': test_case[1],
            'operand1': test_case[2],
            'operand2': test_case[3],
            'operand3': test_case[4],
            'operand4': test_case[5],
            'lock': True if test_case[6] == 'true' else False,
            'rounding_mode': test_case[7],
            'merge_mode': test_case[8],
            'sae': True if test_case[9] == 'true' else False,
            'mask': test_case[10],
            'broadcast': test_case[11],
            'operand_size': test_case[12]
        }
        parsed_tests.append(parsed_test)

    return parsed_tests