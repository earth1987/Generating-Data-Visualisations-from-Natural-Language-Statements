#!/bin/bash
#SBATCH -D /mnt/scratch/users/adbz866           # Working directory
#SBATCH --job-name RO1_gptneo125m_1                 # Job name
#SBATCH --partition=jupyter                       # Controls which partition is used for the job
#SBATCH --nodes=1                               # Controls the minimum/maximum number of nodes allocated to the job
#SBATCH --ntasks-per-node=1                     # Controls the maximum number of tasks per allocated node
#SBATCH --cpus-per-task=1                       # Controls the number of CPUS allocated per task
#SBATCH --mem=10GB                              # Expected ammount CPU RAM needed (Not GPU Memory)
#SBATCH --gres=gpu:1                            # GPUs
#SBATCH --time=12:00:00                         # Expected ammount of time to run Time limit hrs:min:sec
#SBATCH --mail-type=begin                       # Send email when job begins
#SBATCH --mail-type=end                         # Send email when job ends
#SBATCH --mail-type=fail                        # Send email when job fails
#SBATCH --mail-user=billy.pitchford@city.ac.uk

flight env activate gridware
module load libs/nvidia-cuda/11.2.0/bin 
source activate LM_v3
python Test_set_inference_v1.py -o EleutherAI -m gpt-neo-125M -f 3shot_10fold_test -d cuda -b 5 -n 10 -pr 3 -t 1