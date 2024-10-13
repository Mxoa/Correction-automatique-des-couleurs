import numpy as np
import cv2
import Fonctions_de_bases
import loader
import scaling

I=loader.load_image('path')
#faut mettre le path de ton image
R=[]

for k in range(np.size(I,0)):
    R1=[]
    for l in range(np.size(I,1)):
        R1[l]=Fonctions_de_bases.R(I,k,l,Fonctions_de_bases.signum,Fonctions_de_bases.Omega_Ed)
    R[k].append(R1)

L=scaling.scaling(R)
loader.save_image(L)
print(I.shape)