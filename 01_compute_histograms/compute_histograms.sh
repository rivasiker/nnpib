#!/bin/bash
#SBATCH --partition normal
#SBATCH --mem-per-cpu 16G
#SBATCH -c 1
#SBATCH -t 24:00:00

python compute_histograms.py