import util
import pandas as pd
import streamlit as st
from streamlit_echarts import st_echarts


CPF = 0
NAME = 1
BIRTH = 2
SEARCH_OPTIONS = ['CPF', 'Nome', 'Nascimento']
RESULT_COLUMNS = ['CPF', 'RG', 'Nome', 'Nascimento', 'Cidade']

def get_tree_options(tree):
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
                "data": [util.avl_tree_to_dict(tree.root, option)],
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

# Tabela de resultados
def show_results():
    """
    Exibe resultados da busca.
    """
    if search_value is None:
        st.error('É necessário informar um valor para a busca!')
        return
    
    if option == SEARCH_OPTIONS[BIRTH] and search_value[0] > search_value[1]:
        st.error('O limite superior deve ser maior que o limite inferior!')
        return

    result = trees[option].search_node(search_value)
    if result is None:
        st.error('Cadastro não encontrado!')
        return
    
    if not result:
        if option == SEARCH_OPTIONS[CPF]:
            st.error(f"CPF '{search_value}' não encontrado")
        if option == SEARCH_OPTIONS[NAME]:
            st.error(f"Nome '{search_value}' não encontrado")
    else:
        dataframes = []
        if isinstance(result, list):
            for item in result:
                for value in item.value:
                    dataframes.append(pd.DataFrame(data=value.to_dict()))
        else:
            for value in result.value:
                dataframes.append(pd.DataFrame(data=value.to_dict()))

        st.table(pd.concat(dataframes))


# Carrega árvores
if not util.check_if_trees_initialized():
    util.load_trees()
trees = {
    SEARCH_OPTIONS[CPF]: st.session_state.tree_cpf,
    SEARCH_OPTIONS[NAME]: st.session_state.tree_name,
    SEARCH_OPTIONS[BIRTH]: st.session_state.tree_birth
}

# Configura página
st.set_page_config(
    page_title="Busca em cadastro",
    page_icon="	:mag:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Configura painel lateral
with st.sidebar:
    search_value = None
    search = ''
    st.title("ÁRVORE AVL - Busca")
    show_tree = st.toggle('Exibir árvore')
    option = st.selectbox('Tipo de busca', SEARCH_OPTIONS)
    st.session_state['option'] = option
    if not show_tree:
        if option == SEARCH_OPTIONS[NAME]:
            search_value = st.text_input('Nome', '')
        elif option == SEARCH_OPTIONS[BIRTH]:
            search_value = [
                st.date_input("Limite inferior", format="DD/MM/YYYY", value=None),
                st.date_input("Limite superior", format="DD/MM/YYYY", value="today")
            ]
        else:
            search_value = st.number_input('CPF', min_value=1, max_value=1_000_000_000_00, value=None)
        search = st.button("Buscar")
    st.divider()
    st.caption("Enzo Porto & Rafael Blumm")

# Configura painel central
if show_tree:
    st_echarts(get_tree_options(trees[option]), height="700px")
else:
    aux = f"{search_value}" if option != SEARCH_OPTIONS[BIRTH] and search_value is not None else ''
    st.subheader(f"Resultado: {aux}", divider="gray")

# Resultado da busca
if search:
    show_results()
else:
    st.info(f"Informe um {option if option == SEARCH_OPTIONS[CPF] else option.lower()} para buscar")
