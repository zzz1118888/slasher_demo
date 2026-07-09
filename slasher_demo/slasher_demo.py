import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

# 更推荐的方式：直接读取独立的 index.html 文件
with open("slash_demo.html", "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=1200, scrolling=True)
