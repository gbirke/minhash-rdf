import glob
import pickle
import os.path

import minhash
import config

result_data = {}

if len(sys.argv) < 2:
    data_dir = "test_data"
else:
    data_dir = sys.argv[1]

for change_rate in config.CHANGE_RATES:
    result_data[change_rate] = {}
    for shingle_type in config.SHINGLE_CONFIG:
        result_data[change_rate][shingle_type] = {}
        for size in config.SHINGLE_CONFIG[shingle_type]:
            a_file = os.path.join(data_dir, "instance_types_{}_{:02}.p".format(shingle_type, size))
            b_file = os.path.join(data_dir, "instance_types_{:02}_{}_{:02}.p".format(change_rate, shingle_type, size))
            with open(a_file, "rb") as a_data, open(b_file, "rb") as b_data:
                a = pickle.load(a_data)
                b = pickle.load(b_data)
                similarity = minhash.minhash_signatures(a["hashes"], b["hashes"])
                result_data[change_rate][shingle_type][size] = "{:.2f}".format(similarity * 100)

for change_rate in result_data:
    print change_rate, result_data[change_rate]