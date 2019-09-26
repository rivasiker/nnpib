#!/bin/bash
#SBATCH --partition normal
#SBATCH --mem-per-cpu 4G
#SBATCH -c 4
#SBATCH -t 4:00:00

python chr22.py