import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(layout="wide")

# 关键修改：告诉它文件在 slasher_demo 这个子文件夹里
file_path = os.path.join("slasher_demo", "slash_demo.html")

if os.path.exists(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    # 渲染 HTML
    components.html(html_content, height=1200, scrolling=True)
else:
    st.error(f"找不到文件: {file_path}，请检查文件名和路径。")
    st.write("当前 Python 的工作目录是：", os.getcwd())
    st.write("当前目录下的文件夹有：", os.listdir('.'))
    # 尝试列出 slasher_demo 文件夹里的内容，帮你确认
    if os.path.exists("slasher_demo"):
        st.write("slasher_demo 文件夹里的文件：", os.listdir("slasher_demo"))
