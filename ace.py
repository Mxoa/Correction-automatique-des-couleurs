import Fonctions_de_bases
import loader
import scaling
import time
import cv2
import numpy as np
from vizualization import *
import sys


def ACE(image, f=Fonctions_de_bases.signum, d=Fonctions_de_bases.Omega_Ed, scaling_function=scaling.scaling_gw_wp, random=False, n_pts=50):
    
    """
        Implémente l'algorithme ACE
        image : np.array : image à traiter
        f : fonction : fonction seuil
        d : fonction : fonction de distance
    """
    
    print("[[ACE]]")
    print("| f : ", f)
    print("| d : ", d)
    print("| scaling_function : ", scaling_function)
    print("| random : ", random)
    print("| If random, n_pts : ", n_pts)
    print("| Image shape : ", image.shape)
    print("--------------------")
    
    time1 = time.time()
    print("Loading image...")
    I=image.copy()
    print(f"Image loaded {time.time()-time1}s")
    print("Creating R...", "randomly" if random else "not randomly")
    time1 = time.time()

    r_image = Fonctions_de_bases.R(I, f=f, d=d) if not random else Fonctions_de_bases.R_random(I, f=f, d=d, n=n_pts)
    
    print("R created in ",time.time()-time1,"s")
    time1 = time.time()
    
    
    time1 = time.time()
    print("Scaling...")
    scaling_function(r_image)
    scaling_function(r_image, 1)
    scaling_function(r_image, 2)
    print("Scaled in ",time.time()-time1,"s")
    return r_image

if __name__=="__main__":
    
    if len(sys.argv) < 4:
        print("Usage: python ace.py <nom_photo> <nom_fichier_sauvegarde> <alpha> <scaling_function_wpgw=False or True, True by default> <random=True or False> <n>")
        sys.exit(1)

    print(sys.argv)
    nom_fichier = sys.argv[1]
    nom_fichier_sauvegarde = sys.argv[2]
    alpha = float(sys.argv[3])
    scaling_f_n = sys.argv[4] == 'True' if len(sys.argv) >= 5 else True
    randomly = sys.argv[5] == 'True' if len(sys.argv) >= 6 else False
    n_pts = int(sys.argv[6]) if len(sys.argv) >= 7 else 50
    
    print("scaling_f_n", scaling_f_n)
    
    image = loader.load_image(nom_fichier)
    #show_histogram_rgb(image)
    image = ACE(image, lambda t : Fonctions_de_bases.saturation(t, alpha), Fonctions_de_bases.Omega_Ed, scaling.scaling_gw_wp if scaling_f_n else scaling.scaling, random=randomly, n_pts=n_pts)
    #show_histogram_rgb(image)
    loader.save_image(image, nom_fichier_sauvegarde)