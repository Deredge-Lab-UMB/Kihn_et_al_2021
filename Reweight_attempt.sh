
###
Executes the post hoc HDXer reweighing of a trajectory over a user defined range of gamma values.
###

#!/bin/bash

# Script to run MSD analysis of PhuS to expt data
# with full range of gammas

### The 'source activate python37' and MKL_NUM_THREADS commands below are only needed for my machine
### You can comment them out!
### There might be an equivalent environment variable (sometimes OMP_NUM_THREADS)
### to choose a specific number of threads per process on your
### machines, otherwise numpy will run in serial.
source activate openMM
#export MKL_NUM_THREADS=4
###

### Inputs: 
trajfolders='/home/dderedge/Desktop/HDXer_and_Clustering_Tutorial/Calc_HDX/Demo_Files/'
exptfile="UP_holo_SCH.txt"
ratefile="/home/dderedge/Desktop/HDXer_and_Clustering_Tutorial/Calc_HDX/Demo_Files/Intrinsic_rates.dat"

echo "Starting reweighting WITH parameter optimization"
for ((i=-1;i<=-1;i++))
do
 # -l for floating point
 basegamma=`bc -l <<< 10^$i`
 baserate=0.001
 for ((j=1;j<=9;j++))
 do
  gamma=`bc -l <<< $basegamma*$j`
python reweighting.py -f $trajfolders -exp $exptfile -r $ratefile -out "ERK2_SCH_w_Mg_"$j"x10^"$i"_" -g $gamma -mcmin -rf $baserate -dt 0.167 1 10 60 120.0 -bc 0.5 -bh 2
  echo "Gamma "$gamma" complete."
 done
done
