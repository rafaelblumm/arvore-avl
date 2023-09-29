import streamlit as st
from streamlit_echarts import st_echarts
from tree import AVLTree
from util import avl_tree_to_dict, create_mock_tree

def get_tree_options():
    """
    Recupera as configurações do treechart do StreamLit.
    :return: Configurações.
    """
    return {
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

def format_node_path(path: list) -> str:
    """
    Formata o caminho até o nodo.
    :param path: Caminho até o nodo.
    :return: Caminho formatado.
    """
    values = []
    for i in path:
        values.append(str(i.value))
    return " -> ".join(values)

# Inicializa árvore
if 'tree' not in st.session_state:
    st.session_state['tree'] = AVLTree()

# Configura página
st.set_page_config(
    page_title="Árvore AVL",
    page_icon=":deciduous_tree:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Configura painel lateral
with st.sidebar:
    st.title("Operações")
    # Inserir
    insert_input = st.number_input("Valor para Inserir", step=1, key="insert_input")
    insert = st.button("Inserir")
    st.divider()
    # Excluir
    delete_input = st.number_input("Valor para Excluir", step=1, key="delete_input")
    delete = st.button("Excluir")
    st.divider()
    # Buscar
    search_input = st.number_input("Valor para Buscar", step=1, key="search_input")
    search = st.button("Buscar")
    st.divider()

    st.caption("Enzo Porto & Rafael Blumm")


# Configura painel de caminhamentos
st.title("Árvore AVL")
top_panel = st.container()
col1, col2, col3 = top_panel.columns(3)
with col1:
    st.subheader("Caminhamentos")
    st.info(f'Pré-ordem: {st.session_state.tree.pre_order()}')
with col2:
    clear = st.button("Limpar")
    st.info(f'Em ordem: {st.session_state.tree.in_order()}')
with col3:
    mock_tree = st.button('Criar árvore teste')
    st.info(f'Pós-ordem: {st.session_state.tree.post_order()}')

# Atualiza árvore na interface gráfica
if st.session_state.tree.root is not None:
    tree_data = avl_tree_to_dict(st.session_state.tree.root)
    option = get_tree_options()
    st_echarts(option, height="700px")
else:
    top_panel.warning("Insira dados na árvore!")

# Identifica eventos da interface gráfica
if insert:
    st.session_state.tree.insert(insert_input)
    st.experimental_rerun()()
if delete:
    st.session_state.tree.remove(delete_input)
    st.experimental_rerun()()
if clear:
    st.session_state.tree = AVLTree()
    st.experimental_rerun()()
if search:
    node_path = st.session_state.tree.search(search_input)
    if node_path is None:
        top_panel.error("Nodo não encontrado!")
    else:
        top_panel.success(f'Caminho até o nodo [{search_input}]: {format_node_path(node_path)}. ' +
                          f'Altura={node_path[-1].height}')
if mock_tree:
    create_mock_tree()
    st.experimental_rerun()()
