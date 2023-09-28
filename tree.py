class AVLNode:
    """
    Classe que representa um nodo em uma árvore AVL.
    """
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
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
        if self.search_node(value) is not None:
            return
        self.root = self._insert(self.root, value)

    def _insert(self, node: AVLNode, value: int) -> AVLNode:
        """
        Insere um valor na árvore.
        :param node: Nodo pai.
        :param value: Valor a ser inserido.
        :return: Nodo pai do nodo inserido.
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

    def search(self, value: int) -> list | None:
        """
        Procura por um nodo com determinado valor.
        :param value: Valor desejado.
        :return: Caminho até o nodo procurado.
        """
        if self.root is None or value is None:
            return
        return self._search(self.root, value, [])

    def _search(self, node: AVLNode, value: int, path: list) -> list | None:
        """
        Procura por um nodo com determinado valor.
        :param node: Nodo a ser comparado.
        :param value: Valor desejado.
        :param path: Caminho percorrido na árvore.
        :return: Caminho até o nodo procurado.
        """
        if node is None:
            return None

        path.append(node)
        if value < node.value:
            return self._search(node.left, value, path)
        if value > node.value:
            return self._search(node.right, value, path)
        return path

    def search_node(self, value: int) -> AVLNode | None:
        """
        Procura por determinado nodo.
        :param value: Valor do nodo.
        :return: Nodo encontrado.
        """
        path = self.search(value)
        return path[-1] if path is not None else None

    def _update_height(self, node: AVLNode) -> None:
        """
        Atualiza o atributo de altura de um nodo.
        :param node: Nodo a ser atualizado.
        """
        if node:
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
        if self.root is None or self.search(value) is None:
            return

        self._remove(self.root, value)
        self._update_height(self.root)
        self.root = self._balance(self.root)
        return self.root

    def _remove(self, node: AVLNode, value: int, parent: AVLNode = None) -> AVLNode | None:
        """
        Remove nodo com determinado valor da árvore AVL.
        :param node: Nodo a ser comparado.
        :param value: Valor do nodo a ser removido.
        :param parent: Pai do nodo a ser comparado. Default=None.
        :return: Árvore com nodo removido.
        """
        # @TODO: remover raiz
        # @TODO: corrigir balanceamento da árvore após remoção
        if not node:
            return
        elif value < node.value:
            return self._remove(node.left, value, node)
        elif value > node.value:
            return self._remove(node.right, value, node)

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
        if parent.right == node:
            parent.right = None
        else:
            parent.left = None
        return parent

    def _remove_node_has_left_child(self, node: AVLNode, parent: AVLNode) -> AVLNode:
        if parent.right == node:
            parent.right = node.left
        else:
            parent.left = node.left
        return parent

    def _remove_node_has_right_child(self, node: AVLNode, parent: AVLNode) -> AVLNode:
        if parent.right == node:
            parent.right = node.right
        else:
            parent.left = node.right
        return parent

    def _remove_node_with_both_child(self, node: AVLNode, parent: AVLNode) -> AVLNode:
        successor = self._find_successor(node)
        successor_parent = self._find_parent(successor)
        aux = parent.right if parent.right == node else parent.left
        aux.value = successor.value
        return self._remove(successor, successor.value, successor_parent)

    def _find_successor(self, node: AVLNode) -> AVLNode:
        """
        Procura o sucessor do nodo a ser excluído por cópia.
        :param node: Nodo a ser removido.
        :return: Sucessor do nodo.
        """
        if node.left.right is not None:
            return node.left.right
        return node.left

    def _find_parent(self, node: AVLNode) -> AVLNode:
        """
        Recupera o pai do nodo informado.
        :param node: Nodo cujo pai será recuperado.
        :return: Pai do nodo informado.
        """
        return self.search(node.value)[-2]

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
