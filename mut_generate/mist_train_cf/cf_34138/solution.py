"""
QUESTION:
Implement the `max_pooling` function, which takes a 4-dimensional NumPy array `x` with shape `(N, C, H, W)` and a kernel size `k` as input and applies max-pooling to generate the pooled output tensor. The function should return the max-pooled output tensor with the same number of samples and channels but reduced spatial dimensions based on the specified kernel size. Assume that the kernel size `k` divides the height and width of the input tensor without leaving any remainder. The function should not rely on external libraries or functions for the max-pooling operation.
"""

def max_pooling(x, k):
    N, C, H, W = x.shape
    H_out = H // k
    W_out = W // k
    pooled_output = np.zeros((N, C, H_out, W_out))

    for i in range(H_out):
        for j in range(W_out):
            h_start = i * k
            h_end = h_start + k
            w_start = j * k
            w_end = w_start + k
            subregion = x[:, :, h_start:h_end, w_start:w_end]
            pooled_output[:, :, i, j] = np.max(subregion, axis=(2, 3))

    return pooled_output