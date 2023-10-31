from person import Person


class AVLNode:
    """
    Classe que representa um nodo em uma árvore AVL.
    """
    def __init__(self, key: int, value: Person):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0

    def __repr__(self):
        return f"{self.key} ({self.height})"


class AVLTree:
    """
    Classe responsável por armazenar dados em uma estrutura de árvore AVL e
    realizar operações de inserção e remoção de elementos.
    """
    def __init__(self):
        self.root = None

    def __repr__(self):
        if self.root is None:
            return "[]"
        return f"[{self.in_order()}]"

    def insert(self, key: int, value: Person) -> None:
        """
        Insere um valor na árvore.
        :param key: Chave do valor a ser inserido.
        """
        if self.search_node(key) is not None:
            return
        self.root = self._insert(self.root, key, value)

    def _insert(self, node: AVLNode, key: int, value: Person, parent: AVLNode = None) -> AVLNode:
        """
        Insere um valor na árvore.
        :param node: Nodo pai.
        :param key: Valor a ser inserido.
        :return: Nodo pai do nodo inserido.
        """
        if node is None:
            node = AVLNode(key, value)
            if parent is not None:
                node.parent = parent
            return node

        if key < node.key:
            node.left = self._insert(node.left, key, value, node)
        elif key > node.key:
            node.right = self._insert(node.right, key, value, node)

        self._update_height(node)
        return self._balance(node)

    def search(self, key: int) -> list | None:
        """
        Procura por um nodo com determinado valor.
        :param key: Chave do valor desejado.
        :return: Caminho até o nodo procurado.
        """
        if self.root is None or key is None:
            return
        return self._search(self.root, key, [])

    def _search(self, node: AVLNode, key: int, path: list) -> list | None:
        """
        Procura por um nodo com determinado valor.
        :param node: Nodo a ser comparado.
        :param key: Chave do valor desejado.
        :param path: Caminho percorrido na árvore.
        :return: Caminho até o nodo procurado.
        """
        if node is None:
            return None

        path.append(node)
        if key < node.key:
            return self._search(node.left, key, path)
        if key > node.key:
            return self._search(node.right, key, path)
        return path

    def search_node(self, key: int) -> AVLNode | None:
        """
        Procura por determinado nodo.
        :param key: Chave do nodo.
        :return: Nodo encontrado.
        """
        path = self.search(key)
        return path[-1] if path is not None else None

    def _update_height(self, node: AVLNode) -> None:
        """
        Atualiza o atributo de altura de um nodo.
        :param node: Nodo a ser atualizado.
        """
        if node:
            new_height = max(self._get_height(node.left), self._get_height(node.right)) + 1
            if node.height != new_height:
                node.height = new_height
                if node.parent is not None:
                    self._update_height(node.parent)

    def _get_height(self, node: AVLNode) -> int:
        """
        Indica a altura de um nodo. Se este for nulo, retorna -1.
        :param node: Nodo cuja altura será indicada.
        :return: Altura do nodo.
        """
        return -1 if node is None else node.height

    def _balance(self, node: AVLNode) -> AVLNode:
        """
        Identifica se a árvore indicada está balanceada e, se necessário, realiza as operações para rebalancear.
        :param node: Sub-árvore a ser balanceada.
        :return: Sub-árvore balanceada.
        """
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

    def _get_balance(self, node: AVLNode) -> int:
        """
        Calcula o fator de balanceamento do nodo indicado.
        FB = H[árvore esquerda] - H[árvore direita]
        :param node: Nodo cujo fator de balanceamento será calculado.
        :return: Fator de balanceamento do nodo.
        """
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _rotate_left(self, old_root: AVLNode) -> AVLNode:
        """
        Realiza rotação simples a esquerda.
        :param old_root: Nodo a ser rotacionado.
        :return: Sub-árvore rotacionada a esquerda.
        """
        parent_node = old_root.parent

        new_root = old_root.right
        old_root.right = new_root.left

        if (old_root.right):
            old_root.right.parent = old_root
        new_root.left = old_root
        old_root.parent = new_root

        if parent_node is None:
            self.root = new_root
            self.root.parent = None
        else:
            if parent_node.right and parent_node.right.key == old_root.key:
                parent_node.right = new_root
                new_root.parent = parent_node
            elif parent_node.left and parent_node.left.key == old_root.key:
                parent_node.left = new_root
                new_root.parent = parent_node
        
        self._update_height(new_root.left)
        self._update_height(parent_node)
        return new_root

    def _rotate_right(self, old_root: AVLNode) -> AVLNode:
        """
        Realiza rotação simples a direita.
        :param node: Nodo a ser rotacionado.
        :return: Sub-árvore rotacionada a direita.
        """
        parent_node = old_root.parent

        new_root = old_root.left
        old_root.left = new_root.right

        if (old_root.left):
            old_root.left.parent = old_root

        new_root.right = old_root
        old_root.parent = new_root

        if parent_node is None:
            self.root = new_root
            self.root.parent = None
        else:
            if parent_node.right and parent_node.right.key == old_root.key:
                parent_node.right = new_root
                new_root.parent = parent_node
            elif parent_node.left and parent_node.left.key == old_root.key:
                parent_node.left = new_root
                new_root.parent = parent_node

        self._update_height(new_root.right)
        self._update_height(parent_node)
        return new_root

    def remove(self, key: int) -> AVLNode | None:
        """
        Remove nodo com determinado valor da árvore AVL.
        :param key: Chave do nodo a ser removido.
        :return: Árvore com nodo removido.
        """
        if self.root is None or self.search(key) is None:
            return

        parent_node = self._remove(self.root, key)
        self._update_height(parent_node)
        return self._balance_all(self.root)

    def _balance_all(self, node: AVLNode):
        """
        Balanceia todos os nós da árvore indicada.
        :param node: Node a ser balanceado.
        :return: Node balanceado.
        """
        if node is None:
            return None

        node.left = self._balance_all(node.left)
        node.right = self._balance_all(node.right)

        node = self._balance(node)
        return node
    
    def _remove(self, node: AVLNode, key: int, parent: AVLNode = None) -> AVLNode | None:
        """
        Remove nodo com determinado valor da árvore AVL.
        :param node: Nodo a ser comparado.
        :param key: Chave do nodo a ser removido.
        :param parent: Pai do nodo a ser comparado. Default=None.
        :return: Árvore com nodo removido.
        """
        if not node:
            return
        elif key < node.key:
            return self._remove(node.left, key, node)
        elif key > node.key:
            return self._remove(node.right, key, node)

        # É folha
        if node.left is None and node.right is None:
            return self._remove_leaf(node, parent)
        # Nodo tem somente 1 filho a esquerda
        if node.right is None:
            return self._remove_node_has_left_child(node, parent)
        # Nodo tem somente 1 filho a direita
        if node.left is None:
            return self._remove_node_has_right_child(node, parent)
        # Nodo tem 2 filhos (exclusão por cópia)
        return self._remove_node_with_both_child(node, parent)

    def _remove_leaf(self, node: AVLNode, parent: AVLNode) -> AVLNode:
        """
        Remove folha (nodo sem filhos).
        :param node: Nodo a ser removido.
        :param parent: Pai do nodo a ser removido.
        :return: Pai do nodo a ser removido.
        """
        if parent.right == node:
            parent.right = None
        else:
            parent.left = None
        return parent

    def _remove_node_has_left_child(self, node: AVLNode, parent: AVLNode) -> AVLNode:
        """
        Remove nodo com filho a esquerda.
        :param node: Nodo a ser removido.
        :param parent: Pai do nodo a ser removido.
        :return: Pai do nodo a ser removido.
        """
        if parent.right == node:
            parent.right = node.left
        else:
            parent.left = node.left
        return parent

    def _remove_node_has_right_child(self, node: AVLNode, parent: AVLNode) -> AVLNode:
        """
        Remove nodo com filho a direita.
        :param node: Nodo a ser removido.
        :param parent: Pai do nodo a ser removido.
        :return: Pai do nodo a ser removido.
        """
        if parent.right == node:
            parent.right = node.right
        else:
            parent.left = node.right
        return parent

    def _remove_node_with_both_child(self, node: AVLNode, parent: AVLNode) -> AVLNode:
        """
        Remove nodo com dois filhos.
        :param node: Nodo a ser removido.
        :param parent: Pai do nodo a ser removido.
        :return: Sub-árvore do nodo removido.
        """
        successor = self._find_successor(node)
        # Nodo é raíz da árvore
        if parent is None:
            self.root.key = successor.key
        else:
            aux = parent.right if parent.right == node else parent.left
            aux.key = successor.key
        return self._remove(successor, successor.key, successor.parent)

    def _find_successor(self, node: AVLNode) -> AVLNode:
        """
        Procura o sucessor do nodo a ser excluído por cópia.
        :param node: Nodo a ser removido.
        :return: Sucessor do nodo.
        """
        if node.left.right is not None:
            return node.left.right
        return node.left

    def in_order(self) -> list:
        """
        Acessa nodos da árvore utilizando o caminhamento em ordem.
        :return: Valores dos nodos.
        """
        def in_order_node(node):
            if node is not None:
                return in_order_node(node.left) + [node.key] + in_order_node(node.right)
            return []

        return in_order_node(self.root)

    def pre_order(self) -> list:
        """
        Acessa nodos da árvore utilizando o caminhamento em pré-ordem.
        :return: Valores dos nodos.
        """
        def pre_order_node(node):
            if node is not None:
                return [node.key] + pre_order_node(node.left) + pre_order_node(node.right)
            return []

        return pre_order_node(self.root)

    def post_order(self) -> list:
        """
        Acessa nodos da árvore utilizando o caminhamento em pós-ordem.
        :return: Valores dos nodos.
        """
        def post_order_node(node):
            if node is not None:
                return post_order_node(node.left) + post_order_node(node.right) + [node.key]
            return []

        return post_order_node(self.root)
