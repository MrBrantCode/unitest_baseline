"""
QUESTION:
Create a function named `fill_tensor` that takes a 3D tensor `a` and a 1D tensor `lengths` as input. The function should fill the tensor `a` with the value 2333 after a certain index along dimension 1 (sentence length) based on the corresponding value in the tensor `lengths`. The modified tensor `a` should be returned. 

The function should work with tensors of varying sizes, but the input tensors `a` and `lengths` should have the following properties: `a` is a 3D tensor with shape `(batch, sentence_length, embedding_dimension)` and `lengths` is a 1D tensor with shape `(batch,)`.
"""

def fill_tensor(a, lengths):
    for i, length in enumerate(lengths):
        a[i, length:, :] = 2333
    return a