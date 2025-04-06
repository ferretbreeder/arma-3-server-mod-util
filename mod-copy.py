# used mostly from the comfort of my own home to keep
# my own mods updated on my Arma 3 server
# honestly I thought I would have more to put in this file,
# but I imagine that I'll have more to add when I add a GUI
# and potentially do some refactoring

import dotenv
import os
from functions import *

# define path variables from values
dotenv.load_dotenv()
local_path = os.getenv('local_path').strip("r")
server_path = os.getenv('server_path').strip("r")

# define the set of mods to work from
mod_dictionary = csv_dict_builder('modlist.csv')

mod_copy(local_path, server_path, mod_dictionary)