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

    def __repr__(self):
        if self.root is None:
            return "[]"

        return f"[{self._in_order_traversal()}]"

    def _in_order_traversal(self):
        if self.root is None:
            return []

        return self._in_order_traversal(self.root.left) + [self.root.data] + self._in_order_traversal(self.root.right)
