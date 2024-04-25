'''
104. 二叉树的最大深度

给定一个二叉树 root ，返回其最大深度。

二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。

100. 相同的树

给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

101. 对称二叉树

给你一个二叉树的根节点 root ， 检查它是否轴对称。

110. 平衡二叉树

给定一个二叉树，判断它是否是平衡二叉树
  
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 104
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
    # 100
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None or q is None:
            return p == q
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) and p.val == q.val

# 101
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        p = root.left
        q = root.right
        return self.isSame(p, q)

    def isSame(self, p, q):
        if p is None or q is None:
            return p is q
        return p.val == q.val and self.isSame(p.left, q.right) and self.isSame(p.right
        , q.left)

# 110
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_height(node):
            if node is None:
                return 0
            return max(get_height(node.left), get_height(node.right)) + 1
        if root is None:
            return True
        l_depth = get_height(root.left)
        r_depth = get_height(root.right)
        return abs(l_depth-r_depth) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)