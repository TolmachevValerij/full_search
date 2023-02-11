import sys
import requets


def gts(t: dict):
    te = t['boundedBy']['Envelope']
    lc = list(map(float, te['lowerCorner'].split()))
    uc = list(map(float, te['upperCorner'].split()))
    ts = abs(lc[0] - uc[0]), abs(lc[1] - uc[1])
    return ts


