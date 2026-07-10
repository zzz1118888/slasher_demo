import streamlit as st
import os

st.set_page_config(layout="wide")

file_path = os.path.join("slasher_demo", "slash_demo.html")

if os.path.exists(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
        
    # 🌟 捨棄 components.html，改用 st.markdown
    # 加上 unsafe_allow_html=True，讓 HTML 直接渲染，高度完美自適應！
    st.markdown(html_content, unsafe_allow_html=True)
    
else:
    st.error(f"找不到文件: {file_path}，請檢查文件名和路徑。")
