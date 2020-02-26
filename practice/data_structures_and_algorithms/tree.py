
# Definition for a binary tree node.
class BinaryTreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BinaryTreeTraversalAlgorithms(object):

    def preorderTraversal(self, root):
        """
        DFS Preorder: Top -> Bottom, Left -> Right
        :type root: BinaryTreeNode
        :rtype: List[int]

        Time: O(N), N == number of nodes, since we visit each node once
        Space: O(N) (if we keep entire tree)
        """
        
        if root is None:
            return []
        
        stack, output = [root, ], []
        
        # Let's start from the root and then at each iteration pop the current node out of the stack and push its child nodes. 
        # In the implemented strategy we push nodes into output list following the order Top->Bottom and Left->Right.
        # That naturally reproduces preorder traversal.
        while stack:
            root = stack.pop()
            if root is not None:
                output.append(root.val)
                if root.right is not None:
                    stack.append(root.right)
                if root.left is not None:
                    stack.append(root.left)
        
        return output