# Trees

---

## [Binary Tree] Summary
* A tree is a data structure to simulate a hierarchical tree structure.
* Each node of the tree will have a root value and a list of references to other nodes which are called child nodes. 
* From graph view, a tree can also be defined as a directed acyclic graph which has N nodes and N-1 edges.
* A Binary Tree is a tree data structure in which each node has at most two children, which are referred to as the left child and the right child.

## [Binary Tree] Key Concepts
* Understand the concept of a tree and a binary tree
* Be familiar with different traversal methods: understanding these traversal methods will provide a solid foundation for the further study.
  * Understand the difference between different tree traversal methods
  * Be able to solve preorder, inorder and postorder traversal recursively
  * Be able to solve preorder, inorder and postorder traversal iteratively
  * Be able to do level traversal using BFS
* Use recursion to solve binary-tree-related problems

## BFS vs. DFS
### Advantages of  BFS:-
1. Solution will definitely found out by BFS If there are some solution.
2. BFS will never get trapped in blind alley , means unwanted nodes.
3. If there are more than one solution then it will find solution with minimal steps.
### Disadvantages Of BFS :-
1. Memory Constraints As it stores all the nodes of present level to go for next level.
2. If solution is far away then it consumes time.
### Application Of BFS :-
1. Finding Shortest Path.
2. Checking graph with bipertiteness.
3. Copying cheiney's Algorithm.
### Advantages Of DFS :-
1. Memory requirement is Linear WRT Nodes.
2. Less time and space complexity rather than BFS.
3. Solution can be found out by without much more search.
### Disadvantage of DFS :-
1. Not Guaranteed that it will give you solution.
2. Cut-off depth is smaller so time complexity is more.
3. Determination of depth until the search has proceeds.
### Applications of DFS:-
1. Finding Connected components.
2. Topological sorting.
3. Finding Bridges of graph.

---