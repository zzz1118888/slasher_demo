import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(layout="wide")

# 确保 Python 能找到该文件
# 使用 os.path.join 确保路径正确
file_path = "slash_demo.html" 

if os.path.exists(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=1200, scrolling=True)
else:
    st.error(f"找不到文件: {file_path}，请检查文件名是否正确。")
    st.write("当前目录下的文件有：", os.listdir('.'))
