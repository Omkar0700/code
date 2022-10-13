import streamlit as st 
from classi_page import show_classi
from reg_page import show_reg
page =st.sidebar.selectbox("Classifier or Regressor",("Classifier","Regressor"))
if page == "Classifier":
    show_classi()
else:
    show_reg()
