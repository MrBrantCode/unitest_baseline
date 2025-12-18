"""
QUESTION:
Create a function called `get_proxy_verification_args` that generates the required arguments for verifying a TransparentUpgradeableProxy contract on Etherscan. The function should take in the contract address, proxy admin address, and salt as inputs, and return the correct arguments in the format required for verification. The function should assume that the TransparentUpgradeableProxy contract has fixed code that is OpenZeppelin code and that the bytecode provided needs to match exactly with the "runtime bytecode" that exists on-chain. 

The function should not take into account the contract's version or the version of `@openzeppelin/contracts` being used. The function's output should be a string in the format of `"<CONTRACT ADDR>","<PROXY ADMIN ADDR>","<SALT IN HEX>"`.
"""

def get_proxy_verification_args(contract_address, proxy_admin_address, salt):
    """
    Generates the required arguments for verifying a TransparentUpgradeableProxy contract on Etherscan.

    Args:
        contract_address (str): The address of the contract.
        proxy_admin_address (str): The address of the proxy admin.
        salt (str): The salt used when deploying the contract.

    Returns:
        str: The verification arguments in the format required for verification.
    """
    return f'"{contract_address}","{proxy_admin_address}","{salt}"'