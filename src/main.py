import pathlib
import pandas as pd
import streamlit as st
from streamlit_echarts import st_echarts

RESOURCES = pathlib.Path(__file__).parent.parent / "resources"
DATABASE_FILE = "pessoas.csv"

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
    option = st.selectbox(
    'Tipo de busca',
    ('CPF', 'Nome', 'Nascimento'))

    if option == 'CPF':
        cpf = st.number_input('CPF', min_value=0, max_value=999_999_999_99, value=None)
    elif option == 'Nome':
        name = st.text_input('Nome', '')
    elif option == 'Nascimento':
        date_start = st.date_input("Limite inferior", None)
        date_end = st.date_input("Limite superior", None)
    search = st.button("Buscar")
    st.divider()

    st.caption("Enzo Porto & Rafael Blumm")

# Tabela de resultados
# Obs.: enquanto busca não foi implementada, é carregado amostra de valores
data = pd.read_csv(RESOURCES / DATABASE_FILE, sep=';')
df = pd.DataFrame(data, columns=list(data.columns.values))
st.table(df)

# Identifica eventos da interface gráfica
# st.experimental_rerun()()
