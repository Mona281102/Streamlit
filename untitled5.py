# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1E_nTktAsgnCDf17HYOgM3RXhmk0FeKHP
"""

pip install streamlit

# Commented out IPython magic to ensure Python compatibility.
%%writefile our_app.py
import streamlit as st
st.write("hello")

! wget -q -O - ipv4.icanhazip.com

! streamlit run our_app.py & npx localtunnel --port 8501
