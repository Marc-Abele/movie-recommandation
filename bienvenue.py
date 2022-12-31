import streamlit as st


st.title('Bienvenue dans votre cinéma favori')
st.image('bienvenue.jpg', use_column_width='always')
st.header('')
st.subheader('Votre cinéma vous propose un tout nouveau service de recommandations cinématographiques : CreuseFlix')

st.write("- Vous souhaitez avoir des conseils d'après votre acteur fétiche ?")
st.write("\u27A1\uFE0F Direction salle 1 : reco par acteur")
st.write('')
st.write("- Vous souhaitez avoir des conseils d'après vos films favoris ?")
st.write("\u27A1\uFE0F Direction salle 2 : reco par films")
st.write('')
st.write("- Vous n'avez pas d'idée ? Dites nous vos genres préférés, nous nous occupons du reste.")
st.write("\u27A1\uFE0F Direction salle 3 : reco par genres")


