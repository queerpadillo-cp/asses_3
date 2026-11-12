from collections import deque


class TreeNode:
    def __init__(self, value: str):
        self.value = value
        self.left = None
        self.right = None


def build_padillo_tree() -> TreeNode:
    """
    Constructs the 7-node Binary Tree for 'PADILLO':
            P          (Level 0)
          /   \
         A     D       (Level 1)
        / \   / \
       I   L L   O     (Level 2)
    """
    root = TreeNode("P")
    root.left = TreeNode("A")
    root.right = TreeNode("D")

    root.left.left = TreeNode("I")
    root.left.right = TreeNode("L")

    root.right.left = TreeNode("L")
    root.right.right = TreeNode("O")

    return root


def bfs_binary_tree(root: TreeNode) -> list[str]:
    """Performs Breadth-First Search (Level-Order) using a Queue."""
    if not root:
        return []

    visited = []
    queue = deque([root])

    while queue:
        current = queue.popleft()
        visited.append(current.value)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return visited


def dfs_binary_tree(root: TreeNode) -> list[str]:
    """Performs Depth-First Search (Pre-Order) using a Stack."""
    if not root:
        return []

    visited = []
    stack = [root]

    while stack:
        current = stack.pop()
        visited.append(current.value)

        # Push right child first so left child is popped and visited first
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

    return visited


if __name__ == "__main__":
    tree_root = build_padillo_tree()

    bfs_result = bfs_binary_tree(tree_root)
    dfs_result = dfs_binary_tree(tree_root)

    print("=== BINARY TREE TRAVERSAL (PADILLO) ===")
    print("BFS Traversal:", " - ".join(bfs_result))
    print("DFS Traversal:", " - ".join(dfs_result))