import numpy as np
from scipy.fftpack import dct, idct
import loader as ld
from Fonctions_de_bases import Omega_Ed, saturation
import vizualization as vz
import scaling as sc



def dct2_convolution(image, kernel):
    """
    Convolution 2D basée sur la DCT (Discrete Cosine Transform).
    """
    image_dct = dct(dct(image, axis=0, norm='ortho'), axis=1, norm='ortho')
    kernel_dct = dct(dct(kernel, axis=0, norm='ortho'), axis=1, norm='ortho')
    result_dct = image_dct * kernel_dct
    result = idct(idct(result_dct, axis=0, norm='ortho'), axis=1, norm='ortho')
    return result

def get_kernel(sizex, sizey, omega):
    kernel = np.zeros((sizex, sizey))
    for i in range(sizex):
        for j in range(sizey):
            kernel[i, j] = omega(sizex//2, sizey//2, i, j)
    return kernel

def compute_R_2d(image, L, omega, s_alpha):
    """
    Calcul de R(x; L) pour une image 2D en utilisant des convolutions.
    """
    
    weights = get_kernel(image.shape[0], image.shape[1], omega)  # Noyau de convolution
    s_values = s_alpha(L - image)  # Transformation de l'image avec le niveau L
    return dct2_convolution(weights, s_values)

def ace_approximation_2d(image, omega, s_alpha, num_levels=8):
    """
    Algorithme rapide pour approximer ACE sur des images 2D.
    
    Arguments:
        image: Image d'entrée (numpy array 2D).
        omega: 
        s_alpha: Fonction seuil
        num_levels: Nombre de niveaux pour interpoler entre min(image) et max(image).
    
    Retourne:
        Une liste de convolutions calculées pour chaque niveau L.
    """
    L_min, L_max = np.min(image), np.max(image)
    levels = np.linspace(L_min, L_max, num_levels)
    R_results = []

    for L in levels:
        R = compute_R_2d(image, L, omega, s_alpha)
        R_results.append(R)
    
    return levels, R_results

def ace_interpolation(image_unnormalized, omega, s_alpha, num_levels=8, lab=False, scaling_function=sc.scaling_gw_wp):
    """
    Algorithme ACE complet pour interpoler une image 2D.
    
    Arguments:
        image: Image d'entrée (numpy array 2D).
        omega: Fonction poids (par ex., une gaussienne).
        s_alpha: Fonction de transformation pour L - I(y).
        num_levels: Nombre de niveaux pour interpoler entre min(image) et max(image).
    
    Retourne:
        Image interpolée.
    """
    
    print("ACE interpolation...")
    print("| Image shape: ", image_unnormalized.shape)
    print("| Omega: ", omega)
    print("| s_alpha: ", s_alpha)
    print("| Number of levels: ", num_levels)
    print("| Lab: ", lab)
    print("| Scaling function: ", scaling_function)
    
    
    
    image = image_unnormalized.astype(np.float64) / image_unnormalized.max()
    result = np.zeros_like(image)
        
    for channel in range(3):
        levels, R_values = ace_approximation_2d(image[:, :, channel], omega, s_alpha, num_levels)
    
        print(" # Computing channel ", channel)
        
        for k in range(num_levels-1):
            for i in range(image.shape[0]):
                for j in range(image.shape[1]):
                    if levels[k] <= image[i, j, channel] and image[i, j, channel] <= levels[k+1]:
                        result[i, j, channel] = ((R_values[k+1][i, j] - R_values[k][i, j]) / (levels[k+1] - levels[k])) * (image[i, j, channel] - levels[k]) + R_values[k][i, j]
    
    vz.save_channel_rgb(result, 0, "lastace_interpolation")
    
    scaling_function(result, 0)
    scaling_function(result, 1)
    scaling_function(result, 2)
    
    return result



if __name__ == "__main__":
    
    image = ld.load_image("images/article_pont_color.png")
    
    result = ace_interpolation(image, Omega_Ed, saturation, num_levels=8)
    
    ld.save_image(result, "images/article_pont_acel.png")
    