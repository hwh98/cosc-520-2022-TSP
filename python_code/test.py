from core import k_combinatorics, k_subsets, DynamicTSP, scipy, SimpleEuclideanPoints



def Test1():
    """
    Test basics functionality of the k_combinatorics sets with 2 concrete examples.
    :return:
    True means we passed it, else we didn't.
    """
    g = k_combinatorics(5, 3)
    assert len(list(g)) == 10, "k_combinatorics failed on instance (k=3, n=5)."
    g = k_combinatorics(5, 2)
    assert len(list(g)) == 10, "k_combinatorics failed on instance (k=2, n=5)"
    print("Test1 Passed. ")
    return True


def Test2():
    """
    Test of the binomial coefficient properties are all satisfied for a set of size 5.
    :return:
    True means we passed it, else we didn't.
    """
    b = scipy.special.binom
    for k in range(1, 6):
        g = k_combinatorics(5, k)
        assert len(list(g)) == b(5, k), f"k_combinatorics failed for case (k={k},n={5}). "
    print("Test2 passed. ")
    return True


def DynamicTSPTestBasic():
    # make cost table.
    c = {}
    c[0, 1] = c[1, 2] = c[2, 3] = c[3, 0] = 1
    c[0, 2] = 1.2
    c[3, 1] = 1.2
    global DTSP
    DTSP = DynamicTSP(c)
    DTSP.construct_subsets()
    DTSP.construct_subsets()
    print("======== DTSP Simple Tests =========== ")
    for k, v in DTSP.ctable.items():
        print(f"{k} |-> {v}")
    ctable = DTSP.ctable
    assert ctable[(0, 1, 2, 3), (0, 1)] == 3, "Something wrong is with test3, for DynamicTSP. "
    return True


def SimpleGraphTest():
    global SEUP
    N = 10
    SEUP = SimpleEuclideanPoints(N)
    dtsp = DynamicTSP(SEUP.circle().c)
    for itr in range(N - 2):
        dtsp.construct_subsets()
    for k, v in dtsp.ctable.items():
        print(f"({k}, v) |-> {v}")
    return True





def run_tests():
    results = []
    tests = [Test1, Test2, DynamicTSPTestBasic, SimpleGraphTest]
    for test in tests:
        results.append(test())
    for fxn, result in zip(tests, results):
        print(f"{fxn.__name__}: {'Passed' if result else 'Failed'}")




if __name__ == "__main__":
    run_tests()