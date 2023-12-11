import streamlit as st
import pandas as pd
import os


def select():
    export_folder = './export/'
    file_name = os.listdir(export_folder)  # Assuming there is only one file in the folder

    return file_name

with st.form('Form 1'):
    option = st.selectbox('Select', select())

    if st.form_submit_button('Submit'):
        df = pd.read_json('./export/' + option)
        st.write(df)



