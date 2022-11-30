"""
Author's Name: Hongda Li

This is a script for the final project for COSC 520 2022 Winter Term1, at UBC Okanagan.
"""

from tqdm import tqdm
from warnings import warn
import scipy
import matplotlib.pyplot as plt
import numpy as np
import math
import itertools

VERBOSE:bool = True   # The global verbose settings. Boolean.


def k_combinatorics(n:int, k:int):
    """
    Function makes a generator for all subset of size k in a subset of size n. The same function is in the itrtools.

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


def k_subsets(s, k:int):
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


def min_argmin(d:dict):
    """
        Given a dictionary, it terates over all the values and find that keys with the minimum values. None
        if there is no key.
    :param d:
        a dictionary with values that is a number.
    :return:
        the key with the maximum values.
    """
    min_value = None
    min_key = None
    for k, v in d.items():
        if min_value is None or v < min_value:
            min_value = v
            min_key = k
    return min_key, min_value


class SimpleEuclideanPoints:
    """
    This class models 2d points with Euclidean metrics. Each vertex is a coord and we have a full graphy by
    making edges between all of them. Giving us N^2/2 many edges for N number of points.
    """

    def __init__(this, N=10):
        """
            Constructor.
        :param N:
            The number of points we want.
        :return:
            This instance.
        """
        this.v = [I for I in range(N)]
        this.n = N
        this.vlabels = None
        this.edges = list(k_subsets(this.v, 2)) # All undirected edges are ordered pairs.
        this.__cost = None

        if N >= 50:
            warn(f"N={N} is very huge and this is not good for constructing a full graph and solving TSP on it. ")

    def __make(this, xs, ys):
        """
        Private method for establishing the field of an instance of this class.
        :param coordx:
        :param coordy:
        :return:
        """
        d = lambda x1, y1, x2, y2: math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        c = {}
        labels = dict((v, (xs[v], ys[v])) for v in this.v)
        for v1, v2 in this.edges:
            x1, y1 = labels[v1]
            x2, y2 = labels[v2]
            c[v1, v2] = d(x1, y1, x2, y2)
        this.__cost = c
        this.vlabels = labels
        return this

    def circle(this):
        """
            Arrange all the points into a circle and update all the distance between the points.
        :return:
            itself modified.
        """
        t = np.linspace(0, 2*np.pi, this.n + 1)[:-1]
        xs = np.cos(t)
        ys = np.sin(t)
        return this.__make(xs, ys)


    def random_pts(this):
        """
            Construct random points in the unit square in the positive quadrants.
        :return:
            itself modified.
        """
        rand = np.random.rand
        xs, ys = rand(this.n), rand(this.n)
        return this.__make(xs, ys)


    @property
    def c(this):
        """
        The cost table.
        :return:
            The cost table copied.
        """
        if this.__cost is None:
            return None
        return this.__cost.copy()

    def visualize_subgraph(this, edges):
        """
            Given a set of edges, visualize the subgraph and plot it on a window or something.
        :param edges:
            a list of tuples.
        :return:
            the instance itself.
        """
        # TODO: Test this functions.
        assert edges is not None, "Can't plot None, please check what you passed into visualize_subgraph. "
        coordxs = [this.vlabels[0][0]]
        coordys = [this.vlabels[0][1]]
        for _, v in edges:
            coordxs.append(this.vlabels[v][0])
            coordys.append(this.vlabels[v][1])
        plt.plot(coordxs, coordys)
        plt.scatter(coordxs, coordys)
        for id in this.v:
            txt = str(id)
            plt.annotate(txt, this.vlabels[id], color='red')
            pass
        plt.show()
        return this


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
        c = {}          # a new, digested edge cost table, all edges must be ordered pairs.
        for e, cost in this.c.items():
            c[tuple(sorted(e))] = this.ctable[tuple(sorted(e)), tuple(sorted(e))] = cost
            this.ptable[tuple(sorted(e)), tuple(sorted(e))] = list(e)
            vertices.add(e[0]); vertices.add(e[1])
        this.v = sorted(vertices)
        assert all([isinstance(item, int) for item in this.v]), "The cost table is giving identifiers for vertices " \
                                                                "that are not integers."
        this.c = c
        this.k = 2
        return None

    def construct_subsets(this):
        """
            Make a subset of size k for the dynamic table in the field: this.ctable, this.ptable.
        :param k:
            The size of the subset to generated on
        :return:
            None
        """
        if this.k == len(this.v):
            return this
        ptable = {}
        ctable = {}
        k = this.k
        v = this.v

        def has_edge(i, j):
            return tuple(sorted([i, j])) in this.c

        def C(S, i, j): # recursion table.
            return this.ctable[S, tuple(sorted([i, j]))]

        def P(S, i, j): # get path
            return this.ptable[S, tuple(sorted([i, j]))]

        def edge_cost(i, j):
            return this.c[tuple(sorted([i, j]))]

        if VERBOSE:
            gen = tqdm(list(k_subsets(v, k + 1)))
        else:
            gen = tqdm(k_subsets(v, k + 1))
        for S in gen:
            for i, j in k_subsets(S, 2):                         # i < j
                min_cost = float("inf")
                min_path = None                                  # new optimal
                for l in set(S) - set([i, j]):                   # min path going from i <-> l <-> j with size k + 1
                    T = tuple(sorted(set(S) - set([j])))         # S\{j}
                    if not has_edge(l, j):                       # ignore this path.
                        continue
                    cost = C(T, i, l) + edge_cost(l, j)
                    if cost < min_cost:
                        min_path = P(T, i, l) + [j]
                        min_cost = cost
                ctable[tuple(S), (i, j)] = min_cost
                ptable[tuple(S), (i, j)] = min_path
                if min_path is None:
                    raise Exception("The graph is disconnected.")
        this.ptable = ptable
        this.ctable = ctable
        this.k = this.k + 1
        return this

    def perform_all(this):
        """
            Perform the search on the optimal path by looking constructing spanning paths for all subsets and then
            in the end find the optimal tour that go through every paths.
        :param verbose
            Use slightly more memory to get print out for the algorithm so we know what progress we are having.
        :return:
            A list of vertices indicating the optimal path.
        """
        def edge_cost(i, j): return this.c[tuple(sorted([i, j]))]
        n = len(this.v)
        gen = tqdm(range(3, n + 1)) if VERBOSE else range(3, n + 1)
        for k in gen:
            if VERBOSE:
                print(f"Constructing all Spanning paths of length k={k}.")
            this.construct_subsets()
        full_paths = {}                 # maps the paths to their lengths
        for (S, e), p in this.ptable.items():
            full_paths[tuple(p + [p[0]])] = this.ctable[S, e] + edge_cost(e[0], e[1])

        return min_argmin(full_paths)


def main(name):
    import test
    test.run_tests()




if __name__ == '__main__':
    # Press the green button in the gutter to run the script.
    print("The TSP Dynamic programming module is being loaded. ")
    main('PyCharm')



