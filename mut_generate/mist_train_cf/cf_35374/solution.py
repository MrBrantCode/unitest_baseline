"""
QUESTION:
Implement an initializer method for a `VelocityController` class that accepts `sigma` (default 0.0), `v_des` (default 0.0), `a_max` (default 1.0), `k_p` (default 2.0), and additional keyword arguments. The initializer method should set the corresponding attributes of the class instance for the given parameters and any additional keyword arguments.
"""

def VelocityController(sigma=0.0, v_des=0.0, a_max=1.0, k_p=2.0, **kwargs):
    return {
        'sigma': sigma,
        'v_des': v_des,
        'a_max': a_max,
        'k_p': k_p,
        **kwargs
    }