import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(layout="wide")

file_path = os.path.join("slasher_demo", "slash_demo.html")

if os.path.exists(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
        
    # 🌟 暴力破解：直接給 8000，確保在所有螢幕上都不會切底
    components.html(html_content, height=3500, scrolling=False)
    
else:
    st.error(f"找不到文件: {file_path}，请检查文件名和路径。")
