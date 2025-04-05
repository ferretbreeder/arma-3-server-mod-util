import hashlib

def csv_dict_builder(file):

    mod_dictionary = {}

    with open(file, 'r') as f:

        for line in f:
            values = line.strip().split(',')
            mod_dictionary[values[0]] = values[1]
    
    return mod_dictionary

def hash_gen(file):
    with open(file, 'b+r') as f:
        bytes = f.read()
        return hashlib.md5(bytes).hexdigest()