import streamlit as st


def avl_tree_to_dict(node):
    """
    Transforma a estrutura da árvore AVL em JSON para exibição na interface gráfica.
    :param node: Nodo a ser formatado em JSON.
    :return: Árvore AVL em formato JSON.
    """
    if node is None:
        return None

    children = []
    if node.right:
        children.append(avl_tree_to_dict(node.right))
    if node.left:
        children.append(avl_tree_to_dict(node.left))

    return {
        "name": str(node.value),
        "children": children
    }
