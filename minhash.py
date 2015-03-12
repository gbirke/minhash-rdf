import pyhash
import sortedcontainers

def get_signature(A, k=200, hash_func=pyhash.city_64()):
    signature = sortedcontainers.SortedDict()
    for elm in A:
        elm_hash = hash_func(elm)
        if len(signature) < k and elm_hash not in signature:
            signature[elm_hash] = 1
        elif elm_hash < signature.iloc[-1] and elm_hash not in signature:
            signature.popitem()
            signature[elm_hash] = 1
    return signature.keys()

def minhash(A, B):
    SA = get_signature(A)
    SB = get_signature(B)
    num_matches = sum([hminA == hminB for hminA , hminB in zip(SA, SB)])
    max_len_set = min([len(SA), len(SB)])
    return float(num_matches)/float(max_len_set)
