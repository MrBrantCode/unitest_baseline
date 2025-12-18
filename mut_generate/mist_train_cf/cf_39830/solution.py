"""
QUESTION:
Implement a function `calculate_mean_loss` that takes four input arrays `u_online`, `u_target`, `i_online`, and `i_target` representing online and target embeddings for users and items, and returns the mean loss calculated using the formula: `mean_loss = (2 - 2 * (u_online * i_target).sum(dim=-1) + 2 - 2 * (i_online * u_target).sum(dim=-1)).mean()`. The input arrays should be two-dimensional and the function should return a single number representing the mean loss.
"""

def calculate_mean_loss(u_online, u_target, i_online, i_target):
    loss_ui = 2 - 2 * (np.sum(u_online * i_target, axis=-1))
    loss_iu = 2 - 2 * (np.sum(i_online * u_target, axis=-1))
    mean_loss = np.mean(loss_ui + loss_iu)
    return mean_loss