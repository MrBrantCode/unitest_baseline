"""
QUESTION:
Implement the function `generate_optimizer_file_name(model_name, accuracy, model_dir)` that takes in a model name (a string), accuracy (a float), and model directory path (a string) and returns a unique file name in the format `{model_name}{accuracy:.4f}_optims.pth`.
"""

def generate_optimizer_file_name(model_name, accuracy, model_dir):
    return os.path.join(model_dir, f"{model_name}{accuracy:.4f}_optims.pth")