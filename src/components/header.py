import streamlit as st

def header_home():

    logo_url = "https://apps.odoo.com/web/image/loempia.module/117629/icon_image?unique=f600cc6"
    st.markdown(f"""
        <div style="display: flex; flex-direction: column ;align-items: center ;justify-content:center;margin-bottom :5px;margin-top:5px">    
            <img src = '{logo_url}' style = 'height : 120px;' />
            <h1 style = 'text-align : center; color : #E0E3FF'>Snap2Attend</h1>
        </div>
                    """, unsafe_allow_html = True)