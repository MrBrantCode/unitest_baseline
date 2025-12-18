"""
QUESTION:
Create a function called `distributeInheritance` in a smart contract that executes a complex estate plan. The function should take into account multiple beneficiaries and their proportion of inheritance. The function should also trigger the execution of the estate based on an oracle service verifying the status of the testator, and distribute the estate's balance among the beneficiaries according to their share percentages. The function should be part of a contract where the testator is the one who adds beneficiaries and their corresponding share percentages, and the beneficiaries can withdraw their inheritance after the testator's death. The function should be private and only accessible internally by the contract.
"""

def distributeInheritance(beneficiaries, totalBalance):
    """
    This function distributes the total balance among beneficiaries based on their share percentages.

    Args:
    beneficiaries (list): A list of dictionaries containing beneficiary's address and percentage.
    totalBalance (float): The total balance to be distributed.

    Returns:
    dict: A dictionary containing the inheritance amount for each beneficiary.
    """
    
    inheritance = {}
    
    for beneficiary in beneficiaries:
        inheritanceShare = (totalBalance * beneficiary['percentage']) / 100
        inheritance[beneficiary['address']] = inheritanceShare
    
    return inheritance