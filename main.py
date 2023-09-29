import streamlit as st
from streamlit_echarts import st_echarts
from tree import AVLTree
from util import avl_tree_to_dict, create_mock_tree

# Inicializa árvore
if 'tree' not in st.session_state:
    st.session_state['tree'] = AVLTree()

# Configura elementos da interface gráfica
st.write("Operações")
col1, col2, col3 = st.columns(3)
with col1:
    insert_input = st.number_input("Valor para Inserir", step=1)
    insert = st.button("Inserir")
    st.success(f'Caminhamento em pré-ordem: {st.session_state.tree.pre_order()}')
    clear = st.button("Limpar")
with col2:
    delete_input = st.number_input("Valor para Excluir", step=1)
    delete = st.button("Excluir")
    st.warning(f'Caminhamento em ordem: {st.session_state.tree.in_order()}')
    mock_tree = st.button('Criar árvore teste')
with col3:
    search_input = st.number_input("Valor para Buscar", step=1)
    search = st.button("Buscar")
    st.error(f'Caminhamento em pós-ordem: {st.session_state.tree.post_order()}')

# Identifica eventos da interface gráfica
if insert:
    st.session_state.tree.insert(insert_input)
    st.rerun()
if delete:
    st.session_state.tree.remove(delete_input)
    st.rerun()
if clear:
    st.session_state.tree = AVLTree()
    st.rerun()
if mock_tree:
    create_mock_tree()
    st.rerun()

# Atualiza árvore na interface gráfica
if st.session_state.tree.root is not None:
    tree_data = avl_tree_to_dict(st.session_state.tree.root)
    option = {
        "tooltip": {"trigger": "item", "triggerOn": "mousemove"},
        "series": [
            {
                "type": "tree",
                "roam": True,
                "data": [tree_data],
                "symbolSize": 10,
                "initialTreeDepth": 999,
                "label": {
                    "position": "top",
                    "verticalAlign": "middle",
                    "align": "center",
                    "fontSize": 14,
                    "distance": 10,
                    "backgroundColor": "#ffffffb0",
                    "padding": 5,
                    "borderRadius": 5
                },
                "leaves": {
                    "label": {
                        "position": "right",
                        "verticalAlign": "middle",
                        "align": "left",
                    }
                },
                "emphasis": {"focus": "descendant"},
                "expandAndCollapse": True,
                "animationDuration": 550,
                "animationDurationUpdate": 750,
            }
        ],
    }
    st_echarts(option, height="700px")
else:
    st.warning("Insira dados na árvore!")
