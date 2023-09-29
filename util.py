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


def create_mock_tree():
    """
    Cria uma árvore teste para facilitar testes.
    """
    st.session_state.tree.insert(32)
    st.session_state.tree.insert(16)
    st.session_state.tree.insert(48)
    st.session_state.tree.insert(8)
    st.session_state.tree.insert(24)
    st.session_state.tree.insert(40)
    st.session_state.tree.insert(56)
    st.session_state.tree.insert(28)
    st.session_state.tree.insert(36)
    st.session_state.tree.insert(44)
    st.session_state.tree.insert(52)
    st.session_state.tree.insert(60)
    st.session_state.tree.insert(58)
    st.session_state.tree.insert(62)
