"""
QUESTION:
Write a function `configure_model` that takes three dictionaries as input: `auxiliary_head`, `test_cfg`, and `optimizer`. The function should return two dictionaries: `model_config` and `optimizer_config`. 

`auxiliary_head` dictionary contains the number of classes for the auxiliary head of the model, `test_cfg` dictionary specifies the testing configuration, and `optimizer` dictionary specifies the type of optimizer, learning rate, momentum, and weight decay.

`model_config` should contain the number of classes and testing configuration, and `optimizer_config` should contain the type, learning rate, momentum, and weight decay.
"""

def configure_model(auxiliary_head, test_cfg, optimizer):
    model_config = {
        'num_classes': auxiliary_head['num_classes'],
        'test_cfg': test_cfg
    }
    
    optimizer_config = {
        'type': optimizer['type'],
        'lr': optimizer['lr'],
        'momentum': optimizer['momentum'],
        'weight_decay': optimizer['weight_decay']
    }
    
    return model_config, optimizer_config