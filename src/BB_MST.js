var jsgraphs = require('./jsgraphs.js');
let mst_func = require('./BB_MST_func.js');
const lod = require('lodash');
const { clone } = require('mathjs');
let numofvertex = 6;

let g = new jsgraphs.WeightedGraph(numofvertex);
// //one level branch example
// g.addEdge(new jsgraphs.Edge(0, 1, 12));
// g.addEdge(new jsgraphs.Edge(0, 2, 10));
// g.addEdge(new jsgraphs.Edge(0, 3, 19));
// g.addEdge(new jsgraphs.Edge(0, 4, 8));
// g.addEdge(new jsgraphs.Edge(1, 2, 3));
// g.addEdge(new jsgraphs.Edge(1, 3, 7));
// g.addEdge(new jsgraphs.Edge(1, 4, 2));
// g.addEdge(new jsgraphs.Edge(2, 3, 6));
// g.addEdge(new jsgraphs.Edge(2, 4, 20));
// g.addEdge(new jsgraphs.Edge(3, 4, 4));

// // 2-level branch with recursion
// g.addEdge(new jsgraphs.Edge(0, 1, 2));
// g.addEdge(new jsgraphs.Edge(0, 2, 4));
// g.addEdge(new jsgraphs.Edge(0, 3, 4));
// g.addEdge(new jsgraphs.Edge(0, 4, 6));
// g.addEdge(new jsgraphs.Edge(1, 2, 5));
// g.addEdge(new jsgraphs.Edge(1, 3, 3));
// g.addEdge(new jsgraphs.Edge(1, 4, 5));
// g.addEdge(new jsgraphs.Edge(2, 3, 2));
// g.addEdge(new jsgraphs.Edge(2, 4, 6));
// g.addEdge(new jsgraphs.Edge(3, 4, 5));

// 6 vertex example 
g.addEdge(new jsgraphs.Edge(0, 1, 25));
g.addEdge(new jsgraphs.Edge(0, 2, 19));
g.addEdge(new jsgraphs.Edge(0, 3, 19));
g.addEdge(new jsgraphs.Edge(0, 4, 16));
g.addEdge(new jsgraphs.Edge(0, 5, 28));
g.addEdge(new jsgraphs.Edge(1, 2, 24));
g.addEdge(new jsgraphs.Edge(1, 3, 30));
g.addEdge(new jsgraphs.Edge(1, 4, 27));
g.addEdge(new jsgraphs.Edge(1, 5, 17));
g.addEdge(new jsgraphs.Edge(2, 3, 18));
g.addEdge(new jsgraphs.Edge(2, 4, 20));
g.addEdge(new jsgraphs.Edge(2, 5, 23));
g.addEdge(new jsgraphs.Edge(3, 4, 19));
g.addEdge(new jsgraphs.Edge(3, 5, 32));
g.addEdge(new jsgraphs.Edge(4, 5, 41));


mst_func.branchandBound(g)


// //check MST edge connect the every vertex together.
// mst_func.oneTreeMST(mst_result);
// // check tour, and the tour cost 
// if(mst_func.istour(mst_result)){ // if the MST path is a tour, we calculate the cost.
//     let tourfinalcost = mst_func.calculatetourcost(g, mst_result, mst_cost);
//     console.log("The cost of this tour is "+ tourfinalcost);
//     mst_func.getTour(mst)
// }

// //branch
// let branchVertex;// the vertex we will branch on 
// let adjacentVertex;// list of 3 adjacent vertexs connected to vertex
// [branchVertex, adjacentVertex] = mst_func.findBranchVertex(mst_result)
// console.log("branch edge ("+ branchVertex + ") - " + adjacentVertex)


// g = new jsgraphs.Graph(10);
// g.addEdge(0,1);
// g.addEdge(1,4);
// g.addEdge(2,4);
// g.addEdge(2,3);
// g.addEdge(0,3);
// istour(g)
// oneTreeMST(g);

// build the function that can return the  vertext with highest degree.