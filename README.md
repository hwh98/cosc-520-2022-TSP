### **Introduction**

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
 * $C^\*$ the best tour ever found.

Our goal is to find a tour that visits all vertices once, the algorithm is described in algo-
rithm 2. While the pseudo code stated below is formulated as an iterative scheme, in our
implementation it’s implemented with recursion to simplify variables in the scope.

##
Algorithm 2 MST Branch and Bound for TSP


&nbsp; $C^\* := undefined$<br/>
&nbsp; $S:={E}$<br/>
&nbsp; **while** $S \neq \emptyset$ **then**<br/>
&nbsp; &nbsp; Take top $E' \in S$<br/>
&nbsp; &nbsp; **if** $G(V,E')$ is disconnected **then**<br/>
&nbsp; &nbsp; &nbsp; **continue** {Prune by infeasibility}<br/>
&nbsp; &nbsp; **end if**<br/>
&nbsp; &nbsp; Compute $M:=MST(E')**<br/>
&nbsp; &nbsp; **if** $M$ is a spanning path **then**<br/>
&nbsp; &nbsp; &nbsp; Let $T$ be the tour by joining the end points of the path $M$<br/>
&nbsp; &nbsp; &nbsp; **if** $C(T) < C(C^\*)$ **then**<br/>
&nbsp; &nbsp; &nbsp; &nbsp;  $C^\*:=T${New, bettwer tour found}<br/>
&nbsp; &nbsp; &nbsp; **end if**<br/>
&nbsp; &nbsp; **end if**<br/>
&nbsp; &nbsp; **if** $M$ is a path and $c(T) \ge c(C^\*)$ **then**<br/>
&nbsp; &nbsp; &nbsp; **continute** {Pruned by sub-optimality}<br/>
&nbsp; &nbsp; **end if**<br/>
&nbsp; &nbsp; Let $v \subset V$ be a vertex incident to at least 3 edges in $T$<br/>
&nbsp; &nbsp; Let $e_1, e_2, e_3 \subseteq \delta(V) \cap T$ be edges that are incident to $v$ in $T$<br/>
&nbsp; &nbsp; push $E'\setminus\{e_1}, E'\setminus\{e_2\}, E'\setminus\{e_3\}$ onto $S$<br/>
&nbsp; **end while**<br/>

##

### Installation instruction for this algorithm. 

Under the project directory, follow the instructions below to setup the environment for Branch and Bound visualization 

Install node.js, which includes NPM package manager for the javascript, from [here](https://nodejs.org/en/download/)

For windows operating system, download the file and follow the instruction [here](https://phoenixnap.com/kb/install-node-js-npm-on-windows)

For Mac user, you can either download the file and follow the [instruction](https://radixweb.com/blog/installing-npm-and-nodejs-on-windows-and-mac), or you can install it with homebrew.
> brew install node

After install the node.js, you can check if the NPM is also installed successfully by
> npm version

Install the package for graph processing.
> npm install js-graph-algorithms

Install the package for deep cloning the graph.
> npm install lodash

Once you go through the installation instructions, you can open the jsgraph_BB_TSP_Visualization.html with Safari or Chrome web browser.

---
### **Reference and Sources**


1. [A dynamic programming approach to sequencing problems](https://epubs.siam.org/doi/abs/10.1137/0110015?journalCode=smjmap.1)

2. Jon Kleinberg and Éva Tardos. Algorithm design. MTM, 2022

Referenced library and package:

3. [JS graph algorithms](https://github.com/chen0040/js-graph-algorithms)

4. [JS LP algorithm](https://github.com/JWally/jsLPSolver)

5. [JS Graph And graph Algorithm](https://github.com/dagrejs/graphlib/wiki#browser-scripts)

6. [Lodash modular utilities.](https://www.jsdelivr.com/package/npm/lodash)

