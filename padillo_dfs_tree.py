# Name: Queer S. Padillo
# Section: BSIT-2A
# Assessment 3.6: DFS Methods in Tree (Dynamic Program)

from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def build_tree_from_string(self, text):
        if not text:
            return
        self.root = Node(text[0])
        queue = deque([self.root])
        i = 1
        while queue and i < len(text):
            current = queue.popleft()

            # Assign Left Child
            if i < len(text):
                current.left = Node(text[i])
                queue.append(current.left)
                i += 1

            # Assign Right Child
            if i < len(text):
                current.right = Node(text[i])
                queue.append(current.right)
                i += 1

    # 1. Preorder: Root -> Left -> Right
    def preorder(self, node, result):
        if node:
            result.append(node.data)
            self.preorder(node.left, result)
            self.preorder(node.right, result)

    # 2. Inorder: Left -> Root -> Right
    def inorder(self, node, result):
        if node:
            self.inorder(node.left, result)
            result.append(node.data)
            self.inorder(node.right, result)

    # 3. Postorder: Left -> Right -> Root
    def postorder(self, node, result):
        if node:
            self.postorder(node.left, result)
            self.postorder(node.right, result)
            result.append(node.data)


def run_dfs_program():
    print("==================================================")
    print("         DFS METHODS IN BINARY TREE               ")
    print("==================================================\n")

    first_name = input("Enter First Name (Press Enter for 'QUEER'): ").strip()
    last_name = input("Enter Last Name (Press Enter for 'PADILLO'): ").strip()

    if not first_name:
        first_name = "QUEER"
    if not last_name:
        last_name = "PADILLO"

    combined = "".join((first_name + last_name).split()).upper()
    print(f"\nBuilding Binary Tree for: {combined} (Total Nodes: {len(combined)})\n")

    tree = BinaryTree()
    tree.build_tree_from_string(combined)

    pre_res, in_res, post_res = [], [], []
    tree.preorder(tree.root, pre_res)
    tree.inorder(tree.root, in_res)
    tree.postorder(tree.root, post_res)

    print("Preorder  (Root -> Left -> Right):")
    print("  " + " -> ".join(pre_res) + "\n")

    print("Inorder   (Left -> Root -> Right):")
    print("  " + " -> ".join(in_res) + "\n")

    print("Postorder (Left -> Right -> Root):")
    print("  " + " -> ".join(post_res) + "\n")


if __name__ == "__main__":
    run_dfs_program()