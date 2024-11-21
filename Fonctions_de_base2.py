import numpy as np
from numpy.polynomial.chebyshev import Chebyshev
import scipy
import scipy.signal
import loader as ld
from Fonctions_de_bases import *
import scaling as sc
from tqdm import tqdm

x=np.linspace(-256,256,10000)

#Première methode
def Approximation_polynomiale(f, degree, alpha=2):
    # Approximation par les polynômes de Tchebychev
    y = f(x, alpha)
    cheb_poly = Chebyshev.fit(x, y, degree)
    #max_error = np.max(np.abs(y - cheb_poly(x)))
    coefficients = cheb_poly.coef.tolist()
    return coefficients


def R_poly(img, f, degree, omega, alpha=2):
    height,width=np.size(img,0),np.size(img,1)
    R=np.zeros(height,width)
    Omega=np.zeros(height,width)
    cheby=Approximation_polynomiale(f, degree, alpha)
    for x in range(height):
        for y in range(width):
            Omega[x,y]=omega(x,y,0,0)
    for x in range(height):
        for y in range(width):
            for i  in range(degree+1):
                convolved_image=scipy.signal.convolve2d(Omega,img**i)
                ai=0
                # a c'est a.n(x) dans l'article2
                for j in range(i,degree+1):
                    a+=cheby[j]*((-1)**(j-i+1))*((img[x,y])**(j-i))
                R[x,y]+=ai*convolved_image[x,y]
    return R
    

def get_kernel(sizex, sizey, omega):
    kernel = np.zeros((sizex, sizey))
    for i in range(sizex):
        for j in range(sizey):
            kernel[i, j] = omega(sizex//2, sizey//2, i, j)
    return kernel

#Deuxième methode
def R_convolution(L,img,fonction,omega,alpha=2):
    #C'est le calcul de R(x,Lj) qu'on retrouve dans l'article 2 sauf que là on calcule R pour toute l'image au lieu d'un seul pixel x
    height,width=np.size(img,0),np.size(img,1)
    F=np.zeros((height,width))
    
    kernel = get_kernel(width, height, omega)
    
    for i in range(height):
        for j in range(width):
            F[i,j]=fonction(L-img[i,j],alpha)
    return scipy.signal.convolve2d(F,kernel,mode='same', boundary='wrap')
    
def R_interpolation(img_uint,fonction,omega,number_of_levels=8,alpha=2):
    #C'est le calcul du developpement limité qui se trouve juste après dans le meme article
    height,width=np.size(img_uint,0),np.size(img_uint,1)
    L=np.zeros(number_of_levels)
    
    img = img_uint.copy().astype(np.float64)
    # L c'est une liste qui contient les niveaux de "quantification" Lj
    R=[]
    # R c'est une liste des images R(Lj) 
    modified_image=np.zeros((height,width))
    # modified image c'est l'image résultante
    for j in range(number_of_levels):
        L[j]=((img.max()) - img.min())*j*(1/(number_of_levels-1)) + img.min()
        R.append(R_convolution(L[j],img,fonction,omega,alpha))
        
    print("L", L)
    for l in range(width):
        for j in range(number_of_levels-1):
            for k in range(height):
                if img[k,l]<=L[j+1] and img[k,l]>L[j]:
                    modified_image[k,l]=((R[j+1][k,l]-R[j][k,l])/(L[j+1]-L[j]))*(img[k,l]-L[j]) + R[j][k,l]
    return modified_image


def ace_l(image, f=saturation, number_of_levels=8, omega=Omega_Ed, alpha=2):
    # ACE avec approximation polynomiale
    for channel in (range(3)):
        image[:,:,channel] = R_interpolation(image[:,:,channel], f, omega, number_of_levels, alpha)
        
    sc.scaling(image, 0)
    sc.scaling(image, 1)
    sc.scaling(image, 2)
    
    return image

if __name__ == "__main__":
    ima = ld.load_image("images/article_pont.png")
    ima = ace_l(ima, number_of_levels=8)
    ld.save_image(ima, "images/article_pont_acel.png")