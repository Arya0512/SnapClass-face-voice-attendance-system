import streamlit as st


def footer_home():
    st.markdown("""
        <style>
            .arya{
                font-family:cursive;
                font-size:18px;
                color:#E53950;
                font-weight:bold;
                position:relative;
                top:-2px;   /* Try -1px, -2px, or -3px */
            }
        </style>

        <div style="margin-top:2rem; display:flex; justify-content:center; align-items:center; gap:6px;">
            <span style="font-weight:bold; color:white;">Created with ❤️ by</span>
            <span class="arya">Arya</span>
        </div>
        """, unsafe_allow_html=True)
    

def footer_dashboard():
    st.markdown("""
        <style>
            .arya{
                font-family:cursive;
                font-size:18px;
                color:#E53950;
                font-weight:bold;
                position:relative;
                top:-2px;   /* Try -1px, -2px, or -3px */
            }
        </style>

        <div style="margin-top:2rem; display:flex; justify-content:center; align-items:center; gap:6px;">
            <span style="font-weight:bold;">Created with ❤️ by</span>
            <span class="arya">Arya</span>
        </div>
        """, unsafe_allow_html=True)