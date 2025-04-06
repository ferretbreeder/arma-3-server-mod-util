"""
This module provides utility functions for managing and synchronizing mod files
between a local machine and a remote server for an Arma 3 server. It includes
functions for reading and processing a CSV file containing mod mappings, generating
file paths, creating MD5 hashes for file comparison, and copying updated mod files
to the remote server.

Functions:
- csv_dict_builder(file): Reads a CSV file and creates a dictionary mapping local mod
  folder names to their remote counterparts.
- hash_gen(file): Generates an MD5 hash for a given file.
- key_folder_path_generator(base_path, mod_dict): Generates a list of local mod folder
  paths based on the provided base path and mod dictionary.
- value_folder_path_generator(base_path, mod_dict): Generates a list of remote mod
  folder paths based on the provided base path and mod dictionary.
- key_file_path_generator(base_path, mod_dict): Generates a list of file paths to
  meta.cpp files on the local machine for hash comparison.
- value_file_path_generator(base_path, mod_dict): Generates a list of file paths to
  meta.cpp files on the remote machine for hash comparison.
- hash_compare(file_hash_1, file_hash_2): Compares the MD5 hashes of two files to
  determine if they are identical.
- mod_copy(local_path, server_path, mod_dictionary): Compares mod files between the
  local and remote machines and copies updated mods to the remote server if needed.

This module is designed to streamline the process of keeping mods up-to-date on a
remote Arma 3 server by automating file comparison and synchronization tasks.
"""

import hashlib
import shutil

# modlist.csv needs to be in the same directory that this program is running from
# it needs to be named 'modlist.csv' specifically, and it needs to be formatted
def csv_dict_builder(file):

    """
    creates a dictionary and populates it with key value pairs sourced from
    modlist.csv in the project directory

    Args:
        file: a CSV file containing the folder names of the mods on the local machine
        in column #1 and the names of the folders on the remote machine in column #2

    Returns:
        a dictionary containing key-value pairs of the folders names for mods installed
        locally and their remote counterparts
    """

    mod_dictionary = {}

    with open(file, 'r', encoding='utf8') as f:

        for line in f:
            values = line.strip().split(',')
            mod_dictionary[values[0]] = values[1]

    return mod_dictionary

# in this case, MD5 hashes are generated based on a file in each
# mod folder called meta.cpp. These files are small, so there is
# little risk of eating up system resources in reading them into
# memory entirely to generate the hash
def hash_gen(file):

    """
    generates a hash from the metadata file in a mod's folder

    Args:
        file: an accessible file that the MD5 hash will be generated from

    Returns:
        an MD5 hash based on the processed file
    """

    with open(file, 'b+r') as f:
        file_bytes = f.read()
        return hashlib.md5(file_bytes).hexdigest()


def key_folder_path_generator(base_path, mod_dict):

    """
    generates a list of folder paths that will grab the
    directory of the local machine that a specific mod
    will be copied from

    Args:
        base_path: the folder containing all of the mods on the local machine
        populated in the .env file
        mod_dict: a dictionary containing names of the specific mod folders and
        their corresponding folders on the remote server

    Returns:
        a list of folders ready to be copied to the remote server
    """

    key_folder_paths = []

    for key in mod_dict.keys():
        key_folder_paths.append(base_path.strip("\"") + "\\" + key)

    return key_folder_paths

# generates a list of folder paths that will point to the
# directory on the remote machine that a specific mod
# will be copied to
def value_folder_path_generator(base_path, mod_dict):

    """
    generates a list of folder paths from the folders in the mod
    folder on the remote server to know where to copy new files to

    Args:
        base_path: the main mod folder on the remote server
        mod_dict: a dictionary containing names of the specific mod folders and
        their corresponding folders on the remote server

    Returns:
        a list of folders ready to be overwritten with files from the local machine
        if needed
    """

    value_file_paths = []

    for value in mod_dict.keys():
        value_file_paths.append(base_path.strip("\"") + "\\" + mod_dict[value])

    return value_file_paths

# generates a list of file paths that will be used to generate
# hashes to compare necessary files from the source directory
def key_file_path_generator(base_path, mod_dict):

    """
        generates a list of file paths that correspond to the meta.cpp files
        from the local machine

        Args:
            base_path: the folder containing all of the mods on the local machine
            populated in the .env file
            mod_dict: a dictionary containing names of the specific mod folders and
            their corresponding folders on the remote server

        Returns:
            a list of files to be used to check if mods have been updated and need to
            be copied
        """

    key_file_paths = []

    for key in mod_dict.keys():
        key_file_paths.append(base_path.strip("\"") + "\\" + key + "\\meta.cpp")

    return key_file_paths

# generates a list of file paths that will be used to generate
# hashes to compare necessary files from the remote
# directory. I'm using meta.cpp because it contains a timestamp
# for when the mod was published, which should update with
# every new release of the mod.
def value_file_path_generator(base_path, mod_dict):

    """
    generates a list of file paths that correspond to the meta.cpp files
    from the remote machine

    Args:
        base_path: the folder containing all of the mods on the remote machine
        populated in the .env file
        mod_dict: a dictionary containing names of the specific mod folders and
        their corresponding folders on the remote server

    Returns:
        a list of files to be used to check if mods have been updated and need to
        be copied
    """

    value_file_paths = []

    for value in mod_dict.keys():
        value_file_paths.append(base_path.strip("\"") + "\\" + mod_dict[value] + "\\meta.cpp")

    return value_file_paths

# checks the hashes of two files to see if an update is needed
def hash_compare(file_hash_1, file_hash_2):

    """
    compare the MD5 hashes generated from two different files

    Args:
        file_hash_1: a mod.cpp file (from the local machine in this case)
        file_hash_2: a mod.cpp file (conversely, from the remote machine)

    Returns:
    True or False
    """

    return bool(hash_gen(file_hash_1) == hash_gen(file_hash_2))

# generates paths to files to compare, paths to folders to
# copy if necessary, and iterates through lists of files and
# compares the hashes of those files to check if updates are needed
def mod_copy(local_path, server_path, mod_dictionary):

    """
    where the magic happens. Takes the lists generated by all of the other functions
    in this module and uses them to determine which mods need to be updated, and then
    uses that information to copy select mods from the local machine to the remote machine
    if needed.

    Args:
        local_path: the path to the mod folder on the local machine. populated in the .env
        file
        server_path: the path to the mod folder on the remote machine. populated in the .env
        file
        mod_dictionary: a dictionary containing names of the specific mod folders and
        their corresponding folders on the remote server

    Returns:
        nothing, but currently prints "status updates" to the console
    """

    src_folders = key_folder_path_generator(local_path, mod_dictionary)
    dst_folders = value_folder_path_generator(server_path, mod_dictionary)
    local_files = key_file_path_generator(local_path, mod_dictionary)
    remote_files = value_file_path_generator(server_path, mod_dictionary)

    for i in range(len(local_files)):
        if hash_gen(local_files[i]) == hash_gen(remote_files[i]):
            print("Hashes match, no updates")
            i += 1
        else:
            shutil.copytree(src_folders[i], dst_folders[i], dirs_exist_ok=True)
            print("update needed... done")
            i += 1

    print("copy complete")
