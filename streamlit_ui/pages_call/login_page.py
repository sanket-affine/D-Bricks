import streamlit as st
import databricks.sql as dbsql
# from pages.user_add_page import user_add
from src.login_call import UserData
import streamlit as st



def login():
    st.markdown("""
    <div style='text-align: center; margin-top:-50px; margin-bottom: 20px;margin-left: -50px;'>
    <h2 style='font-size: 60px; font-family: Courier New, monospace;
                    letter-spacing: 2px; text-decoration: none;'>
    <img src="https://acis.affineanalytics.co.in/assets/images/logo_small.png" alt="logo" width="70" height="60">
    <span style='background: linear-gradient(45deg, #ed4965, #c05aaf);
                            -webkit-background-clip: text;
                            -webkit-text-fill-color: transparent;
                            text-shadow: none;'>
                    FashionFinder
    </span>
    <span style='font-size: 60%;'>
    <sup style='position: relative; top: 5px; color:white ;'>by Affine</sup> 
    </span>
    </h2>
    </div>
    """, unsafe_allow_html=True) 
    with st.form("login_form"):
        email_id = st.text_input("Email ID",placeholder="xyz.d@affine.ai")
        user_pass=st.text_input("Password", placeholder="admin@123",type="password")
        col1, col2 = st.columns(2)
        login = col1.form_submit_button("Login")
        # register_user = col2.form_submit_button("Register User")
   

    if login:
        st.session_state.login_flag, st.session_state.login_user_type=UserData().login(email_id,user_pass)

        if st.session_state.login_flag:
            st.session_state.login_user=email_id
            st.success("Login successfully")
        else:
            st.session_state.login_user=None
            st.error("Failed to login, please try again later")

       
           
        