from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxLevelSum(root):
    max_sum = float("-inf")
    max_level = 1

    level = 1

    q = deque()
    q.append(root)

    while q:
        level_size = len(q)
        level_sum = 0

        for i in range(level_size):
            node = q.popleft()
            level_sum += node.val
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            
        if level_sum > max_sum:
            max_sum = level_sum
            max_level = level
        
        level += 1
    
    return max_level


root = TreeNode(1)
root.left = TreeNode(7)
root.right = TreeNode(0)

root.left.left = TreeNode(7)
root.left.right = TreeNode(-8)
root.right.right = TreeNode(9)

# Call the function
print(maxLevelSum(root))