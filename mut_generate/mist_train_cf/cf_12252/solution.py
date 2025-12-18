"""
QUESTION:
Implement a function named `test_turing_machine` that evaluates a Turing machine's functionality and identifies potential limitations or issues. The function should accept a Turing machine object and a set of test cases as input. The Turing machine object should have methods to execute the machine, check for halting, and verify correctness. The function should return a report detailing the test results, including any discrepancies, errors, or unexpected behavior.
"""

def test_turing_machine(turing_machine, test_cases):
    """
    Evaluates a Turing machine's functionality and identifies potential limitations or issues.

    Args:
        turing_machine (TuringMachine): A Turing machine object with methods to execute, check for halting, and verify correctness.
        test_cases (list): A set of test cases to evaluate the Turing machine.

    Returns:
        dict: A report detailing the test results, including any discrepancies, errors, or unexpected behavior.
    """
    report = {}
    
    for test_case in test_cases:
        try:
            # Execute the Turing machine
            result = turing_machine.execute(test_case)
            
            # Check for halting
            if not turing_machine.is_halted():
                report[test_case] = "Error: Turing machine did not halt."
                continue
            
            # Verify correctness
            if not turing_machine.is_correct(result):
                report[test_case] = "Error: Turing machine produced incorrect output."
            else:
                report[test_case] = "Success"
        
        except Exception as e:
            report[test_case] = f"Error: {str(e)}"
    
    return report