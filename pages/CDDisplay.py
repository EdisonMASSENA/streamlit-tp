import streamlit as st
import pandas as pd
from Database import *

database = DataBase('cdiscountDB')

st.title("Cdiscount Display")

tables = database.get_tables()

selectTable =  st.selectbox('Select a table', tables)

table = database.select_table(selectTable)

df = pd.DataFrame(table)

st.write(df)






