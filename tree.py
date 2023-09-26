class AVLNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 0

    def __repr__(self):
        return f"{self.value} ({self.height})"


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            node = AVLNode(value)
            return node

        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)

        self._update_height(node)
        return self._balance(node)

    def _check_value_in_subtree(self, node, value):
        if node is None:
            return False
        elif value == node.value:
            return True
        elif value < node.value:
            return self._check_value_in_subtree(node.left, value)
        else:
            return self._check_value_in_subtree(node.right, value)

    def _update_height(self, node):
        node.height = max(self._get_height(node.left), self._get_height(node.right)) + 1

    def _get_height(self, node):
        return -1 if node is None else node.height

    def _balance(self, node):
        balance = self._get_balance(node)

        if balance > 1:
            balance_left = self._get_balance(node.left)
            # Rotação simples a direita
            if balance_left > 0:
                return self._rotate_right(node)
            # Rotação dupla a direita
            if balance_left < 0:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)

        elif balance < -1:
            right_balance = self._get_balance(node.right)
            # Rotação simples a esquerda
            if right_balance < 0:
                return self._rotate_left(node)
            # Rotação dupla a esquerda
            if right_balance > 0:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)

        return node

    def _get_balance(self, node):
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _rotate_left(self, node):
        # @TODO: apagar mensagem de debug
        print("rot esq", node.value)
        # Define variáveis auxiliares
        pivot = node.right
        aux = pivot.left
        # Realiza a rotação
        pivot.left = node
        node.right = aux
        # Atualiza a altura dos nodos
        self._update_height(pivot)
        self._update_height(node)

        return pivot

    def _rotate_right(self, node):
        # @TODO: apagar mensagem de debug
        print("rot dir", node.value)
        # Define variáveis auxiliares
        pivot = node.left
        aux = pivot.right
        # # Realiza a rotação
        pivot.right = node
        node.left = aux
        # # Atualiza a altura dos nodos
        self._update_height(node)
        self._update_height(pivot)
        return pivot

    def remove(self, value):
        if self.root is None:
            return

        self._remove(self.root, value)

        self._update_height(self.root)
        self._balance(self.root)

        return self.root

    def _remove(self, node, value):
        if value < node.value:
            self._remove(node.left, value)
            return
        elif value > node.value:
            self._remove(node.right, value)
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

        return self._in_order_traversal(node.left) + [node.value] + self._in_order_traversal(node.right)

    def in_order(tree):
        def in_order_node(node):
            if node is not None:
                return in_order_node(node.left) + [node.value] + in_order_node(node.right)
            else:
                return []

        return in_order_node(tree.root)

    def pre_order(tree):
        def pre_order_node(node):
            if node is not None:
                return [node.value] + pre_order_node(node.left) + pre_order_node(node.right)
            else:
                return []

        return pre_order_node(tree.root)

    def post_order(tree):
        def post_order_node(node):
            if node is not None:
                return post_order_node(node.left) + post_order_node(node.right) + [node.value]
            else:
                return []

        return post_order_node(tree.root)
