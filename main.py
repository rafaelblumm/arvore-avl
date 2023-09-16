import streamlit as st
from streamlit_echarts import st_echarts
from tree import AVLNode, AVLTree

insert
insert = st.button("Inserir")
exclude = st.button("Excluir")

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
            # "top": "1%",
            # "left": "7%",
            # "bottom": "1%",
            # "right": "20%",
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

