

# How many change sets should be created and which amount of lines (in percent) should be changed.
CHANGE_RATES = [1] + range(5,55,5)

# What partitioning (shingling) strategies should be used and 
# how many overlapping tokens should be tried for each strategy
SHINGLE_CONFIG = {
#    "byte": [2, 4, 8, 16],
    "word":   [1, 2, 3, 5],
    "triple": [1, 2, 3, 5],
    "turtle": [1, 2, 3, 5]
}

# Sample size of MinHash, how many shashes should be stored in a signature
NUM_HASHES = 500