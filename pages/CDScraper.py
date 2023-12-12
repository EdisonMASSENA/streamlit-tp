import streamlit as st
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import sqlalchemy as db

from Database import DataBase



def scrap_cdiscount(search):

    driver = webdriver.Chrome()
    driver.get('https://www.cdiscount.com/')

    time.sleep(2)

    driver.find_element(By.ID, "search").send_keys(search)
    driver.find_element(By.ID, "search").send_keys(Keys.ENTER)

    time.sleep(2)

    json_list = []
    produit = driver.find_elements(By.CLASS_NAME, "jsPrdBlocContainer")

    for i in range(len(produit)):
        # time.sleep(1)
        nom = produit[i].find_element(By.CLASS_NAME, "prdtBILTit").text
        try:
            note = produit[i].find_element(By.CLASS_NAME, "u-visually-hidden").text
        except:
            note = ''
        photo = produit[i].find_element(By.CLASS_NAME, "prdtBImg").get_attribute("src")
        lien = produit[i].find_element(By.TAG_NAME, "a").get_attribute("href")
        prix = produit[i].find_element(By.CLASS_NAME, "price").text
        
        json_list.append({"nom": nom, "note": note, "photo": photo, "lien": lien, "prix": prix})
    
    df = pd.DataFrame(json_list)

    df.to_csv(f"./export/{search}.csv", index=False)

    return df


database = DataBase('cdiscountDB')


st.title("Cdiscount Scraper")

with st.form(key='my_form'):
    search = st.text_input("Recherchez un produit")
    submitted = st.form_submit_button("Search")


    if submitted:
        df = scrap_cdiscount(search)
        st.write(df)
        database.create_table(search, id_product=db.Integer, nom=db.String, note=db.String, photo=db.String, lien=db.String, prix=db.String)
        for i in range(len(df)):
            database.add_row(search, id_product=i, nom=df.nom[i], note=df.note[i], photo=df.photo[i], lien=df.lien[i], prix=df.prix[i])






