"""
QUESTION:
Write a function `find_decay_chain(config_str, particle_name)` that takes a configuration string `config_str` and a `particle_name` as input. The configuration string represents a decay chain of particles and their decay products in YAML format, where each particle is a key and its decay products are listed as values. The function should return the decay chain for the given particle, including the particle itself and all its decay products, along with their subsequent decay products, and so on. Assume the input configuration string is well-formed and follows the specified YAML format.
"""

from typing import List

def find_decay_chain(config_str: str, particle_name: str) -> List[str]:
    config_dict = {}
    exec(config_str, {}, config_dict)  

    decay_dict = config_dict['decay']
    decay_chain = []

    def traverse_decay(particle):
        decay_chain.append(particle)
        if particle in decay_dict:
            for decay_product in decay_dict[particle]:
                traverse_decay(decay_product[1])

    traverse_decay(particle_name)
    return decay_chain