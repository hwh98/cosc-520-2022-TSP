## **Introduction**
The travelling salesman problem is a canonical computational problem and gained intense
research interest over the decades. We will state the travelling salesman problem along with
some terminologies here, along with some preliminary analysis of the algorithm

---

## **The Dynamic Programming Algorithm for TSP**

We define a graph $G = (V, E)$, a weighted undirected graph, then we consider the recursive table: 

$$
\begin{aligned}
    C(S, i, j) := \min_{p\in \mathcal P}
    \left\lbrace
        |p|: p:(i \rightarrow j), \forall v \in S, v \in p
    \right\rbrace, 
\end{aligned}
$$

where it denotes the minimum length of the path going form the vertex $i$ to $j$ visiting every vertex in the set $S$. We define the basecase for all the $|S| = 2$, in which case we have: 

$$
\begin{aligned}
    C(\{i, j\}, i, j) = c(i, j)\quad \forall i, j\in E, i\neq j, 
\end{aligned}
$$

And the main part of the algorithm started like: 

* For $k = 3...N$ do: 
  * For all $|S| = k, S \subseteq V$, DO: 
    * $C(S, i, j) :=\min_{l \in S\setminus \{i, j\}}\{C(S\setminus \{j\}, i, l) + c(l, j)\}$ for all $i ,j \in S; i < j$

#### **Subsets Generator**

* Encode each of the subset of a set of size $n$ into an integer in $[0, 2^n]$. 

### **Implementations Issues and How they Are Addressed**

* 

---
## **The Branch and Bound Algorithm with Minimum Spanning Tree for TSP**

The branch and bound algorithm is based on the principle that we cut off the subset of the solution, e.g: feasible suboptimal solution, that is, the total set of feasible solutions is partitioned into smaller subset of solution. 
The total number of possible solutions is reduced by the branching process, and the smaller subsets can then be evaluated systematically until the best solution is found. 
At the heart of the method, we'll see one of the things we keep track of is the bound. We'll keep track of what a lower bound is or, in other words, the best solution could possibly be. And the bound guarantees that we can solve each sub-problem and find the global optimal. Generally speaking, the branching strategy and the bound calculation of the node can be obtained in any way. Here, we will use the Minimum Spanning Tree algorithm, which is able to yield an undirected path that connects all the vertices together at the lowest cost, to calculate the lower bound on the cost of the tour and the vertex with the highest degree is the one we branch on in the next step.


To sum up, it stepwise enumerates all the possible candidate solutions by exploring the search space by the means of a decision tree.
In each node, we will branch and constraint to achieve the sub-problem in the next level, and we will calculate the bound of the following splitted node to see if the feasible solution is better than the solution we found so far to decide whether to update the best solution. 


The notation of the algorithm is as followed:

 * $G = (V,E)$ the input undirected graph of TSP.
 * $c : E  \rightarrow  R$ is the weight of the edge should be non-negative.
 * $P \subseteq E$ the path P is the set of edge E.
 * $MST()$ is the minimum spannign tree algorithm, and the $MST(E')$ refer to the algorithm in the subgraph $G(V,E')$
Our goal is to find the path(tour) that will visited each vertex exactly once.

The algorithm for finding the solution tour for TSP is as follow:
1. Set $C*$ as being undefined.
2. Initialized a stack with ${E}$ randomly.
3. WHILE stack is no-empty DO
    - Take and remove an item from the stack and call it $E'$
    - IF the graph $G(V,E')$ is not connected, goto(3)
    - Compute $T := MST(E')$
    - IF T is a path and $c(T) < c(C*) or C* undeined$ 
        THEN update $C* := T and goto (3)
    - IF $T$ is a path and $c(T) >= c(C*)$ 
        THEN goto (3)
    - Let $v \in V$ be a node that is incident to at least 3 edges in $T$
    - Let $e1, e2, e3 \subseteq \delta(V) \bigcap T$ be 3 edges that are incident to $v$ in $T$
    - Put the $E'$ {e1}, $E'$ {e2}, $E'$ {e3} on the stack
12. Return $C*$

### Installation instruction for this algorithm. 

(npm libs) lodash, jest, jest-regex-util , python(for python httpserver, ...)

---
### **Reference and Sources**

We make use of the 2 of the other repos to suppport our project: 
1.[A dynamic programming approach to sequencing problems](https://epubs.siam.org/doi/abs/10.1137/0110015?journalCode=smjmap.1)
2. Jon Kleinberg and Éva Tardos. Algorithm design. MTM, 2022

We make use of other sources to suppport our project:
3. [JS graph algorithms](https://github.com/chen0040/js-graph-algorithms)
4. [JS LP algorithm](https://github.com/JWally/jsLPSolver)
5. [JS Graph And graph Algorithm](https://github.com/dagrejs/graphlib/wiki#browser-scripts)
