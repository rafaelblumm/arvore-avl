import streamlit as st
from streamlit_echarts import st_echarts
from tree import AVLNode, AVLTree

insert_input = st.number_input("Valor para Inserir", step=1)
insert = st.button("Inserir")
delete_input = st.number_input("Valor para Excluir", step=1)
delete = st.button("Excluir")


if 'tree' not in st.session_state:
    st.session_state['tree'] = AVLTree()

if insert:
    st.session_state.tree.insert(insert_input)
if delete:
    st.session_state.tree.remove(delete_input)

print(st.session_state.tree)

main_tree = {
    'name': 'Arvore Avl',
    'children': [{'name': '0'}]
}

option = {
    "tooltip": {"trigger": "item", "triggerOn": "mousemove"},
    "series": [
        {
            "type": "tree",
            "roam": True,
            "data": [main_tree],
            "symbolSize": 10,
            "initialTreeDepth": 3,
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

