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
    * $C(S, i, j) :=\min_{l \in S\setminus \{i, j\}}\{C(S\setminus \{j\}, i, l) + c(l, j)\}$ for all $i ,j \in S; i < j$

#### **Subsets Generator**

* Encode each of the subset of a set of size $n$ into an integer in $[0, 2^n]$. 

### **Implementations Issues and How they Are Addressed**

* 

---
## **The Branch and Bound Algorithm with Minimum Spanning Tree for TSP**

The branch and bound algorithm is based on the principle that we cut off the subset of the solution, e.g: feasible suboptimal solution, that is, the total set of feasible solutions is partitioned into smaller subset of solution. The smaller subsets can then be evaluated systematically until the best solution is found. 
At the heart of the method, we'll see one of the things we keep track of is the bound. We'll keep track of what a lower bound is or, in other words, the best solution could possibly be. And the bound guarantees that we can solve each sub-problem and find the global optimal.

To sum up, it stepwise enumerates all the possible candidate solutions by exploring the search space by the means of a decision tree.
In each node, we will branch and constraint to achieve the sub-problem in the next level, and we will calculate the bound of the following splitted node to see if the feasible solution is better than the solution we found so far to decide whether to update the best solution. 
In general, the branching strategy and the bound calculation of the node can be obtained in any way. 
Here, we will use the Minimum Spanning Tree algorithm to decide which vertex we branch on.


The notation of the algorithm is as followed:

 * $G = (V,E)$ the input undirected graph of TSP.
 * $c : E  \rightarrow  R$ is the weight of the edge should be non-negative.
 * $P \subseteq E$ the path P is the set of edge E.
 * $\text{MST}(\cdots)$ is the minimum spanning tree algorithm, and the $MST(E')$ refer to the algorithm in the subgraph $G(V,E')$
 * $C*$ is the best tour ever found.
Our goal is to find the tour that will visited each vertex exactly once, the algorithm is described in algorithm 2. While the pseudo code stated below is formulated as an iterative schem, in our implementation it's implemenedted with recursion to simplify variable in the scope.

$C^* := undefined$<br/>
$S :={E}$<br/>
**while** $S \neq \emptyset$ **do**<br/>
&nbsp; Take top $E' \in S$ <br/>
&nbsp; **if** $G(V,E')$ is disconnected **then** <br/>
&nbsp; &nbsp; **continue** {Prune by infeasibility}<br/>
&nbsp; **end if**<br/>
&nbsp; Compute $M:=MST(E')$<br/>
&nbsp; **if** $M$ is a spanning bath **then**<br/>
&nbsp; &nbsp; Let $T$ be th tour by joining the end points of th path $M$<br/>
&nbsp; &nbsp; **if** $C(T)<C$ **then**<br/>
&nbsp; &nbsp; &nbsp; $C^*:= T$ {New,better tour found}<br/>
&nbsp; &nbsp; **end if**<br/>
&nbsp; **if** $M$ is a path and $c(T) \ge c(C^*)$ **then**<br/>
&nbsp; &nbsp; **continue** {Pruned by sub-optimality}<br/>
&nbsp; **end if**<br/>
&nbsp; let $v \subset V$ be a vertex incident to at least 3 edges in $T$<br/>
&nbsp; Let $e_1, e_2, e_3 \subseteq \delta(V) \cap T$ be edges that are incident to $v$ in $T$<br/>
&nbsp; push $E'\setminus\{e_1}, E'\setminus\{e_2\}, E'\setminus\{e_3\}$ onto $S$<br/>
**end while**



### Installation instruction for this algorithm. 

(npm libs) lodash, jest, jest-regex-util , python(for python httpserver, ...)

---
### **Sources**

We make use of the 2 of the other repos to suppport our project: 
1. JS graph algorithms: [here](https://github.com/chen0040/js-graph-algorithms)
2. JS LP algorithm: [here](https://github.com/JWally/jsLPSolver)
3. JS Graph And graph Algorithm: [here](https://github.com/dagrejs/graphlib/wiki#browser-scripts)
