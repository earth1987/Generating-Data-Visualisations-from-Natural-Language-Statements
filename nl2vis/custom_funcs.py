"""Custom code that gets used across more than notebook"""
import bz2
import pickle

### Pickle a file and then compress it
# Source: https://betterprogramming.pub/load-fast-load-big-with-compressed-pickles-5f311584507e
def save_compressed(fpath, data):
  """Pickle a file and then compress it."""
  with bz2.open(fpath, "wb") as f: 
    pickle.dump(data, f)

# Load compressed pickle file
# Source: https://betterprogramming.pub/load-fast-load-big-with-compressed-pickles-5f311584507e
def load_compressed(fpath):
  """Load a compressed pickle file"""
  with bz2.open(fpath, "rb") as f: 
    data = pickle.load(f)
  return data

### Save uncompressed pickle file
# Note: wb = write binary
# Source: https://www.programiz.com/python-programming/file-operation
# Source: https://realpython.com/python-pickle-module/
# Source: https://ianlondon.github.io/blog/pickling-basics/
def save_pickle(fpath, data):
  """Save an uncompressed pickle file"""    
  with open(fpath, 'wb') as f:
    pickle.dump(data, f)
        
### Load uncompressed pickle file
# Note: rb = read binary
# Source: https://www.programiz.com/python-programming/file-operation
# Source: https://realpython.com/python-pickle-module/
# Source: https://ianlondon.github.io/blog/pickling-basics/
def load_pickle(fpath):
  """Load an uncompressed pickle file"""
  with open(fpath, 'rb') as f:
    data = pickle.load(f)
  return data

def set_directories(platform, organisation, model_type):
    """Set relevant directories on colab, hpc and laptop"""

    if platform == 'colab':
        
        # Model and tokenizer directory
        model_directory = organisation + "/" + model_type
        local_model_directory = "/content/drive/MyDrive/Colab Notebooks/2. Models/Autoregressive LMs/" + model_type
        
        # Prompt and results directory
        prompt_directory = "/content/drive/MyDrive/Colab Notebooks/3. Results/Prompts/"
        results_directory = "/content/drive/MyDrive/Colab Notebooks/3. Results/" + model_type + "/"
        
        # Json schema directory
        schema_directory = "/content/drive/MyDrive/Colab Notebooks/3. Results/" + model_type + "/"
        
    elif platform =='hpc':
        
        # Model and tokenizer directory (archive folder)
        archive_folder = "/mnt/data/users/adbz866/"
        local_model_directory = archive_folder + model_type
    
        # Prompt and results directory (scratch folder)
        prompt_directory = "/mnt/scratch/users/adbz866/"
        results_directory = "/mnt/scratch/users/adbz866/"
        
        # Json schema directory
        schema_directory = "/mnt/scratch/users/adbz866/"
        
    return prompt_directory, results_directory, schema_directory, local_model_directory