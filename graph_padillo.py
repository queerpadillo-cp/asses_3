from collections import deque


def build_padillo_graph() -> dict[str, list[str]]:
    """
    Constructs the 7-vertex Graph for 'PADILLO' (matching Page 9 network layout).
    L1 and L2 distinguish the two 'L' nodes in the network.
    """
    return {
        "P": ["A", "L1", "D"],
        "A": ["P", "I", "L2"],
        "L1": ["P", "L2", "O"],
        "D": ["P", "O"],
        "I": ["A"],
        "L2": ["A", "L1"],
        "O": ["L1", "D"],
    }


def bfs_graph(graph: dict[str, list[str]], start: str) -> list[str]:
    """Performs Breadth-First Search on a Graph using a Queue and Visited set."""
    visited = {start}
    queue = deque([start])
    traversal_order = []

    while queue:
        current = queue.popleft()
        traversal_order.append(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal_order


def dfs_graph(graph: dict[str, list[str]], start: str) -> list[str]:
    """Performs Depth-First Search on a Graph using a Stack and Visited set."""
    visited = set()
    stack = [start]
    traversal_order = []

    while stack:
        current = stack.pop()

        if current not in visited:
            visited.add(current)
            traversal_order.append(current)

            # Push neighbors in reverse order so leftmost neighbor is explored first
            for neighbor in reversed(graph[current]):
                if neighbor not in visited:
                    stack.append(neighbor)

    return traversal_order


if __name__ == "__main__":
    padillo_graph = build_padillo_graph()

    bfs_result = bfs_graph(padillo_graph, "P")
    dfs_result = dfs_graph(padillo_graph, "P")

    print("=== GRAPH TRAVERSAL (PADILLO) ===")
    print("BFS Traversal:", " - ".join(bfs_result))
    print("DFS Traversal:", " - ".join(dfs_result))