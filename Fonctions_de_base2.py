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
    y=f(x,alpha)
    cheb_poly = Chebyshev.fit(x, y, degree)
    Max_error=np.max(np.abs(np.subtract(y,cheb_poly(x))))
    return (cheb_poly,Max_error)

'''Y=Approximation_polynomiale(saturation2,17)[0](x)
#L'erreur maximale
print(Approximation_polynomiale(saturation2,17)[1])
plt.plot(x,Y)
plt.show()'''

def R_interpolation(x,y,L,img,f,alpha=2,omega):
    height,width=np.size(img,0),np.size(img,1)
    F=np.zeros((height,width))
    Omega=np.zeros((height,width))
    for i in range(height):
        for j in range(width):
            F[i,j]=f(L-img(i,j),alpha)
            Omega[i,j]=omega(x,y,i,j)
    return scipy.signal.convolve2d(Omega,F)    
    
def Interpolation(x,y,img,number_of_levels=8):
    L=np.zeros(8)
    for j in range(number_of_levels):
        L[j]=np.min(img)-(np.max(img)-np.min(img))*(j/(number_of_levels-1))
    #J'ai pas encore terminé la fonction
        