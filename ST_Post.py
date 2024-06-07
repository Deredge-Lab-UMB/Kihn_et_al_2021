
###
Scripted used at the completion of the simulated_tempering.py script to check temperatures sampled, and check for even sampling across the temperature range.
###

import numpy as np
import datetime
import matplotlib.pyplot as plt
from scipy.stats import linregress
import itertools
import math
import os
import pandas as pd



file_path_exp = 'output.txt'
file_path_std_output = 'results.txt'
params = {'legend.fontsize': 2,
          'legend.handlelength': 1}
plt.rcParams.update(params)

def load_exp(file_path):
    df = pd.read_csv(file_path, sep="\s+")
    return df

def plot_temerpatures(df):
    i = 0
    plt.title('Temperature weight plot')
    for c in df.columns:
        if i > 1:
            p = 0
            x_data = []
            y_data = []
            z_data = []
            for row in df.iterrows():
                y_data.append(int(df.at[p, c]))
                x_data.append((int(df.at[p, '#"Steps"'])))
                z_data.append((int(df.at[p, 'Temperature (K)'])))
                p = p + 1
            plt.plot(x_data,y_data, label= c)
            plt.xlabel('Step Number', color='#1C2833')
            plt.ylabel('Temperature Weight', color='#1C2833')
            plt.legend(loc='best')
        i = i + 1
    plt.savefig('Temperature_weight_plot.png', dpi=600)
    plt.close()

def plot_temerpatures_2(df):
    i = 0
    plt.title('Temperature weight plot')
    for c in df.columns:
        if i > 1:
            p = 0
            x_data = []
            y_data = []
            z_data = []
            for row in df.iterrows():
                y_data.append(int(df.at[p, c]))
                x_data.append((int(df.at[p, '#"Steps"'])))
                z_data.append((int(df.at[p, 'Temperature (K)'])))
                p = p + 1
            plt.plot(x_data,z_data, label= c)
            plt.xlabel('Step Number', color='#1C2833')
            plt.ylabel('Temperature', color='#1C2833')
            plt.legend(loc='best')
        i = i + 1
    plt.savefig('Temperature_plot.png', dpi=600)
    plt.close()


def add_histogram_2(df):
    i = 0
    plt.title('Temperature weight plot')
    for c in df.columns:
        if i > 1:
            p = 0
            x_data = []
            y_data = []
            z_data = []
            for row in df.iterrows():
                y_data.append(int(df.at[p, c]))
                x_data.append((int(df.at[p, '#"Steps"'])))
                z_data.append((int(df.at[p, 'Temperature (K)'])))
                p = p + 1
        i = i + 1
    plt.hist(z_data, bins=[300,320,340,360,380,400,420,440,460,480,500,520,540])
    plt.xlabel('Temperature', color='#1C2833')
    plt.ylabel('Count', color='#1C2833')
    plt.savefig('Temperature_Histogram.png', dpi=600)
    plt.close()

temp_weights = load_exp(file_path_exp)
std_output = load_exp(file_path_std_output)
plot_temerpatures(temp_weights)
plot_temerpatures_2(temp_weights)
add_histogram_2(temp_weights)
