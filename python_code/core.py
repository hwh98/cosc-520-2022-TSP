"""
Author's Name: Hongda Li

This is a script for the final project for COSC 520 2022 Winter Term1, at UBC Okanagan.
"""

def k_combinatorics(n, k):
    """
    Function makes a generator for all subset of size k in a subset of size n.

    :param int n: The size of the set we are looking at.
    :param int k: The size subsets from this set that you want to choose from.
    :raise Exception: Error when k > n.
    """
    if not (isinstance(n, int) and isinstance(k, int)):
        raise Exception("The given n, k: {n}, {k} is not both an instance of integers.")
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


def k_subsets(s, k):
    """
        Given the set s, generate all possible subset of set s, with size k, assuming that the elements in the set
        s are unique.
        NOTE: The ordering of the elements from the original set to the subset is PRESERVED.
    :param s:
        Something indexable.
    :param k:
        int.
    :return:
        it yields.
    """
    for comb in k_combinatorics(len(s), k):
        yield [s[idx] for idx in comb]
    return

def rand_full_undigraph_euclidean(N):
    """
        Generator a full graph whose vertices are euclidean points in the space.The points are uniform random
        on the unit square.
    :param N:
        The number of points we looking at
    :return:
    """
    pass


class DynamicTSP:
    """
    This class contains the dynamic programming algorithm for the traveling salesman problem. It's interative and
    has nice interface for visualizations and stuff.

    Attributes
    ------
    ptable: dict
        A dictionary that maps a subset of vertices S and a set of vertices {i, j} to the shortest path the goes from
        i -> j using all vertices in set S exactly once.
        Expected Types:
        (sorted list, tuple of the directed edge) |-> List of integers of the path

    ctable: dict
        A dictionary that maps subset of vertices S and a set of vertices {i, j} in the graph to the cost of the
        shortest path that goes from i -> j through every vertex in S exactly once.
        (sorted list, tuple of the directed edge) |-> Integers representing the cost.
    v:
        This is the list of vertices in the graph.
    """
    def __init__(this, cost_table):
        assert isinstance(cost_table, dict), "Give DynamicTSP an instance of dictionary as cost table please."
        this.c = cost_table
        this.ptable = {}
        this.ctable = {}
        this.v = None
        this.k = 0
        this.construct_base()

    def construct_base(this):
        """
            The base case is when the set S has size of 2, containing only 2 vertices. In this case the cost of the path
            that goes from i to j is just the cost of the edges linking i, j.
        :return:
            None.
        """
        vertices = set()
        for e, cost in this.c.items:
            this.ctable[tuple(sorted(e)), tuple(e)] = cost
            this.ptable[tuple(sorted(e)), tuple(e)] = list(e)
            vertices.add(e[1]); vertices.add(e[2])
        assert all([isinstance(item, int) for item in this.v]), "The cost table is giving identifiers for vertices " \
                                                                "that are not integers."
        this.v = sorted(vertices)
        this.k = 2
        return None

    def construct_subset(this):
        """
            Make a subset of size k for the dynamic table in the field: this.ctable, this.ptable.
        :param k:
            The size of the subset to generated on
        :return:
            None
        """
        ptable = {}
        ctable = {}
        for S in k_subsets(this.v, this.k + 1):                      # S is a sorted array.
            for idx1 in range(len(this.v)):
                for idx2 in range(len(this.v)):
                    i, j = this.v[idx1], this.j[idx2]
                    if i == j:
                        continue                                     # skip.
                    min_cost = float("inf"); min_path = None
                    for l in set(S) - set([i, j]):                   # min path going from i -> l -> j
                        T = tuple(set(S) - set([j]))
                        cost = this.ctable[T, (i, l)] + this.c[l, j]
                        if cost < min_cost:
                            min_path = this.ptable[T, (i, l)] + [l, j]
                            min_cost = min_cost
                    ctable[tuple(S), (i, j)] = min_cost
                    ptable[tuple(S), (i, j)] = min_path
        this.ptable = ptable
        this.ctable = ctable
        this.k = this.k + 1
        return this



        return None

    def perform(this, verbosity):
        """
        Perform the algorithm and print out stuff for checking.
        :return:

        """
        pass




def main(name):
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("The TSP Dynamic programming module is being loaded. ")
    main('PyCharm')



