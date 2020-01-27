import numpy as np
from scipy import interpolate
from ROOT import gROOT, TCanvas, TGraph, gApplication
import array as arr
import cmath

def getGraphFromFunc(f, inputs):
    outputs = arr.array('f')
    inp = arr.array('f')
    for i in inputs:
        inp.append(i)
        outputs.append(f(i))
    graph = TGraph(len(inputs),inp,outputs)
    return graph

#---------------------preamble----------------

pi = np.pi
im_unit = complex(0,1)
print(im_unit)

#----------------------main------------------

gROOT.Reset()

#Parameters of problem
U = 0.1 #100 mV RF input
L0 = 3e-8 #Inductance of coil 30 nH
R = 619
r = 10
Rcoil = 0.35
f = 213e6
knob = 0.885
Cstray = 1e-15 #Stray capacitance 10^-3 pF
trim = 7*0.5

delta_C = 0
delta_phi = 0

#Derived quantities
w_res = 2*pi*f
w_low = 2 * pi * (213 - 0.25) * (1e6)
w_high = 2 * pi * (213 + 0.25) * (1e6)
delta_w = 2 * pi * 500 * ((1e3)/256)

#Functions
def slope():
    return delta_C / (0.25 * 2 * pi * 1e6)

def slope_phi():
    return delta_phi / (0.25 * 2 * pi * 1e6)

def Ctrim(w):
    return slope()*(w - w_res)

def Cmain():
    return 20*(1e-12)*knob

def C(w):
    return Cmain() + Ctrim(w)*(1e-12)

def Cpf():
    return C(w_res)*(1e12)

#--------------------Cable characteristics-------------

#Parameters
alpha = 0.0343 #estimate from August 1997
beta1 = 4.752e-9
Z_cable = 50 #Cable impedance 50 ohms
D = 10.27e-11 #F/m
M = 2.542e-7
delta_l = 0

#Derived quantities
S = 2*Z_cable*alpha

#Functions

def Z0(w):
    return cmath.sqrt( (S + w*M*im_unit) / (w*D*im_unit))

def beta(w):
    return beta1*w

def gamma(w):
    return complex(alpha,beta(w))

def Zc(w):
    temp_variable = complex(0,w*C(w))
    return 1/temp_variable

#More derived quantities
vel = 1/beta(1)

#More functions
def lam(w):
    return vel/f

#Even more derived quantities
l = trim*lam(w_res)

#Even more functions
def l(w):
    return l +  delta_l





#------------------READING IN DATA FROM FILES-------------

#Variables for creating splines
k_ints = range(0,256)
k = np.array(k_ints,float)
x = (k*delta_w)+w_low

butxi = []
butxii = []
vback = []
vreal = []

Icoil = []

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

f5 = open("current.dat","r")
for line in f5:
    Icoil.append(float(line))
f5.close()

x1 = interpolate.interp1d(x,butxi)
x2 = interpolate.interp1d(x,butxii)
b = interpolate.interp1d(x,vback)
rb = interpolate.interp1d(x,vreal)

def chi(w):
    return complex(x1(w),-1*x2(w))



ic = interpolate.interp1d(k,Icoil)
#tg = getGraphFromFunc(x1,x)
tg = getGraphFromFunc(ic,k)

tg.Draw()
gApplication.Run()
