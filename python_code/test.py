from core import k_combinatorics
import scipy

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


if __name__ == "__main__":
    Test1()
    Test2()