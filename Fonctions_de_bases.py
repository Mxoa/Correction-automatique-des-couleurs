import numpy as np
import math
import time
import warnings
import tqdm

# Convertir les avertissements en erreurs
warnings.filterwarnings("error", category=RuntimeWarning)


# définir les fonctions de base
def signum(t, alpha=None):
# fonction signe    
    if t>=0:
        return 1
    return -1

def saturation(t, alpha=2):
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

def R_pixel(I,i,j,r,Omega, channel = 0):
    lignes=np.size(I,0)
    S=0
    colonnes=np.size(I,1)
    for x in range(lignes):
        for y in range(colonnes):
            
            try:
                print(r(I[i,j,channel] - I[x,y,channel]))
                S += Omega(i, j, x, y) * r(I[i,j,channel] - I[x,y,channel])
            except:
                print("Error")
                print("I > ", I[i,j,channel],I[x,y,channel])
                print("x,y > ", x,y)
                print("i,j > ", i,j)
                raise Exception("Error {}".format(I[i,j,0]-I[x,y,0]))
            
    return S

def R(I, f=signum, d=Omega_Ed):
    R=[]
    
    R = I.copy().astype(np.float64)
    
    for channel in range(3):
        print("Computing channel ", channel)
        for i in tqdm.tqdm(range(np.size(I,0))):
            for j in range(np.size(I,1)):
                R[i, j, channel] = R_pixel(I,i,j,f,d, channel)
    
    
    R=np.array(R)
    R=R/(abs(max(R.max(), -R.min()))) # R in [-1,1]
    print("RMAX MIN", R.max(), R.min())
    return R
    