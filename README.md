### **Intro**

This repo is for the final project of COSP 520 2022 Winter Term 1. We are doing something about the Traveling Salesman Problem. 



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
    * $C(i, j, S) :=\min_{l \in S\setminus \{i, j\}}\{C(S\setminus \{j\}, i, l) + c(l, j)\}$

#### **Subsets Generator**

* Encode each of the subset of a set of size $n$ into an integer in $[0, 2^n]$. 

---
## **The Branch and Bound Algorithm with Minimum Spanning Tree for TSP**

The branch and bound algorithm is based on the principle that we cut off the subset of solution, e.g: feasible suboptimal solution, that is, the total set of feasible solution is partitioned into smaller subset of solution. The smaller subsets can then be evaluated systematically until the best solution is found. 
To sums up, it stepwise enumerate all the possible candidate solution by exploreing the search space by the means of a decision tree.
In each node, we will branch and constraint to achieve the sub-problem in the next level, and we will calculate the bound of the following splitted node to see if the feasible solution is better than the solution we found so far to decide whether to update best solution. 
In general, the branching strategy and the bound calcuation of the node can be obtained in any way. 
Here, we will use the Minmum Spanning Tree algorithm to decide which vertex we branch on.

The notation of the algorithm is as followed:

 * $G$ = (V,E)$ the input undirected graph of TSP.
 * $c : E  \rightarrow  R$ is the weight of the edge should be non-negative.
 * $P \subseteq E$ the path P is the set of edge E.
 * $MST()$ is the minimum spannign tree algorithm, and the $MST(E')$ refer to the algorithm in the subgraph $G(V,E')$
Our goal is to find the path(tour) that will visited each vertex exactly once.

The algorithm for finding the solution tour for TSP is as follow:
1. Set $C*$ as being undefined.
2. Initialized a stack with ${E}# randomly.
3. WHILE stack is no-empty DO
    - Take and remove an item from the stack and call it $E'$
    - IF the graph $G(V,E') is not connected, goto(3)
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


---
### **Sources**

We make use of the 2 of the other repos to suppport our project: 
1. JS graph algorithms: [here](https://github.com/chen0040/js-graph-algorithms)
2. JS LP algorithm: [here](https://github.com/JWally/jsLPSolver)
3. JS Graph And graph Algorithm: [here](https://github.com/dagrejs/graphlib/wiki#browser-scripts)
