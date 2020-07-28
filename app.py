
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
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(
            csv.encode()
        ).decode()  # some strings <-> bytes conversions necessary here
        return f'<a href="data:file/csv;base64,{b64}" download="copyright.csv">Download csv file</a>'
    
    if sentence:
        df3 = {'name' : [sentence]}
        df3 = pd.DataFrame(df3)
        df3 = CopyRight(df3)
        st.dataframe(df3)

    if data is not None:
        df = pd.read_csv(data, encoding = 'utf-8')