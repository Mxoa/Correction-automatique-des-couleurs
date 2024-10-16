import Fonctions_de_bases
import loader
import scaling
import time
import cv2
import numpy as np
from vizualization import *


def ACE(image, f=Fonctions_de_bases.signum, d=Fonctions_de_bases.Omega_Ed):
    
    time1 = time.time()
    print("Loading image...")
    I=image
    print(f"Image loaded {time.time()-time1}s")

    time1 = time.time()
    R=[]
    
    print("Creating R...")

    for k in range(np.size(I,0)):
        R1=[]
        for l in range(np.size(I,1)):
            R1.append(Fonctions_de_bases.R(I,k,l,f,d))
        R.append(R1)
    
    print("R created in ",time.time()-time1,"s")
    time1 = time.time()
    print("Scaling...")
    L=scaling.scaling(R)
    print(I.shape)
    print("Scaled in ",time.time()-time1,"s")
    return I

if __name__=="__main__":
    image = loader.load_image("images/test2.jpg")
    show_histogram_rgb(image)
    image = ACE(image)
    show_histogram_rgb(image)