"""
QUESTION:
Implement a function `soft_copy(targ_net, net, tau)` that performs a soft copy of the parameters from the source network `net` to the target network `targ_net` using a weighted average with a given `tau` value. The update rule is `new_param = (1 - tau) * targ_param + tau * src_param`, where `targ_param` and `src_param` are the parameters of the target and source networks, respectively. The function should return the updated target network.
"""

def entance(targ_net, net, tau):
    for p_target, p in zip(targ_net.parameters(), net.parameters()):
        p_target.data.copy_((1 - tau) * p_target.data + tau * p.data)
    return targ_net