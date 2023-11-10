import util
import pandas as pd
import streamlit as st


CPF = 0
NAME = 1
BIRTH = 2
SEARCH_OPTIONS = ['CPF', 'Nome', 'Nascimento']
RESULT_COLUMNS = ['CPF', 'RG', 'Nome', 'Nascimento', 'Cidade']

# Tabela de resultados
def show_results():
    """
    Exibe resultados da busca.
    """
    if search_value is None:
        st.error('É necessário informar um valor para a busca!')
        return

    result = trees[option].search_node(search_value)
    if result is None or len(result) == 0:
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
    st.title("ÁRVORE AVL - Busca")
    option = st.selectbox('Tipo de busca', SEARCH_OPTIONS)

    search_value = None
    if option == SEARCH_OPTIONS[NAME]:
        search_value = st.text_input('Nome', '')
    elif option == SEARCH_OPTIONS[BIRTH]:
        date_start = st.date_input("Limite inferior", format="DD/MM/YYYY", value=None)
        date_end = st.date_input("Limite superior", format="DD/MM/YYYY", value="today")
        search_value = [date_start, date_end]
    else:
        search_value = st.number_input('CPF', min_value=1, max_value=1_000_000_000_00, value=None)

    search = st.button("Buscar")
    st.divider()
    st.caption("Enzo Porto & Rafael Blumm")

# Configura painel central
aux = f"{search_value}" if option != SEARCH_OPTIONS[BIRTH] and search_value is not None else ''
st.subheader(f"Resultado: {aux}", divider="gray")

# Resultado da busca
if search:
    show_results()
else:
    st.info(f"Informe um {option if option == SEARCH_OPTIONS[CPF] else option.lower()} para buscar")
