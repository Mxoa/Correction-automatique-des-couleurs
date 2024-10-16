import numpy as np
import math
import time
import warnings

# Convertir les avertissements en erreurs
warnings.filterwarnings("error", category=RuntimeWarning)


# définir les fonctions de base
def signum(t, alpha=None):
# fonction signe    
    if t>=0:
        return 1
    return -1

def saturation(t, alpha):
# fonction saturation    
    return min(max(alpha*t , -1) , 1)

def Omega_Ed(i1,j1,i2,j2):
# distance euclidienne
# i et j les coordonées du pixel    
    if i1==i2 and j1==j2:
        return 0
    return 1/(math.sqrt(((i1-i2)**2)+((j1+j2)**2)))

def Omega_Manhattan(i1,j1,i2,j2):
# Norme 1
    if i1==i2 and j1==j2:
        return 0
    return 1/(abs(i1-i2)+abs(j1+j2))

def R_pixel(I,i,j,r,Omega):
    lignes=np.size(I,0)
    S=0
    colonnes=np.size(I,1)
    for x in range(lignes):
        for y in range(colonnes):
            
            try:
                S += Omega(i, j, x, y) * r(int(I[x,y,0]) - int(I[i,j,0]))
            except:
                print("Error")
                print("I > ", I[i,j,0],I[x,y,0])
                print("x,y > ", x,y)
                print("i,j > ", i,j)
                print("r > ", r(I[i,j,0]-I[x,y,0]))
                raise Exception("Error {}".format(I[i,j,0]-I[x,y,0]))
            
    return S

def R(I, f=signum, d=Omega_Ed):
    R=[]
    
    R = I.copy().astype(np.float64)
    

    for k in range(2): #np.size(I,0)):
        for l in range(2): #np.size(I,1)):
            R[k, l, 0] = R_pixel(I,k,l,f,d)
    
    
    R=np.array(R)
    R=R/(max(R.max(), -R.min())) # R in [-1,1]
    
    return R
    

def R_max(I,r,Omega,alpha=None):
    lignes=np.size(I,0)
    colonnes=np.size(I,1)
    S=0
    for i in range(lignes):
        for j in range(colonnes):
            S=max(S,R(I,i,j,r,Omega,alpha))
    return S