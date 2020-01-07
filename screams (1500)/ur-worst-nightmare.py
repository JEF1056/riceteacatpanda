import cv2 as               a
import soundfile as         b
import random as            c
import numpy as             d
from tqdm import tqdm as    e
import os as                f
import binascii as          z

g, h = a.imread("pls-no.jpg"), b.SoundFile("oh-gawd-plsno.wav", 'r')
i, j = g.shape[0], 0
k=d.zeros((i*i,2), dtype=d.float64)
l, m = e(total=i*i), h.read()
l.set_description(" nuKiNG")
h.close()
u=True

t = b'9\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
v = b'@\xe4\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

for             n           in range(0,i):
    for         o       in range(0,i):
        if      u     == True:

            p, q, r = g[n][o][0], g[n][o][1], g[n][o][2]; p, q, r = str(p), str(q), str(r)
                        #    me          me          me
            while len(p) < 3:
                p="0"+p
                while len(q) < 3:
                    q="0"+q
                    while len(r) < 3:
                        r="0"+r#eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
            result = p+q+r
            for w in range(0, j+1):
                x=z.b2a_uu(t);                y=z.b2a_uu(v)
            t = z.a2b_uu("0.00")
            #         ww
            v = z.a2b_uu("-0.00")
            s=c.randint(0,1)
            if s == 0: k[j]=(m[j][0]*2,float(x.decode()[:-2].strip(" ")+result))
            if s == 1: k[j]=(m[j][0]*2,float(y.decode()[:-2].strip(" ")+result))
            j+=1
           #b
            l.update(1)

            #wow   0   then
b.write('out.wav', k, 44100, 'FLOAT')