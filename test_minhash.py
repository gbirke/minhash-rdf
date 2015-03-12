import minhash

def test_get_signature_returns_k_lowest_values():
    my_set = ("4", "2", "3", "1", "5", "99")
    sig1 = minhash.get_signature(my_set, 1, lambda x: x)
    assert set(sig1) == set(["1"])

    sig3 = minhash.get_signature(my_set, 3, lambda x: x)
    assert set(sig3) == set(["1", "2", "3"])

    assert set(minhash.get_signature(("99", "98"), 1, lambda x: x)) == set(["98"])


def test_minhash_same_sets():
    s1 = ("4", "2", "3", "1")
    s2 = ("1", "2", "3", "4")
    assert minhash.minhash(s1, s2) == 1.0

def test_minhash_different_sets():
    s1 = ("4", "2", "3", "1")
    s2 = ("5", "6", "7", "8")
    assert minhash.minhash(s1, s2) == 0

def test_minhash_similar_sets():
    s1 = ("4", "2", "3", "1")
    s2 = ("1", "2", "5", "6")
    assert minhash.minhash(s1, s2) == 0.25
