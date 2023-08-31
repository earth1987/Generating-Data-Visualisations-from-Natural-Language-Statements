# Special paths and variables that are used across the project
def file_directory(PLATFORM):
  """Returns file directory given platform."""
  if PLATFORM == 'colab':
      return '/content/drive/MyDrive/Data science jobs/2. Portfolio/3. NL2VIS/'
  elif PLATFORM == 'hpc':
      return "/mnt/scratch/users/adbz866/"
  elif PLATFORM == 'laptop':
      return 'C:/Users/billy/OneDrive/Documents/Python Scripts/1. Portfolio/1. NL2VIS/'