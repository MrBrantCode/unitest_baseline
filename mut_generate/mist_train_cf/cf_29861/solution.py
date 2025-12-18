"""
QUESTION:
Write a function `parse_model_config(config)` that takes a dictionary `config` as input, where the keys are model names and the values are paths to the corresponding resources or nested dictionaries for specific models. The function should return a dictionary with the keys "word_embedding", "contextual_embedding", and "generative_model" containing the model names and their associated paths organized by model type. The model types are determined as follows: "glove" is a word embedding model, "elmo" and "bert" are contextual embedding models, and "vae" is a generative model. The stopwords path should be excluded from the output.
"""

def parse_model_config(config):
    word_embedding = {}
    contextual_embedding = {}
    generative_model = {}

    for model, path in config.items():
        if isinstance(path, str):
            if model == "glove":
                word_embedding[model] = path
            else:
                generative_model[model] = {model: path}
        else:
            if model == "elmo" or model == "bert":
                contextual_embedding[model] = path
            else:
                generative_model[model] = path

    return {
        "word_embedding": word_embedding,
        "contextual_embedding": contextual_embedding,
        "generative_model": generative_model
    }