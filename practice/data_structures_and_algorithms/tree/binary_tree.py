"""
Binary Tree Node Data Structure + Traversal Algorithms:
- BinaryTreeNode Data Structure
- BinaryTree Traversal Algorithms
    - DFS: depth-first search with stacks
        - Preorder: Root -> Left subTree -> Right subTree
        - Inorder: Left subTree -> Root -> Right subTree
        - Postorder: Left subTree -> Right subTree -> Root
    - BFS: breadth-first search with queues (Left -> Right | level-order traversal)
- Complexity Analysis
    - Iterative DFS:
        - Time: O(N): we visit each node once
        - Space: O(N): we could have the entire tree in the stack
    - Recursive DFS:
        - Time: O(N)
        - Space: O(N): but beware of stack overflow
    - BFS:
        - Time:
        - Space:
- When to use BFS vs DFS?
    - BFS
    - DFS
"""
# Definition for a binary tree node.
class BinaryTreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BinaryTreeTraversal(object):

    def doPreorderDFS(self, root):
        """
        DFS Preorder: Root -> Left subTree -> Right subTree
        Order: Top->Bottom, Left-> Right
        :type root: BinaryTreeNode
        :rtype: List[int]

        Approach:
        - Start with a stack (Python list) containing the root node
        - Enter while loop => check that stack is not empty at each iteration
        - For each while-loop iteration: 
            - Pop the current node out of the stack (last inserted item), and add this node to the result (Top->Bottom)
            - Add the current node's child nodes to the stack
            - Here, we push the right child to the stack before the left child, because we're gonna pop off the last item from the stack, meaning left -> right traversal (stack is LIFO)
        - This follows the order (Top->Bottom, Left->Right) for DFS preorder traversal.
        
        Time: O(N), N == number of nodes, since we visit each node once
        Space: O(N) (if we keep entire tree)
        """
        if not root: return []
        stack, output = [root, ], []
        
        while stack:
            root = stack.pop()
            if root:
                output.append(root.val)
                if root.right:
                    stack.append(root.right)
                if root.left:
                    stack.append(root.left)
        
        return output

    def doInorderDFS(self,root):
        """
        DFS Inorder: Left subTree -> Root -> Right subTree
        Order: Left -> Right

        Approach:
        - Start with an empty stack (Python list), and current node equals root
        - Enter while loop => check that stack is not empty OR current node is not null
        - For each while-loop iteration: 
            - Keep adding nodes to the left
            - When we reach the bottom, this means there are no more left subtrees
            - Now, we pop the last element in stack and add it to the output
            - Then, we check the right node of current, if it doesn't exist, we go back up a level (via the stack)
            - Repeat this until the stack is empty and current is null
        - This follows the order (Left->Root->Right) for DFS inorder traversal.
        
        Time: O(N), N == number of nodes, since we visit each node once
        Space: O(N) (we keep entire tree's nodes)
        """
        stack, output = [], []
        current = root
        while current or stack:
            # keep drilling down for left subtrees
            while current:
                stack.append(current)
                current = current.left
            # here, we reached the bottom left-most leaf node => add this leaf node from left subtree to output
            current = stack.pop()
            output.append(current.val)
            # now, check the right subtree for this node (if it exists)
            current = current.right
        return output

    def doPostorderDFS(self,root):
        """
        DFS PostOrder: Left subTree -> Root -> Right subTree
        Order: Bottom->Top, Left->Right
        :type root: BinaryTreeNode
        :rtype: List[int]

        Approach:
        - Start with a stack (Python list) containing the root node
        - Enter while loop => check that stack is not empty at each iteration
        - For each while-loop iteration: 
            - Pop the current node out of the stack (last inserted item), and add this node to the result (Top->Bottom)
            - Add the current node's child nodes to the stack 
        - Since DFS postorder transversal is Bottom->Top and Left->Right the output list should be reversed after the end of loop.

        Notes:
        - Since we need bottom->up via reversing the final result, we add nodes to output from right subtree -> left subtree, then reverse it to have left subtree -> root -> right subtree
        - This is why we append root.left before appending root.right!

        Time: O(N), N == number of nodes, since we visit each node once
        Space: O(N) (if we keep entire tree)
        """
        if not root: return []
        stack, output = [root, ], []
        
        # we're reversing the output for the final answer, so we want to do things in reverse
        # first we add the root node, since this is the last item in postorder traversal (left->right->root)
        # then we add the left nodes, then we add the right nodes, then we pop off the stack
        # adding the right nodes first, then the left nodes
        # Result: (left->right->root) for DFS postorder traversal
        while stack:
            # add root to output
            root = stack.pop()
            output.append(root.val)
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
        
        return output[::-1]


    def doRecursivePreorderDFS(self,root):
        def helper(root, res):
            if root:
                res.append(root.val)
                if root.left:
                    helper(root.left, res)
                if root.right:
                    helper(root.right, res)
        res = []
        helper(root,res)
        return res

    def doRecursiveInorderDFS(self,root):
        def helper(root, res):
            if root:
                if root.left:
                    helper(root.left, res)
                res.append(root.val)
                if root.right:
                    helper(root.right, res)
        res = []
        helper(root,res)
        return res

    def doRecursivePostorderDFS(self,root):
        def helper(root, res):
            if root:
                if root.left:
                    helper(root.left, res)
                if root.right:
                    helper(root.right, res)
                res.append(root.val)
        res = []
        helper(root,res)
        return res


    def doBFS(self,root):
        """
        Approach: BFS with queue/deque (FIFO)
        - In Python using Queue structure would be an overkill since it's designed for a safe exchange between multiple threads and hence requires locking which leads to a performance loose. In Python the queue implementation with a fast atomic append() and popleft() is deque.
        - The zero level contains only one node root. The algorithm is simple:
            - Initiate queue with a root and start from the level number 0 : level = 0.
            - While queue is not empty:
                - Start the current level by adding an empty list into output structure levels.
                - Compute how many elements should be on the current level : it's a queue length.
                - Pop out all these elements from the queue and add them into the current level.
                - Push their child nodes into the queue for the next level.
                - Go to the next level level++.

        :type root: BinaryTreeNode
        :rtype: List[List[int]]

        Time complexity: O(N) since each node is processed exactly once.
        Space complexity: O(N) to keep the output structure which contains N node values.
        """
        from collections import deque
        levels = []
        # return empty list if root is null
        if not root: return levels

        # start with a queue/deque (double-ended queue) with only the root node
        queue = deque([root,])
        level = 0

        # while queue is not empty
        while queue:
            # start the current level (add new list to current level to store this level's nodes)
            levels.append([])

            # check number of elements in current level (this was populated in the previous iteration by getting the child nodes) => initial iteration: we just have the root node in the queue
            level_length = len(queue)

            # pop all elements from queue (FIFO) and add to current level
            for index in range(level_length):
                node = queue.popleft()
                levels[level].append(node.val)

                # add child nodes for all nodes on the current level (these nodes will get added to the next level)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # go to the next level
            level += 1

        return levels

    def doRecursiveBFS(self,root):
        """
        Approach:
        - The simplest way to implement BFS is to use recursion. 
        - Let's first ensure that the tree is not empty, and then call recursively the function helper(node, level), which takes the current node and its level as the arguments.
        - The helper function does the following:
            - The output list here is called levels, and hence the current level is just a length of this list, len(levels). 
            - Compare the number of a current level, len(levels), with a node level, level. 
            - If you're still on the previous level - add the new one by adding a new list into levels.
            - Append the node value to the last list in levels.
            - Process recursively child nodes if they are not None : helper(node.left / node.right, level + 1).
            
        :type root: TreeNode
        :rtype: List[List[int]]

        Time complexity: O(N) since each node is processed exactly once.
        Space complexity: O(N) to keep the output structure which contains N node values.
        """
        levels = []
        
        def helper(node, level):
            # check if we need to add a new level (when len(levels) == level)
            if len(levels) == level:
                levels.append([])

            # add node value to last list in levels
            levels[level].append(node.val)

            # process left and right child nodes
            if node.left:
                helper(node.left, level+1)
            if node.right:
                helper(node.right, level+1)

        # call helper function starting at root and level 0
        helper(root, 0)
        return levels

if __name__ == '__main__':
    print ""
    print """ Tree:
                A
              /   \          
            B       C
          /   \     
        D       E
    """
    root = BinaryTreeNode("A")
    root.left = BinaryTreeNode("B")
    root.right = BinaryTreeNode("C")
    root.left.left = BinaryTreeNode("D")
    root.left.right = BinaryTreeNode("E")

    s = BinaryTreeTraversal()
    print "DFS Preorder (Root -> Left subTree -> Right subTree) (With Stack): ", s.doPreorderDFS(root)
    print "DFS Preorder (Root -> Left subTree -> Right subTree) (Recursively): ", s.doRecursivePreorderDFS(root)

    print "DFS Inorder (Left subTree -> Root -> Right subTree) (With Stack): ", s.doInorderDFS(root)
    print "DFS Inorder (Left subTree -> Root -> Right subTree) (Recursively): ", s.doRecursiveInorderDFS(root)

    print "DFS Postorder (Left subTree -> Right subTree -> Root) (Recursively): ", s.doPostorderDFS(root)    
    print "DFS Postorder (Left subTree -> Right subTree -> Root) (Recursively): ", s.doRecursivePostorderDFS(root)

    print "BFS (Level-Order Traversal) (With Queue/Deque): ", s.doBFS(root)
    print "BFS (Level-Order Traversal) (Recursively): ", s.doRecursiveBFS(root)
