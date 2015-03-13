import os.path
import pickle
import glob

import shingles
import minhash




SHINGLE_CONFIG = {
    "byte": [6, 8, 12],
    "word": [3, 5, 8],
    "triple": [1, 2, 3, 5]
}

NUM_HASHES = 200

def hash_dir(dir_glob, shingle_type, shingle_size):
    shingle_generator_func = getattr(shingles, "{}_tokenizer".format(shingle_type))
    for filename in dir_glob:
        fn_root, fn_ext = os.path.splitext(filename)
        target_filename = "{}_{}_{:02d}.p".format(fn_root, shingle_type, shingle_size)
        with open(filename, "r") as src, open(target_filename, "wb") as dst:
            generator = shingle_generator_func(src, shingle_size)
            hashes = minhash.get_signature(generator, NUM_HASHES)
            data = {
                "shingle_type": shingle_type,
                "shingle_size": shingle_size,
                "hashes": set(hashes)
            }
            pickle.dump(data, dst)

for shingle_type in SHINGLE_CONFIG:
    for size in SHINGLE_CONFIG[shingle_type]:
        hash_dir(glob.glob("test_data/*.ttl"), shingle_type, size)
