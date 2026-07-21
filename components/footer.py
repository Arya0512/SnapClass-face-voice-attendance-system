import streamlit as st


def footer_home():
    logo_url = "https://www.jready.org/wp-content/uploads/2025/05/Arya-Logotype-RGB-BrightCrimson.png"
    
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
        <p style="font-weight:bold; color:white;"> Created with ❤️ by</p>  
        <img src='{logo_url}' style='height:35px;'/>
        </div>
                
                """, unsafe_allow_html=True)