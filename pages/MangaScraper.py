import streamlit as st
import pandas as pd
import requests


def scrap_manga(search):

    response = requests.get("http://localhost:8000/search", params={'search': search})
    df = pd.DataFrame(response.json())
    return df


st.title("Manga Scraper")

col1, col2 = st.columns(2)

with st.form(key='my_form'):
    search = st.text_input("Recherchez un manga")
    submitted = st.form_submit_button("Search")

    if submitted:
        datas = scrap_manga(search)
        st.write(datas)

        # for data in datas:
        #     with col1:
        #         st.image(data['img'])
        #     with col2:
        #         st.write(data['title'])
        #         st.write(data['desc'])