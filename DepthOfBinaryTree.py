__author__ = 'qfeng'

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# breadth-first solution
class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        current_depth = 0
        current_node_list = [root]
        child_node_list = []
        while current_node_list != []:
            current_node_list = filter(None, current_node_list)
            if current_node_list == []:
                continue
            # we have something in the current node list!
            current_depth += 1
            # check if any of the current nodes 
            # has children nodes
            for current_node in current_node_list:
                if current_node == None:
                    continue
                # for loop to get all children from all current nodes
                if current_node.left == None and current_node.right == None:
                    continue
                else:
                    if current_node.left != None:
                        child_node_list.append(current_node.left)
                    if current_node.right != None:
                        child_node_list.append(current_node.right)

            # if none of the current nodes has children, while loop breaks
            # otherwise the else loop above was executed, and current depth incremented
            current_node_list = child_node_list
            # re initialize child node list
            child_node_list = []
            
        return current_depth

tree = TreeNode(1)
leaf1l = TreeNode(2.1)
leaf1r = TreeNode(2.2)
leaf2l = TreeNode(3.1)

leaf1l.left = leaf2l
tree.left = leaf1l
tree.right = leaf1r

tree4 = TreeNode(1)
tree4.left=tree

tree_none = None
sol = Solution()
print sol.maxDepth(tree4)
print sol.maxDepth(tree)
print sol.maxDepth(leaf1r)
print sol.maxDepth(tree_none)