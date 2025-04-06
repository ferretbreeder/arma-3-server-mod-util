import hashlib
import shutil

# builds a dictionary using the specially-formatted modlist.csv
def csv_dict_builder(file):

    mod_dictionary = {}

    with open(file, 'r') as f:

        for line in f:
            values = line.strip().split(',')
            mod_dictionary[values[0]] = values[1]
    
    return mod_dictionary

# generates a hash from the metadata file in a mod's folder
def hash_gen(file):
    with open(file, 'b+r') as f:
        bytes = f.read()
        return hashlib.md5(bytes).hexdigest()

# generates a list of folder paths that will grab the directory of the local machine that a specific mod will be copied
# from
def key_folder_path_generator(base_path, mod_dict):

    key_file_paths = []

    for key in mod_dict.keys():
        key_file_paths.append(base_path.strip("\"") + "\\" + key)

    return key_file_paths

# generates a list of folder paths that will grab the directory of the remote machine that a specific mod will be copied
# to
def value_folder_path_generator(base_path, mod_dict):

    value_file_paths = []

    for value in mod_dict.keys():
        value_file_paths.append(base_path.strip("\"") + "\\" + mod_dict[value])

    return value_file_paths

# generates a list of file paths that will be used to generate hashes to compare necessary files from the source directory
def key_file_path_generator(base_path, mod_dict):

    key_file_paths = []

    for key in mod_dict.keys():
        key_file_paths.append(base_path.strip("\"") + "\\" + key + "\\meta.cpp")

    return key_file_paths

# generates a list of file paths that will be used to generate hashes to compare necessary files from the remote directory
def value_file_path_generator(base_path, mod_dict):

    value_file_paths = []

    for value in mod_dict.keys():
        value_file_paths.append(base_path.strip("\"") + "\\" + mod_dict[value] + "\\meta.cpp")

    return value_file_paths

# checks the hashes of two files to see if an update is needed
def hash_compare(file_hash_1, file_hash_2):

    if hash_gen(file_hash_1) == hash_gen(file_hash_2):
        return True

# def mod_copy(local_path, server_path, mod_dictionary):
#
#     src_folders = []
#     dst_folders = []