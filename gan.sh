#!/bin/bash

#SBATCH --job-name gan   ##name that will show up in the queue
#SBATCH --output gan.out   ##filename of the output; the %j will append the jobID to the end of the name making the output files unique despite the sane job name; default is slurm-[jobID].out
#SBATCH --gres=gpu:1  ##number of GPUs per node
#SBATCH --nodes 1  ##number of nodes to use
#SBATCH --time 0-00:100:00  ##time for analysis (day-hour:min:sec)
#SBATCH --ntasks 1  ##number of tasks (analyses) to run
#SBATCH --cpus-per-task 1  ##the number of threads the code will use
#SBATCH --partition epscor  ##the partition to run in [options: normal, backfill, cdflab, cdflab-debug, gpu, debug]
#SBATCH --mem-per-cpu 4096M

## Load modules, insert code, and run your programs here.
##module load tensorflow-gpu/1.15.0
module load cuda/10.1.243-gcc-9.2.0-gl7b4mh
##module load cuda/10.0.130-gcc-4.8.5-kqvlz4i
##module load pytorch
source /home/qqli_epscor/ganvenv/bin/activate
srun -n 1 python capgtrain.py
