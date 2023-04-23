import sys
import requests


def gts(t: dict):
    te = t['boundedBy']['Envelope']
    lc = list(map(float, te['lowerCorner'].split()))
    uc = list(map(float, te['upperCorner'].split()))
    ts = str(abs(lc[0] - uc[0])), str(abs(lc[1] - uc[1]))
    #ts = ['0.005', '0.005']
    print(ts)
    return ts
