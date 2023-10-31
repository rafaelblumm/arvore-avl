import util
import pandas as pd
import streamlit as st
from streamlit_echarts import st_echarts


SEARCH_OPTIONS = 'CPF', 'Nome', 'Nascimento'
RESULT_COLUMNS = ['CPF', 'RG', 'Nome', 'Nascimento', 'Cidade']

# Tabela de resultados
def show_results():
    """
    Exibe resultados da busca.
    """
    if option == "CPF":
        if not cpf:
            st.error('É necessário informar um CPF para a busca!')
            return
        result = trees[option].search_node(cpf)
        if not result:
            st.error(f"CPF '{cpf}' não encontrado")
        else:
            st.table(pd.DataFrame(data=result.value.to_dict()))
    else:
        st.error(f"Busca por {option.lower()} ainda não foi implementada!")

# Carrega árvores
if not util.check_if_trees_initialized():
    util.load_trees()
trees = {
    SEARCH_OPTIONS[0]: st.session_state.tree_cpf,
    SEARCH_OPTIONS[1]: st.session_state.tree_name,
    SEARCH_OPTIONS[2]: st.session_state.tree_birth
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
    st.title("Buscar")
    option = st.selectbox('Tipo de busca', SEARCH_OPTIONS)

    if option == 'Nome':
        name = st.text_input('Nome', '')
    elif option == 'Nascimento':
        date_start = st.date_input("Limite inferior", format="DD/MM/YYYY", value=None)
        date_end = st.date_input("Limite superior", format="DD/MM/YYYY", value="today")
    else:
        cpf = st.number_input('CPF', min_value=1, max_value=1_000_000_000_00, value=None)

    search = st.button("Buscar")
    st.divider()
    st.caption("Enzo Porto & Rafael Blumm")

# Resultado da busca
if search:
    show_results()
else:
    st.info(f"Informe um {option if option == 'CPF' else option.lower()} para buscar")
