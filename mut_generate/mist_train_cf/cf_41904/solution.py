"""
QUESTION:
Write a Python function `generate_cmake_command` that takes six parameters: three boolean values `WITH_MKL`, `WITH_GPU`, `USE_TENSORRT`, and three string values `LIB_DIR`, `CUDNN_LIB`, `CUDA_LIB`. The function returns a CMake command as a string based on the given parameters. The command should include flags `-DPADDLE_LIB`, `-DWITH_MKL`, `-DWITH_GPU`, `-DWITH_STATIC_LIB=OFF`, and `-DTENSORRT_ROOT` if `USE_TENSORRT` is `True`.
"""

def generate_cmake_command(WITH_MKL: bool, WITH_GPU: bool, USE_TENSORRT: bool, LIB_DIR: str, CUDNN_LIB: str, CUDA_LIB: str) -> str:
    cmake_command = "cmake .. -DPADDLE_LIB={} -DWITH_MKL={} -DWITH_GPU={} -DWITH_STATIC_LIB=OFF".format(LIB_DIR, "ON" if WITH_MKL else "OFF", "ON" if WITH_GPU else "OFF")

    if USE_TENSORRT:
        cmake_command += " -DTENSORRT_ROOT=/paddle/nvidia-downloads/TensorRT-6.0.1.5"

    return cmake_command