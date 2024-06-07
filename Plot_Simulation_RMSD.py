
###
Plots per residue average and maximum RMSD of trajectories from the simulation starting structure.
###

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('RMSD_H212R_Run1.tml', skiprows=[0,1,2,3,4,5,6,7,8], header=None, sep='\s+')
df.columns = ['res_id', 'chain', 'empty', 'frame', 'rmsd']

class Res:
    ...

x = 0
res_list = []
res_name = []
for row in df.iterrows():
    if df.at[x,'res_id'] in res_name:
        break
    if df.at[x,'res_id'] not in res_name:
        res = Res()
        setattr(res, 'res_id', df.at[x,'res_id'])
        setattr(res, 'rmsd', [])
        res_list.append(res)
        res_name.append(df.at[x,'res_id'])
    x = x + 1

z = 0
for row in df.iterrows():
    res_name = df.at[z,'res_id']
    res_name = res_name - 1
    _res = res_list[res_name]
    name = _res.res_id
    rmsd = _res.rmsd
    rmsd.append(df.at[z, 'rmsd'])
    setattr(_res, 'rmsd', rmsd)
    z = z + 1

columns = []

name_id = 0
for num in res_list[0].rmsd:
   columns.append(str(name_id))
   name_id = name_id + 1
ndf = pd.DataFrame(columns=columns)
y = 0
for res in res_list:
    i = 0
    for p in res_list[y].rmsd:
        ndf.at[y, str(i)] = float(res_list[y].rmsd[i])
        average = sum(res_list[y].rmsd)/len(res_list[y].rmsd)
        maximum = max(res_list[y].rmsd)
        setattr(res_list[y], 'average', average)
        setattr(res_list[y], 'max', maximum)
        i = i + 1
    y = y + 1
new_columns = []
for c in columns:
    new_columns.append(int(c)*10)
ndf.columns = new_columns
ndf = ndf.astype('int64')
heatmap = sns.heatmap(ndf, cbar=True, xticklabels=True, cmap='brg')
plt.gca().xaxis.set_major_locator(plt.MaxNLocator(50))
plt.xlabel('Frame')
plt.ylabel('Residue')
plt.savefig('Heatmap_RMSD.png', dpi=600)
plt.close()
ax = []
mx = []
y_ax = []
for r in res_list:
    y_ax.append(r.res_id)
    ax.append(r.average)
    mx.append(r.max)
plt.plot(ax,y_ax)
plt.gca().invert_yaxis()
plt.savefig('Average_RMSD_Plot.png', dpi=600)
plt.close()
plt.plot(mx, y_ax)
plt.gca().invert_yaxis()
plt.savefig('Max_RMSD_Plot.png', dpi=600)
plt.close()
with open('RMSD_Results.txt', 'w+') as f:
    f.write('PhuS  H212R 520K Simulated Tempering Run 1 RMSD Avereage: ' + str(sum(ax)/len(ax)) + '\n')
    f.close()
