
# Definition for a binary tree node.
class BinaryTreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BinaryTreeTraversal(object):

    def doPreorderDFS(self, root):
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
            #print 'current root: ', root.val
            if root is not None:
                output.append(root.val)
                #print 'output: ', output
                if root.right is not None:
                    stack.append(root.right)
                if root.left is not None:
                    stack.append(root.left)
                #print 'stack: ', [ s.val for s in stack ]
        
        return output

    def doPostorderDFS(self,root):
        pass

    def doInorderDFS(self,root):
        pass

    def doInorderDFSRecursion(self,root):
        def _helper(root, res):
            if root:
                if root.left:
                    _helper(root.left, res)
                res.append(root.val)
                if root.right:
                    _helper(root.right, res)
        res = []
        _helper(root, res)
        return res

    def doBFS(self,root):
        pass

if __name__ == '__main__':
    node1 = BinaryTreeNode(1)
    node2 = BinaryTreeNode(2)
    node3 = BinaryTreeNode(3)
    node4 = BinaryTreeNode(4)
    node5 = BinaryTreeNode(5)

    node1.left = node2
    node1.right = node5
    node2.left = node3
    node2.right = node4

    s = BinaryTreeTraversal()
    print "DFS Preorder: ", s.doPreorderDFS(node1)
    print "DFS Inorder (Recursion): ", s.doInorderDFSRecursion(node1)