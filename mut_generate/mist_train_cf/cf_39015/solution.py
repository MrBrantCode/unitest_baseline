"""
QUESTION:
Implement the `TrainRequest` class that inherits from the `Request`, `DocsPropertyMixin`, and `GroundtruthPropertyMixin` classes. The `TrainRequest` class should have an `__init__` method that takes in three parameters: `request_data`, `docs_data`, and `groundtruth_data`. The `Request` mixin provides basic request functionality with a single parameter `request_data`, the `DocsPropertyMixin` mixin provides documentation properties with a single parameter `docs_data`, and the `GroundtruthPropertyMixin` mixin provides ground truth data properties with a single parameter `groundtruth_data`.
"""

def TrainRequest(request_data, docs_data, groundtruth_data):
    request = type('Request', (), {'request_data': request_data})
    docs_property = type('DocsPropertyMixin', (), {'docs_data': docs_data})
    groundtruth_property = type('GroundtruthPropertyMixin', (), {'groundtruth_data': groundtruth_data})
    train_request = type('TrainRequest', (request.__class__, docs_property.__class__, groundtruth_property.__class__), {})
    return train_request()