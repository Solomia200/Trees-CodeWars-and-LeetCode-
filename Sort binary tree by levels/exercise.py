def tree_by_levels(node):
    num = []
    if node is None:
        return []
    queue = [node]
    current = node
    while queue:
        current = queue.pop(0)
        num.append(current.value)
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)
    return num