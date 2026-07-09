import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(layout="wide")

# 找到你的 HTML 文件
file_path = os.path.join("slasher_demo", "slash_demo.html")

if os.path.exists(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
        
    # 🌟 关键修改在这里：
    # 1. height 调大到 2200（或者更大，确保底部不会被裁切）
    # 2. scrolling=False 彻底关掉内部滚动条
    components.html(html_content, height=2200, scrolling=False)
    
else:
    st.error(f"找不到文件: {file_path}，请检查文件名和路径。")
    st.write("当前 Python 的工作目录是：", os.getcwd())
    st.write("当前目录下的文件夹有：", os.listdir('.'))
    if os.path.exists("slasher_demo"):
        st.write("slasher_demo 文件夹里的文件：", os.listdir("slasher_demo"))
