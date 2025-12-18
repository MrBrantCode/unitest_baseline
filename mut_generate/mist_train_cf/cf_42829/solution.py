"""
QUESTION:
Implement the `build_config` method of a class that generates configuration commands for a network device. The method takes four parameters: `apply`, `attributes`, `unconfig`, and `**kwargs`. If `apply` is `True`, construct configuration commands based on the provided `attributes` and `**kwargs`. If `unconfig` is `True`, construct commands to unapply the configuration. The `attributes` parameter should be used to format attribute values. 

`apply`: a boolean indicating whether the configuration should be applied (default is `True`). 
`attributes`: a dictionary containing attributes for the configuration.
`unconfig`: a boolean indicating whether the configuration should be unapplied (default is `False`).
`**kwargs`: additional keyword arguments that may be provided. 

The method should return a list of configuration commands if `apply` is `True` and a message if `apply` is `False`.
"""

def build_config(apply=True, attributes=None, unconfig=False, **kwargs):
    '''Interface build config'''
    if apply:
        assert attributes is not None, "Attributes must be provided for configuration"

        # Extracting attribute values
        interface_name = attributes.get('interface_name')
        enable_default_bw = attributes.get('enable_default_bw')

        configurations = []

        if unconfig:
            configurations.append(f'no interface {interface_name}')
        else:
            configurations.append(f'interface {interface_name}')

            if enable_default_bw:
                configurations.append('ip rsvp bandwidth')

        # Additional keyword arguments processing
        for key, value in kwargs.items():
            configurations.append(f'{key} {value}')

        return configurations
    else:
        return "Configuration not applied"