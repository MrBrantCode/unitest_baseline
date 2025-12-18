"""
QUESTION:
Write a function `generateDeploymentScript` that generates a deployment script as a string based on the provided base directory. The function should take the base directory as a string input and return a script that stops all services, checks out and deploys the latest code, starts all services, and prints a message indicating that CORDA and Webservers are up and running. The commands in the script should be executed in the specified order and reference the base directory using the `$BASEDIR` variable. The function should not execute the script, only generate it as a string.
"""

def generate_deployment_script(base_dir: str) -> str:
    deployment_script = f"{base_dir}/stopAll.sh\n"
    deployment_script += f"{base_dir}/checkoutAndDeployNode.sh\n"
    deployment_script += f"{base_dir}/startAll.sh\n"
    deployment_script += "echo \"---------------------------------------\"\n"
    deployment_script += "echo \"CORDA and Webservers are UP and running\"\n"
    deployment_script += "echo \"---------------------------------------\"\n"
    return deployment_script