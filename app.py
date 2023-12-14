import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="My Streamlit App",
    page_icon='🧠',
    layout="wide"
)

st.title("My first Title")

st.markdown("""
# Titre
## Sous-titre
```
            print('Hello World')
```          
"""
)

# Sous-titre
st.subheader("Subheader")

# Afficher des éléments sur la page
st.write("Bonjour tout le monde !")

df = pd.read_json('data.json')
if st.checkbox('Afficher le dataframe'):
    st.write(df)

# Création de colonnes
col1, col2 = st.columns(2)

with col1:
    # Graphique avec matplotlib
    fig, ax = plt.subplots()
    ax.hist(df.tag)
    st.pyplot(fig)

with col2:
    # Graphique avec plotly.expres
    st.plotly_chart(px.histogram(df.tag))

theme = st.selectbox('Sélectionnez le thème : ', df.tag.value_counts().index)

st.write(theme, len(df[df.tag == theme].tag))

text = st.text_input('Tape your text')
st.title(text)


with st.form('Form 1'):
    name = st.text_input('Tape your name')
    age = st.slider('Select your age : ', 0, 100)

    if st.form_submit_button('Send Form'):
        st.write('Your name : %s'%(name))
        st.write(f'Your age : {age}')
