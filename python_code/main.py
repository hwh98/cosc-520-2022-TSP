

def k_combinatorics(n, k):
    """
    Function makes a generator for all subset of size k in a subset of size n.

    Parameters
    ------
    n: int
        The size of the set we are looking at.
    k: int
        The size subsets from this set that you want to choose from.
    Raise
    -----
        Error when k > n.
    """
    if not (isinstance(n, int) and isinstance(k, int)):
        raise f"The given n, k: {n}, {k} is not both an instance of integers."
    assert n >= k, f"k_combinator expects k <= n but have {k} <= {n}. "

    def inner_recur(a, k, start_at, already_chosen):
        if k == 0:
            yield list(already_chosen)
            return
        n = len(a)
        for I in range(start_at, n - k + 1):
            already_chosen.append(a[I])
            yield from inner_recur(a, k - 1, I + 1, already_chosen)
            already_chosen.pop()
        return

    yield from inner_recur([I for I in range(n)], k, 0, [])


class DynamicTSP:
    """
    This class contains the dynamic programming algorithm for the traveling salesman problem. It's interative and
    has nice interface for visualizations and stuff.

    Attributes
    ------
    ptable: dict
        A dictionary that maps a subset of vertices S and a set of vertices {i, j} to the shortest path the goes from
        i -> j using all vertices in set S exactly once.
    ctable
    """
    def __init__(this, cost_table):
        assert isinstance(cost_table, dict), "Give DynamicTSP an instance of dictionary as cost table please."
        this.ptable = {}
        this.ctable = {}
        pass




def main(name):
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("The TSP Dynamic programming module is being loaded. ")
    main('PyCharm')


