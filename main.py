import streamlit as st
from anytree import Node, RenderTree
from streamlit_echarts import st_echarts


st.button("Inserir")
st.button("Excluir")

root = Node("3")
node1 = Node("1", parent=root)
node2 = Node("2", parent=root)
node3 = Node("4", parent=node2)
node4 = Node("5", parent=node3)

option = {
    "tooltip": {"trigger": "item", "triggerOn": "mousemove"},
    "series": [
        {
            "type": "tree",
            "roam": True,
            "data": [root],
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

