"""
QUESTION:
Write a function 'configure_dockerfile' that generates a Dockerfile with the following specifications: it installs a specific version of a software package from a non-standard source, configures it to run as a service in the background, and exposes any necessary ports.
"""

def configure_dockerfile(package_name, package_version, repository_url, repository_key_url, port):
    """
    Generates a Dockerfile that installs a specific version of a software package 
    from a non-standard source, configures it to run as a service in the background, 
    and exposes any necessary ports.

    Args:
        package_name (str): The name of the software package.
        package_version (str): The version of the software package.
        repository_url (str): The URL of the repository for the software package.
        repository_key_url (str): The URL of the repository key for the software package.
        port (int): The port to expose.

    Returns:
        str: The content of the Dockerfile.
    """

    dockerfile_content = f"""
    FROM ubuntu:latest

    # Install dependencies
    RUN apt-get update && apt-get install -y \
        curl \
        software-properties-common

    # Add repository for software package
    RUN curl -fsSL {repository_key_url} | apt-key add -
    RUN add-apt-repository "deb [arch=amd64] {repository_url} $(lsb_release -cs) main"

    # Install specific version of software package
    RUN apt-get update && apt-get install -y \
        {package_name}={package_version}

    # Configure software package to run as a service
    RUN systemctl enable {package_name}.service

    # Start software package service
    CMD ["systemctl", "start", "{package_name}.service"]

    # Expose any necessary ports
    EXPOSE {port}
    """

    return dockerfile_content