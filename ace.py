import Fonctions_de_bases
import loader
import scaling
import time
import cv2
import numpy as np
from vizualization import *
import sys


def ACE(image, f=Fonctions_de_bases.signum, d=Fonctions_de_bases.Omega_Ed, scaling_function=scaling.scaling_gw_wp, random=False, n_pts=50, lab=False):
    
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
    print("[--------------------")
    
    time1 = time.time()
    print("Loading image...")
    I=image.copy()
    print(f"Image loaded {time.time()-time1}s")
    print("Creating R...", "randomly" if random else "not randomly")
    
    save_channel_rgb(I, 0, f"lastace{"LAB" if lab else "RGB"}")
    save_channel_rgb(I, 1, f"lastace{"LAB" if lab else "RGB"}")
    save_channel_rgb(I, 2, f"lastace{"LAB" if lab else "RGB"}")
    
    time1 = time.time()

    r_image = Fonctions_de_bases.R(I, f=f, d=d) if not random else Fonctions_de_bases.R_random(I, f=f, d=d, n=n_pts, lab=lab)
    
    print("R created in ",time.time()-time1,"s")
    time1 = time.time()

    if lab:
        scaling_function(r_image, 0)
    else:
        scaling_function(r_image, 0)
        scaling_function(r_image, 1)
        scaling_function(r_image, 2)
        
    print("Scaled in ",time.time()-time1,"s")
    
    save_channel_rgb(r_image, 0, f"lastace_after{"LAB" if lab else "RGB"}")
    save_channel_rgb(r_image, 1, f"lastace_after{"LAB" if lab else "RGB"}")
    save_channel_rgb(r_image, 2, f"lastace_after{"LAB" if lab else "RGB"}")
    
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
            lab = args[6] == 'True'
            normalization = Fonctions_de_bases.Omega_Ed_2 if args[7] == 'Ed2' else Fonctions_de_bases.Omega_Manhattan if args[7] == 'Manhattan' else Fonctions_de_bases.Omega_Ed
            image = loader.load_image(nom_fichier, lab=lab)
            save_histogram_rgb(image, nom_fichier)
            image = ACE(image, lambda t : Fonctions_de_bases.saturation(t, alpha), Fonctions_de_bases.Omega_Ed, scaling.scaling_gw_wp if scaling_f_n else scaling.scaling, random=randomly, n_pts=n_pts, lab=lab)
            save_histogram_rgb(image, nom_fichier_sauvegarde)
            loader.save_image(image, nom_fichier_sauvegarde, lab=lab)
