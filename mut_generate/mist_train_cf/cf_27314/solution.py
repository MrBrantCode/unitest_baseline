"""
QUESTION:
Implement a `generate_usernames` function that generates a list of potential usernames. The function should take `region`, `number`, `min_len`, `prefix`, and `suffix` as parameters, along with `config` and `deity` attributes of the class instance. It must use `config.generator.get_prospects` to obtain a list of prospects based on `input_words=[deity, region]`, `number`, and `min_len`. The function should then return a list of usernames by appending `prefix` and `suffix` to each prospect. The `prefix` and `suffix` parameters are optional and default to empty strings.
"""

def generate_usernames(config, deity, region, number, min_len, prefix='', suffix=''):
    prospects = config.generator.get_prospects(
        input_words=[deity, region],
        number=number,
        min_len=min_len
    )
    usernames = [f'{prefix}{name}{suffix}' for name in prospects]
    return usernames