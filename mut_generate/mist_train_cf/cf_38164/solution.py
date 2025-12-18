"""
QUESTION:
Write a function `getXY` that calculates the coordinates of a focused window. It takes a focused window object `fw` and the dimensions of a status bar (`sbw` and `sbh`) as input, along with two boolean flags `DEBUG_COORDS` and `DEBUG_STATUSBAR` to control debug output. The function returns a tuple of coordinates `(pwx, pwy)`. If `fw` is falsy, return `(0, 0)`. Apply the following rules: 
- If `DEBUG_COORDS` is True, print debug information about the focused window.
- If `fw.wvy` is less than or equal to `sbh`, set `statusBarOffset` to `sbh`.
- If `fw.py` equals `fw.wvy`, adjust the coordinates using `fw.px` and `fw.py`.
"""

def getXY(fw, sbw, sbh, DEBUG_COORDS, DEBUG_STATUSBAR):
    pwx = 0
    pwy = 0

    if fw:
        if DEBUG_COORDS:
            print("getXY: focused window=", fw, "sb=", (sbw, sbh))
        if fw.wvy <= sbh:
            statusBarOffset = sbh
            if DEBUG_STATUSBAR:
                print("getXY: yes, considering offset=", sbh)
        else:
            if DEBUG_STATUSBAR:
                print("getXY: no, ignoring statusbar offset fw.wvy=", fw.wvy, ">", sbh)

        if fw.py == fw.wvy:
            pwx = fw.px
            pwy = fw.py
            if DEBUG_STATUSBAR:
                print("getXY: but wait, fw.py == fw.wvy so we are adjusting by ", (fw.px, fw.py))

    return pwx, pwy