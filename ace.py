import Fonctions_de_bases
import loader
import scaling
import time
import cv2
import numpy as np
from vizualization import *
import sys


def ACE(image, f=Fonctions_de_bases.signum, d=Fonctions_de_bases.Omega_Ed, scaling_function=scaling.scaling_gw_wp, random=False, n_pts=50, lab=True):
    
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
    print("| Lab : ", lab)
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

    if lab:
        scaling_function(r_image, 0, 0, 255)
        scaling_function(r_image, 1, 0, 255)
        scaling_function(r_image, 2, 0, 255)
    else:
        scaling_function(r_image, 0)
        scaling_function(r_image, 1)
        scaling_function(r_image, 2)
    print("Scaled in ",time.time()-time1,"s")
    return r_image.astype(np.uint8)

if __name__=="__main__":
    # Opens a file where the lines are the arguments of the program which are the name of the file to process, the name of the file to save, the alpha value, the scaling function, if the random set is used and the number of points in the random set
    with open("arguments.txt", "r") as f:
        for line in f:
            args = line.split()
            print(args)
            nom_fichier = args[0]
            nom_fichier_sauvegarde = args[1]
            alpha = float(args[2])
            scaling_f_n = args[3] == 'True'
            randomly = args[4] == 'True'
            n_pts = int(args[5])
            print("scaling_f_n", scaling_f_n)
            image = loader.load_image(nom_fichier)
            save_histogram_rgb(image, nom_fichier)
            image = ACE(image, lambda t : Fonctions_de_bases.saturation(t, alpha), Fonctions_de_bases.Omega_Ed, scaling.scaling_gw_wp if scaling_f_n else scaling.scaling, random=randomly, n_pts=n_pts)
            save_histogram_rgb(image, nom_fichier_sauvegarde)
            loader.save_image(image, nom_fichier_sauvegarde)
