"""
QUESTION:
Implement a function `updateTextures(xIn, args)` that takes a list of textures `xIn` and a dictionary `args` containing two lists of boolean values `optThetas` and `optPhis` as input. For each texture in `xIn`, apply the following rules based on the corresponding values in `optThetas` and `optPhis`: if both are `True`, include the entire texture; if only `optThetas` is `True`, include the first half of the texture; if only `optPhis` is `True`, include the second half of the texture. Return the modified list of textures.
"""

def entrance(xIn, args):
    opt_thetas = args['optThetas']
    opt_phis = args['optPhis']
    xOut = []

    for i, (t, f) in enumerate(zip(opt_thetas, opt_phis)):
        if t and f:
            xOut.append(xIn[i])
        elif t:
            pts_per_phase = xIn[i].size // 2
            xOut.append(xIn[i][:pts_per_phase])
        elif f:
            pts_per_phase = xIn[i].size // 2
            xOut.append(xIn[i][pts_per_phase:])

    return xOut