class AVLNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.height = 0

    def __repr__(self):
        return f"{self.data} ({self.height})"


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = AVLNode(data)
            return

        self._insert(self.root, data)

    def _insert(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = AVLNode(data)
                self._update_height(node)
                self._balance(node)
                return
            else:
                self._insert(node.left, data)
                return
        else:
            if node.right is None:
                node.right = AVLNode(data)
                self._update_height(node)
                self._balance(node)
                return
            else:
                self._insert(node.right, data)
                return

    def _update_height(self, node):
        node.height = max(self._get_height(node.left), self._get_height(node.right)) + 1

    def _get_height(self, node):
        if node is None:
            return -1
        else:
            return node.height

    def _balance(self, node):
        balance = self._get_balance(node)

        if balance > 1:
            if self._get_balance(node.left) < 0:
                self._rotate_left_right(node)
            else:
                self._rotate_left(node)
        elif balance < -1:
            if self._get_balance(node.right) > 0:
                self._rotate_right_left(node)
            else:
                self._rotate_right(node)

    def _get_balance(self, node):
        if node is None:
            return 0
        else:
            return self._get_height(node.left) - self._get_height(node.right)

    def _rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node

        self._update_height(node)
        self._update_height(new_root)

        return new_root

    def _rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node

        self._update_height(node)
        self._update_height(new_root)

        return new_root

    def _rotate_left_right(self, node):
        node.left = self._rotate_left(node.left)
        return self._rotate_right(node)

    def _rotate_right_left(self, node):
        node.right = self._rotate_right(node.right)
        return self._rotate_left(node)

    def remove(self, data):
        if self.root is None:
            return

        self._remove(self.root, data)

        self._update_height(self.root)
        self._balance(self.root)

        return self.root

    def _remove(self, node, data):
        if data < node.data:
            self._remove(node.left, data)
            return
        elif data > node.data:
            self._remove(node.right, data)
            return

        if node.left is None:
            new_root = node.right
        elif node.right is None:
            new_root = node.left
        else:
            successor = self._find_successor(node)
            new_root = successor.right
            successor.right = None
            successor.left = node.left
            node.left = None

        self._update_height(new_root)
        self._balance(new_root)

        return new_root

    def _find_successor(self, node):
        if node.right is None:
            return node

        successor = node.right
        while successor.left is not None:
            successor = successor.left

        return successor

    def __repr__(self):
        if self.root is None:
            return "[]"

        return f"[{self._in_order_traversal(self.root)}]"

    def _in_order_traversal(self, node):
        if node is None:
            return []

        return self._in_order_traversal(node.left) + [node.data] + self._in_order_traversal(node.right)
