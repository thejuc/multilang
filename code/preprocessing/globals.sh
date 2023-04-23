#! /bin/bash

# you can remove this line if you are working in your own conda environment
module load anacondapy/2022.05

# 1. Edit wherever the dicoms get transferred on the scanner
scanner_dir=/jukebox/dicom/conquest/Prisma-MSTZ400D/HassoL/2023

# 2. Edit where your project directory is
project_dir=/jukebox/PNI-classes/students/NEU502/2023-NEU502B/wlong/multilang

# 3. Edit where your scratch and work directories are located
scratch_dir=/jukebox/scratch/wlong/work/multilang

data_dir=$project_dir/data
bids_dir=$data_dir/bids
raw_dir=$data_dir/dicom                     # this is where I want the data from conquest to be copied into my study directory
defaced_dir=$bids_dir/derivatives/deface    # this is where defaced images will end up
scripts_dir=$project_dir/code/preprocessing # directory with my preprocessing scripts, including this one
