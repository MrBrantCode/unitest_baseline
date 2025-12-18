"""
QUESTION:
Implement a function `process_config_model` that takes a configuration model `cfg` as input and returns a dictionary containing the number of layers, learning rate, and optimizer type extracted from the configuration model. The dictionary should have keys "num_layers", "learning_rate", and "optimizer_type". Assume that the `Cfg` class has the necessary attributes and methods to retrieve the required information, including `get_num_layers()`, `get_learning_rate()`, and `get_optimizer_type()`.
"""

def process_config_model(cfg):
    return {
        "num_layers": cfg.get_num_layers(),
        "learning_rate": cfg.get_learning_rate(),
        "optimizer_type": cfg.get_optimizer_type()
    }