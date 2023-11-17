import pathlib
from person import Person
from tree import AVLTree
import streamlit as st
import pandas as pd
from datetime import datetime


RESOURCES = pathlib.Path(__file__).parent.parent / "resources"
DATABASE_FILE = "pessoas.csv"
CSV_SEPARATOR = ';'
TREE_KEYS = ['tree_cpf', 'tree_name', 'tree_birth']

def check_if_trees_initialized() -> bool:
    """
    Indica se árvores AVL da sessão foram inicializadas com os dados.
    :return True se árvores estão inicializadas.
    """
    for i in TREE_KEYS:
        if i not in st.session_state:
            return False
    return True

def load_trees() -> None:
    """
    Carrega árvores AVL da sessão.
    """
    for k in TREE_KEYS:
        st.session_state[k] = AVLTree()
    for k, v in pd.read_csv(RESOURCES / DATABASE_FILE, sep=CSV_SEPARATOR).iterrows():
        person = Person(v.CPF, v.RG, v.Nome, datetime.strptime(v.Nascimento, "%d/%m/%Y"), v.Cidade)
        st.session_state['tree_cpf'].insert(person.cpf, person)
        st.session_state['tree_name'].insert(person.name, person)
        st.session_state['tree_birth'].insert(person.birth, person)

def avl_tree_to_dict(node, tree_type):
    """
    Transforma a estrutura da árvore AVL em JSON para exibição na interface gráfica.
    :param node: Nodo a ser formatado em JSON.
    :return: Árvore AVL em formato JSON.
    """
    if node is None:
        return None

    children = []
    if node.right:
        children.append(avl_tree_to_dict(node.right, tree_type))
    if node.left:
        children.append(avl_tree_to_dict(node.left, tree_type))

    return {
        "name": str(node.value[0]),
        "children": children
    }
