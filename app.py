
import streamlit as st
import pandas as pd 
import numpy as np
import base64
from copyright import CopyRight

st.title("Copyright Name Finder")

sentence = st.text_input("Input Your Text Here :")

st.set_option('deprecation.showfileUploaderEncoding', False)