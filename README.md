### **Intro**

This repo is for the final project of COSP 520 2022 Winter Term 1. We are doing something about the Traveling Salesman Problem. 



---
### **The Dynamic Programming Algorithm for TSP**

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
### **The Branch and Bound Algorithm with Minimum Spanning Tree for TSP**



---
### **Sources**

We make use of the 2 of the other repos to suppport our project: 
1. JS graph algorithms: [here](https://github.com/chen0040/js-graph-algorithms)
2. JS LP algorithm: [here](https://github.com/JWally/jsLPSolver)
3. JS Graph And graph Algorithm: [here](https://github.com/dagrejs/graphlib/wiki#browser-scripts)
