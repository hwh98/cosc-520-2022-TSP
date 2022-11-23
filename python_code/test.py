from core import k_combinatorics, k_subsets, DynamicTSP, scipy



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


def Test3():
    # make cost table.
    c = {}
    c[0, 1] = c[1, 2] = c[2, 3] = c[3, 0] = 1
    c[0, 2] = 1.2
    c[3, 1] = 1.2
    global dtsp
    dtsp = DynamicTSP(c)
    for k, v in dtsp.ctable.items():
        print(f"{k} |-> {v}")
    dtsp.construct_subset()
    for k, v in dtsp.ctable.items():
        print(f"{k} |-> {v}")
    dtsp.construct_subset()
    for k, v in dtsp.ctable.items():
        print(f"{k} |-> {v}")
    return True


def run_tests():
    results = []
    tests = [Test1, Test2, Test3]
    for test in tests:
        results.append(test())
    for fxn, result in zip(tests, results):
        print(f"{fxn.__name__}: {'Passed' if result else 'Failed'}")


if __name__ == "__main__":
    run_tests()