import os.path
import pickle
import glob
import sys
import time

import shingles
import minhash
import config


def hash_dir(dir_glob, shingle_type, shingle_size):
    shingle_generator_func = getattr(shingles, "{}_tokenizer".format(shingle_type))
    for filename in dir_glob:
        fn_root, fn_ext = os.path.splitext(filename)
        target_filename = "{}_{}_{:02d}.p".format(fn_root, shingle_type, shingle_size)
        with open(filename, "r") as src, open(target_filename, "wb") as dst:
            generator = shingle_generator_func(src, shingle_size)
            hashes = minhash.get_signature(generator, config.NUM_HASHES)
            data = {
                "shingle_type": shingle_type,
                "shingle_size": shingle_size,
                "hashes": set(hashes)
            }
            pickle.dump(data, dst)

if len(sys.argv) < 2:
    data_dir = "test_data"
else:
    data_dir = sys.argv[1]

for shingle_type in config.SHINGLE_CONFIG:
    for size in config.SHINGLE_CONFIG[shingle_type]:
        start = time.time()
        hash_dir(glob.glob(os.path.join(data_dir, "*.ttl")), shingle_type, size)
        end = time.time()
        print "generated signatures for {} shingles ({} tokens) in {:.2f} seconds.".format(shingle_type, size, end-start)
