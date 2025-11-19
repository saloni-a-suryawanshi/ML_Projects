import streamlit as st
from langgraph_backend import graph   # your backend file

st.set_page_config(page_title="LangGraph Streamlit Frontend", page_icon="⚡")

st.title("⚡ LangGraph Streamlit Frontend")

st.subheader("📌 Graph Structure (GraphViz)")

# --- SHOW GRAPH USING GRAPHVIZ ---
try:
    gv = graph.get_graph().draw_graphviz()
    st.graphviz_chart(gv)
except Exception as e:
    st.error(f"GraphViz rendering error: {e}")


st.subheader("📝 Run the Graph")

user_input = st.text_input("Enter your message:")

if st.button("Run Graph"):
    result = graph.invoke({"message": user_input})
    st.success("Output:")
    st.write(result["message"])
