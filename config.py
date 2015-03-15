#CHANGE_RATES = [1,3,5,8] + range(10,55,5)
#CHANGE_RATES = [1,5,10,25,50]
#CHANGE_RATES = range(1,11) + range(10,55,5)
CHANGE_RATES = range(1,25) + range(25,55,5)

SHINGLE_CONFIG = {
#    "byte": [2, 4, 8, 16],
    "word":   [2, 3, 5],
    "triple": [2, 3, 5],
    "turtle": [2, 3, 5]
}

NUM_HASHES = 500