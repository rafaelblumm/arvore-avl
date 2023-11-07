import pathlib
from person import Person
from tree import AVLTree
import streamlit as st
import pandas as pd


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
        person = Person(v.CPF, v.RG, v.Nome, v.Nascimento, v.Cidade)
        st.session_state['tree_cpf'].insert(person.cpf, person)
        st.session_state['tree_name'].insert(person.name, person)
