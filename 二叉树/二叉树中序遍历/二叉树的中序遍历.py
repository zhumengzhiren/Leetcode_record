# 94. 二叉树的中序遍历
# 给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。

# 示例 1：

# 输入：root = [1,null,2,3]
# 输出：[1,3,2]
# 示例 2：

# 输入：root = []
# 输出：[]
# 示例 3：

# 输入：root = [1]
# 输出：[1]

def inorderTraversal(root) :
        l = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            l.append(node.val)
            dfs(node.right)
            return
        dfs(root)
        return l