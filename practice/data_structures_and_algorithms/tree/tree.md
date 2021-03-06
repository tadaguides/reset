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
* In general:
  * use BFS - when you want to find the shortest path from a certain source node to a certain destination. (Or more generally, the smallest number of steps to reach the end state from a given initial state.)
  * use DFS - when you want to exhaust all possibilities, and check which one is the best/count the number of all possible ways.
  * use either BFS or DFS - when you just want to check connectedness between two nodes on a given graph. (Or more generally, whether you could reach a given state to another.)
* BFS vs. DFS heavily depends on the structure of the search tree and the number and location of solutions (aka searched-for items).
  * If you know a solution is not far from the root of the tree, a breadth first search (BFS) might be better.
  * If the tree is very deep and solutions are rare, depth first search (DFS) might take an extremely long time, but BFS could be faster.
  * If the tree is very wide, a BFS might need too much memory, so it might be completely impractical.
  * If solutions are frequent but located deep in the tree, BFS could be impractical.
  * If the search tree is very deep you will need to restrict the search depth for depth first search (DFS), anyway (for example with iterative deepening).
* Comparing BFS and DFS, the big advantage of DFS is that it has much lower memory requirements than BFS, because it’s not necessary to store all of the child pointers at each level. Depending on the data and what you are looking for, either DFS or BFS could be advantageous.
* For example, given a family tree if one were looking for someone on the tree who’s still alive, then it would be safe to assume that person would be on the bottom of the tree. This means that a BFS would take a very long time to reach that last level. A DFS, however, would find the goal faster. But, if one were looking for a family member who died a very long time ago, then that person would be closer to the top of the tree. Then, a BFS would usually be faster than a DFS. So, the advantages of either vary depending on the data and what you’re looking for.
* One more example is Facebook; Suggestion on Friends of Friends. We need immediate friends for suggestion where we can use BFS. May be finding the shortest path or detecting the cycle (using recursion) we can use DFS.

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

### BFS vs DFS Reference
* https://www.programmerinterview.com/data-structures/dfs-vs-bfs/
* https://stackoverflow.com/questions/3332947/when-is-it-practical-to-use-depth-first-search-dfs-vs-breadth-first-search-bf
* https://www.quora.com/What-are-the-advantages-of-using-BFS-over-DFS-or-using-DFS-over-BFS-What-are-the-applications-and-downsides-of-each

---

## Solve Tree Problems Recursively
* When you meet a tree problem, ask yourself two questions: 
  1. Can you determine some parameters to help the node know its answer? 
  2. Can you use these parameters and the value of the node itself to determine what should be the parameters passed to its children? 
  * If the answers are both yes, try to solve this problem using a "top-down" recursive solution.
* Or, you can think of the problem in this way: for a node in a tree, if you know the answer of its children, can you calculate the answer of that node? 
  * If the answer is yes, solving the problem recursively using a "bottom-up" approach might be a good idea.

### "Top-Down" Solution
* "Top-down" means that in each recursive call, we will visit the node first to come up with some values, and pass these values to its children when calling the function recursively. 
* So the "top-down" solution can be considered as a kind of preorder traversal (Root -> Left -> Right). 
* The recursive function top_down(root, params) works like this:
  1. return specific value for null node
  2. update the answer if needed                      // answer <-- params
  3. left_ans = top_down(root.left, left_params)      // left_params <-- root.val, params
  4. right_ans = top_down(root.right, right_params)   // right_params <-- root.val, params 
  5. return the answer if needed                      // answer <-- left_ans, right_ans

### Example "Top-Down" Problem: Find max depth of a binary tree
* We know that the depth of the root node is 1. 
* For each node, if we know its depth, we will know the depth of its children. 
* Therefore, if we pass the depth of the node as a parameter when calling the function recursively, all the nodes will know their depth. 
* And for leaf nodes, we can use the depth to update the final answer. 
* Here is the pseudocode for the recursive function maximum_depth(root, depth):
  1. return if root is null
  2. if root is a leaf node:
  3.      answer = max(answer, depth)         // update the answer if needed
  4. maximum_depth(root.left, depth + 1)      // call the function recursively for left child
  5. maximum_depth(root.right, depth + 1)     // call the function recursively for right child

### "Bottom-Up" Solution
* "Bottom-up" is another recursive solution. In each recursive call, we will firstly call the function recursively for all the children nodes and then come up with the answer according to the returned values and the value of the current node itself. 
* This process can be regarded as a kind of postorder traversal (Left -> Right -> Root). 
* Typically, a "bottom-up" recursive function bottom_up(root) will be something like this:
  1. return specific value for null node
  2. left_ans = bottom_up(root.left)          // call function recursively for left child
  3. right_ans = bottom_up(root.right)        // call function recursively for right child
  4. return answers                           // answer <-- left_ans, right_ans, root.val

### Example "Bottom-Up" Problem: For a single tree node, what is the max depth of the subtree at that root node?
* If we know the maximum depth l of the subtree rooted at its left child and the maximum depth r of the subtree rooted at its right child, can we answer the previous question? 
* Of course yes, we can choose the maximum between them and add 1 to get the maximum depth of the subtree rooted at the current node. That is x = max(l, r) + 1.
* It means that for each node, we can get the answer after solving the problem for its children. 
* Therefore, we can solve this problem using a "bottom-up" solution. 
* Here is the pseudocode for the recursive function maximum_depth(root):
  1. return 0 if root is null                 // return 0 for null node
  2. left_depth = maximum_depth(root.left)
  3. right_depth = maximum_depth(root.right)
  4. return max(left_depth, right_depth) + 1  // return depth of the subtree rooted at root

---