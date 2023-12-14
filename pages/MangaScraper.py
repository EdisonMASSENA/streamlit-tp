import streamlit as st
import pandas as pd
import requests


def scrap_manga(search):

    response = requests.get("http://localhost:8000/search", params={'search': search})
    df = pd.DataFrame(response.json())
    return df


st.title("Manga Scraper")


with st.form(key='my_form'):
    search = st.text_input("Recherchez un manga")
    submitted = st.form_submit_button("Search")

    if submitted:
        datas = scrap_manga(search)
        st.write(datas)

        img_values = datas['img'].values
        titles = datas['title'].values
        col1, col2 = st.columns(2)

        with col1:
            for img in img_values:
                st.image(img)
        with col2:
            for title in titles:
                st.write(title) 
            



    