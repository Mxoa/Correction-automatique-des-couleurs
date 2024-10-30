import Fonctions_de_bases
import loader
import scaling
import time
import cv2
import numpy as np
from vizualization import *


def ACE(image, f=Fonctions_de_bases.signum, d=Fonctions_de_bases.Omega_Ed):
    
    """
        Implémente l'algorithme ACE
        image : np.array : image à traiter
        f : fonction : fonction seuil
        d : fonction : fonction de distance
    """
    
    time1 = time.time()
    print("Loading image...")
    I=image.copy()
    print(f"Image loaded {time.time()-time1}s")
    print("Creating R...")
    time1 = time.time()

    r_image = Fonctions_de_bases.R(I)
    
    print("R created in ",time.time()-time1,"s")
    time1 = time.time()
    
    
    time1 = time.time()
    print("Scaling...")
    I=scaling.scaling(r_image)
    I=scaling.scaling(r_image, 1)
    I=scaling.scaling(r_image, 2)
    print("Scaled in ",time.time()-time1,"s")
    return I

if __name__=="__main__":
    image = loader.load_image(r"C:\Users\jabal\Correction-automatique-des-couleurs\image-test.png")
    show_histogram_rgb(image)
    image = ACE(image)
    show_histogram_rgb(image)
    loader.save_image(image, "test2_new")