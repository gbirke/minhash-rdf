""" This script tests the speed of the hashing for various tokens."""

import sys
import random
import timeit
import pyhash
import shingles
import config

# how many token samples should be taken from input file
sample_length = 100000

# How many times the samples should be iterated
num_repeats = 100

if len(sys.argv) < 2:
    print "You must give a data source as argument!"
    sys.exit(1)

avg_length = {}
samples = {}
with open(sys.argv[1], "r") as src:
    for shingle_type in config.SHINGLE_CONFIG:
        src.seek(0)
        shingle_generator_func = getattr(shingles, "{}_tokenizer".format(shingle_type))
        tokens = list(shingle_generator_func(src, 1))
        token_length = len("".join(tokens))
        avg_length[shingle_type] = token_length / len(tokens)
        samples[shingle_type] = tokens[:sample_length]

def get_sample_hash_func(samples):
    hasher = pyhash.city_64()
    def fnc():
        for s in samples:
            h = hasher(s)
    return fnc

# normalize samples length if the input file is too small
smallest_sample = min([len(samples[t]) for t in samples] + [sample_length])
for s in samples:
    samples[s] = samples[s][:smallest_sample]

num_hashes = smallest_sample*num_repeats
for shingle_type in config.SHINGLE_CONFIG:
    execution_time = timeit.timeit(get_sample_hash_func(samples[shingle_type]), number=num_repeats)
    hashes_per_second = num_hashes / execution_time
    print "Hashing {} {:6} strings with avg. length {:4} took {:3.3f} seconds ({:2.1f} MHashes/s).".format(
        num_hashes, 
        shingle_type, 
        avg_length[shingle_type], 
        execution_time,
        hashes_per_second / 1000
    )