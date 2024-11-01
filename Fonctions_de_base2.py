import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.chebyshev import Chebyshev
import scipy
import scipy.signal
import Fonctions_de_bases


def saturation2(t, alpha=2):
    # Application de la saturation à chaque élément de l'array
    return np.clip(alpha * t, -1, 1)

x=np.linspace(-256,256,10000)

def Approximation_polynomiale(f,degree,alpha=2):
    #approximation par les polynomes de Tchebychev
    y=f(x,alpha)
    cheb_poly = Chebyshev.fit(x, y, degree)
    Max_error=np.max(np.abs(np.subtract(y,cheb_poly(x))))
    return (cheb_poly,Max_error)

'''Y=Approximation_polynomiale(saturation2,17)[0](x)
#L'erreur maximale
print(Approximation_polynomiale(saturation2,17)[1])
plt.plot(x,Y)
plt.show()'''

def R_interpolation1(L,img,fonction,omega,alpha=2):
    #C'est le calcul de R(x,Lj) qu'on retrouve dans l'article 2 sauf que là on calcule R pour toute l'image au lieu d'un seul pixel x
    height,width=np.size(img,0),np.size(img,1)
    F=np.zeros((height,width))
    Omega=np.zeros((height,width))
    for i in range(height):
        for j in range(width):
            F[i,j]=fonction(L-img(i,j),alpha)
            Omega[i,j]=omega(0,0,i,j)
    return scipy.signal.convolve2d(Omega,F,mode='same')    
    
def R_interpolation2(img,fonction,omega,number_of_levels=8,alpha=2):
    #C'est le calcul du developpement limité qui se trouve juste après dans le meme article
    height,width=np.size(img,0),np.size(img,1)
    L=np.zeros(number_of_levels)
    # L c'est une liste qui contient les niveaux de "quantification" Lj
    R=[]
    # R c'est une liste des images R(Lj) 
    modified_image=np.zeros((height,width))
    # modified image c'est l'image résultante
    for j in range(number_of_levels):
        L[j]=np.min(img)-(np.max(img)-np.min(img))*(j/(number_of_levels-1))
        R.append(R_interpolation1(L[j],img,fonction,omega,alpha))
    for k in range(height):
        for l in range(width):
            for j in range(number_of_levels-1):
                if img[k,l]<=L[j+1] and img[k,l]>=L[j]:
                    modified_image[k,l]=((R[j+1][k,l]-R[j][k,l])/(L[j+1]-L[j]))*(img[k,l]-L[j])
    return modified_image