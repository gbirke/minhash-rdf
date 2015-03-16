#CHANGE_RATES = [1,3,5,8] + range(10,55,5)
#CHANGE_RATES = [1,5,10,25,50]
#CHANGE_RATES = range(1,11) + range(10,55,5)
CHANGE_RATES = range(1,35) + range(35,55,5)

SHINGLE_CONFIG = {
#    "byte": [2, 4, 8, 16],
    "word":   [1, 2, 3, 5],
    "triple": [1, 2, 3, 5],
    "turtle": [1, 2, 3, 5]
}

NUM_HASHES = 500