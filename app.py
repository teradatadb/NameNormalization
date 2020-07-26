
import streamlit as st
import pandas as pd 
import numpy as np
import base64
from copyright import CopyRight

st.title("Copyright Name Finder")

sentence = st.text_input("Input Your Text Here :")

st.set_option('deprecation.showfileUploaderEncoding', False)

data = st.file_uploader("Upload a Dataset", type=["csv","txt"])


def main():

    def download_file(df):
        """
        Generates a link allowing the data in a given panda dataframe to be downloaded
        in:  dataframe
        out: href string
        """