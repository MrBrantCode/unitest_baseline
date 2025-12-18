"""
QUESTION:
Write a function `generate_cuda_installation_script` that takes a string `cuda_version` in the format "X.Y" as input and returns a string containing the necessary shell commands to install and configure CUDA on a Linux system. The function should handle the installation of CUDA compiler, libraries, drivers, cuDNN, and symbolic linking of CUDA directories.
"""

def generate_cuda_installation_script(cuda_version):
    cuda_version_dashed = cuda_version.replace(".", "-")
    installation_script = f"sudo apt-get install -y --no-install-recommends cuda-compiler-{cuda_version_dashed} cuda-libraries-dev-{cuda_version_dashed} cuda-driver-dev-{cuda_version_dashed} cuda-cudart-dev-{cuda_version_dashed}\n"
    installation_script += "sudo apt-get install -y --no-install-recommends libcudnn8-dev\n"
    installation_script += "sudo rm -rf /usr/local/cuda\n"
    installation_script += f"sudo ln -s /usr/local/cuda-{cuda_version} /usr/local/cuda\n"
    return installation_script