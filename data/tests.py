import numpy as np
from scipy import interpolate
from ROOT import gROOT, TCanvas, TGraph
import array as arr

def getGraphFromFunc(f, inputs):
    outputs = arr.array('f')
    inp = arr.array('f')
    for i in inputs:
        inp.append(i)
        outputs.append(f(i))
    graph = TGraph(len(inputs),inp,outputs)
    return graph

#main

gROOT.Reset()

w_low = 2 * np.pi * (213 - 0.25) * (10**6)
delta_w = 2 * np.pi * 500 * ((10**3)/256)

k_ints = range(0,256)
k = np.array(k_ints,float)

x = (k*delta_w)+w_low

#READING IN DATA FROM FILES

butxi = []
butxii = []
vback = []
vreal = []

f = open("DPROTON.DAT","r")
for line in f:
    butxi.append(float(line))
f.close()

f2 = open("PROTON.DAT","r")
for line in f2:
    butxii.append(float(line))
f2.close()

f3 = open("Backgmd.dat","r")
for line in f3:
    vback.append(float(line))
f3.close()

f4 = open("Backreal.dat","r")
for line in f4:
    vreal.append(float(line))
f4.close()

x1 = interpolate.interp1d(x,butxi)
x2 = interpolate.interp1d(x,butxii)
b = interpolate.interp1d(x,vback)
rb = interpolate.interp1d(x,vreal)



