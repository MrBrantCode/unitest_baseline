"""
QUESTION:
Write a function `import_azure_resource_group` that imports an existing Azure Resource Group into Terraform state. The function should take two parameters: `terraform_resource_name` and `azure_resource_id`. The function should construct the `terraform import` command string using the provided parameters and return this string.

Restrictions:
- The function should not execute the `terraform import` command, only construct the command string.
- The function should not take any other parameters besides `terraform_resource_name` and `azure_resource_id`.
"""

def import_azure_resource_group(terraform_resource_name, azure_resource_id):
    """
    Construct the terraform import command string to import an existing Azure Resource Group into Terraform state.

    Args:
        terraform_resource_name (str): The Terraform name of the resource group.
        azure_resource_id (str): The Azure ID of the existing resource group.

    Returns:
        str: The constructed terraform import command string.
    """
    return f"terraform import azurerm_resource_group.{terraform_resource_name} {azure_resource_id}"