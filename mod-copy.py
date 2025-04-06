# used mostly from the comfort of my own home to keep my own mods updated on my Arma 3 server
#
import dotenv
import os
from functions import *

# define path variables from values
dotenv.load_dotenv()
local_path = os.getenv('local_path').strip("r")
server_path = os.getenv('server_path').strip("r")

# define the set of mods to work from
mod_dictionary = csv_dict_builder('modlist.csv')

# used for debugging. will be removed.
print(key_folder_path_generator(local_path, mod_dictionary))
print(value_folder_path_generator(server_path, mod_dictionary))