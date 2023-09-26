class AVLNode:
    """
    Classe que representa um nodo em uma árvore AVL.
    """
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None
        self.height = 0

    def __repr__(self):
        return f"{self.value} ({self.height})"


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

    def insert(self, value: int) -> None:
        """
        Insere um valor na árvore.
        :param value: Valor a ser inserido.
        """
        self.root = self._insert(self.root, value)

    def _insert(self, node: AVLNode, value: int) -> AVLNode:
        """
        Insere um valor na árvore.
        :param node: Nodo pai.
        :param value: Valor a ser inserido.
        :return: Nodo inserido.
        """
        if node is None:
            node = AVLNode(value)
            return node

        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)

        self._update_height(node)
        return self._balance(node)

    def _check_value_in_subtree(self, node: AVLNode, value: int) -> bool:
        """
        Indica se valor já foi inserido em determinada sub-árvore.
        :param node: Sub-árvore.
        :param value: Valor a ser testado.
        :return: Se valor existe na árvore.
        """
        if node is None:
            return False
        elif value == node.value:
            return True
        elif value < node.value:
            return self._check_value_in_subtree(node.left, value)
        else:
            return self._check_value_in_subtree(node.right, value)

    def _update_height(self, node: AVLNode) -> None:
        """
        Atualiza o atributo de altura de um nodo.
        :param node: Nodo a ser atualizado.
        """
        node.height = max(self._get_height(node.left), self._get_height(node.right)) + 1

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

    def _rotate_left(self, node: AVLNode) -> AVLNode:
        """
        Realiza rotação simples a esquerda.
        :param node: Nodo a ser rotacionado.
        :return: Sub-árvore rotacionada a esquerda.
        """
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

    def _rotate_right(self, node: AVLNode) -> AVLNode:
        """
        Realiza rotação simples a direita.
        :param node: Nodo a ser rotacionado.
        :return: Sub-árvore rotacionada a direita.
        """
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

    def remove(self, value: int) -> AVLNode | None:
        """
        Remove nodo com determinado valor da árvore AVL.
        :param value: Valor do nodo a ser removido.
        :return: Árvore com nodo removido.
        """
        if self.root is None:
            return

        self._remove(self.root, value)

        self._update_height(self.root)
        self._balance(self.root)

        return self.root

    def _remove(self, node: AVLNode, value: int) -> AVLNode | None:
        """
        Remove nodo com determinado valor da árvore AVL.
        :param node: Nodo a ser comparado.
        :param value: Valor do nodo a ser removido.
        :return: Árvore com nodo removido.
        """
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

    def _find_successor(self, node: AVLNode) -> AVLNode:
        """
        Procura o sucessor do nodo a ser removido.
        :param node: Pai do nodo a ser comparado.
        :return: Sucessor do nodo.
        """
        if node.right is None:
            return node

        successor = node.right
        while successor.left is not None:
            successor = successor.left

        return successor

    def in_order(self) -> list:
        """
        Acessa nodos da árvore utilizando o caminhamento em ordem.
        :return: Valores dos nodos.
        """
        def in_order_node(node):
            if node is not None:
                return in_order_node(node.left) + [node.value] + in_order_node(node.right)
            return []

        return in_order_node(self.root)

    def pre_order(self) -> list:
        """
        Acessa nodos da árvore utilizando o caminhamento em pré-ordem.
        :return: Valores dos nodos.
        """
        def pre_order_node(node):
            if node is not None:
                return [node.value] + pre_order_node(node.left) + pre_order_node(node.right)
            return []

        return pre_order_node(self.root)

    def post_order(self) -> list:
        """
        Acessa nodos da árvore utilizando o caminhamento em pós-ordem.
        :return: Valores dos nodos.
        """
        def post_order_node(node):
            if node is not None:
                return post_order_node(node.left) + post_order_node(node.right) + [node.value]
            return []

        return post_order_node(self.root)
