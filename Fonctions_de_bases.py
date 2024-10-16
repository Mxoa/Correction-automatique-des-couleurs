import numpy as np
import math

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

def R(I,i,j,r,Omega,alpha=None):
    lignes=np.size(I,0)
    S_Omega,S=0,0
    colonnes=np.size(I,1)
    for x in range(lignes):
        for y in range(colonnes):
            S_Omega+=Omega(i,j,x,y)
            
            
            #print("I > ", I[i,j,0],I[x,y,0])
            
            try:
                S+=Omega(i,j,x,y)*r(I[i,j,0]-I[x,y,0], alpha)
            except:
                print("Error")
                print("I > ", I[i,j,0],I[x,y,0])
                print("x,y > ", x,y)
                print("i,j > ", i,j)
                print("r > ", r(I[i,j,0]-I[x,y,0], alpha))
                raise Exception("Error")
            
    return S/S_Omega