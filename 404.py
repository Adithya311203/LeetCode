def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([(root, False)])  # (node, is_left)
        total_sum = 0
        
        while queue:
            node, is_left = queue.popleft()
            
            if is_left and not node.left and not node.right:
                total_sum += node.val
            
            if node.left:
                queue.append((node.left, True))
            if node.right:
                queue.append((node.right, False))
        
        return total_sum