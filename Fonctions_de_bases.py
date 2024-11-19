import numpy as np
import math
import time
import warnings
import tqdm
import random

# Convertir les avertissements en erreurs
warnings.filterwarnings("error", category=RuntimeWarning)


# définir les fonctions de base
def signum(t):
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
    return 1/(abs(i1-i2)+abs(j1-j2))

def R_pixel(I,i,j,r,Omega, channel = 0):
    lignes=np.size(I,0)
    S=0
    S_normalize=0
    
    colonnes=np.size(I,1)
    for x in range(lignes):
        for y in range(colonnes):
            
            S_normalize += Omega(i, j, x, y)
            
            #try:
            #print(r(I[i,j,channel] - I[x,y,channel]))
            S += Omega(i, j, x, y) * r(float(I[i,j,channel]) - float(I[x,y,channel]))
            # except:
            #     print("Error")
            #     print("I > ", I[i,j,channel],I[x,y,channel])
            #     print("x,y > ", x,y)
            #     print("i,j > ", i,j)
            #     #raise Exception("Error {}".format(float(I[i,j,channel]) - float(I[x,y,channel])))
            
    return S/(S_normalize*(r(10)))

def R_pixel_random(I,i,j,r,omega, random_set, channel = 0, rmax=1):
    S=0
    S_normalize=0
    for (x , y) in random_set:
        S += omega(i, j, x, y) * r(float(I[i,j,channel]) - float(I[x,y,channel]))
        S_normalize += omega(i, j, x, y)
    return S/(S_normalize*(rmax))

def R_random(I, f=signum, d=Omega_Ed, n=1000):
    R=[]
    
    R = I.copy().astype(np.float64)
    
    I_X = np.size(I,0)
    I_Y = np.size(I,1)
    
    random_set = set()
    while len(random_set) < n:
        x = random.randint(0, I_X- 1)
        y = random.randint(0, I_Y- 1)
        random_set.add((x, y))

    
    for channel in range(3):
        print("Computing channel ", channel)
        for i in tqdm.tqdm(range(np.size(I,0))):
            for j in range(np.size(I,1)):
                R[i, j, channel] = R_pixel_random(I,i,j,f,d, random_set, channel)
    
    
    R=np.array(R)
    # R=R/(abs(max(R.max(), -R.min()))) # R in [-1,1]
    # print("RMAX MIN", R.max(), R.min())
    return R

def R(I, f=signum, d=Omega_Ed):
    R=[]
    
    R = I.copy().astype(np.float64)
    
    for channel in range(3):
        print("Computing channel ", channel)
        for i in tqdm.tqdm(range(np.size(I,0))):
            for j in range(np.size(I,1)):
                R[i, j, channel] = R_pixel(I,i,j,f,d, channel)
    
    
    R=np.array(R)
    # R=R/(abs(max(R.max(), -R.min()))) # R in [-1,1]
    # print("RMAX MIN", R.max(), R.min())
    return R


def gray_world(image):
    red_channel = image[:, :, 0]
    blue_channel = image[:, :, 1]
    green_channel = image[:, :, 2]
    
    means = []