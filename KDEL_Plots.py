
###
An example of the type of script used to generate the KDEL plots in Kihn et. al., 2021
###


import mdtraj as md
import numpy as np
import matplotlib.pyplot as plt
import pyemma
import pandas as pd
import seaborn as sns

plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"
COM = pd.read_csv('COM.dat', sep='\s+')
SASA = pd.read_csv('VTX_Restrained_SASA.txt')
SASA_data = []
COM_data = []

x = 0 
for row in COM.iterrows():
    data = COM.at[x,'COM'] 
    COM_data.append(data)      
    x = x + 1

z = 0
for row in SASA.iterrows():
    data = SASA.at[z,'SASA'] 
    SASA_data.append(data)    
    z = z + 1


sns.kdeplot(COM_data,SASA_data, shade=True, cbar=True) #,common_norm=True)
plt.xlabel('Center of Mass (\u212B)')
plt.ylabel('SASA (nm^2)')
#plt.xlim(0,25)
#plt.ylim(5,22)
plt.savefig('COM_vs_SASA_VTX.png', dpi=600)
plt.close()
