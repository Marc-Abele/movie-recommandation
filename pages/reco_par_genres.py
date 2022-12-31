import bs4
import pandas as pd
import requests
import streamlit as st
from bs4 import BeautifulSoup
from outils import affiche, title, synopsis, pays
import time


liste_genres = ['Action', 'Adult', 'Adventure', 'Animation',
                'Biography', 'Comedy', 'Crime', 'Documentary',
                'Drama', 'Family', 'Fantasy', 'Film-Noir',
                'Game-Show', 'History', 'Horror', 'Music', 
                'Musical', 'Mystery', 'News', 'Reality-TV', 
                'Romance', 'Sci-Fi', 'Short', 'Sport', 
                'Talk-Show', 'Thriller', 'War', 'Western']

st.title('Recommandations de films par genres')


# import du dataframe
df_final = pd.read_csv('df_fin_fin.csv')

# Reco par genre
genres_pref = st.multiselect('Choisissez vos 2 genres cinématographiques préférés',
                             options = liste_genres,
                             max_selections = 2)


if len(genres_pref) ==2:
    
    reco =df_final[(df_final[genres_pref[0]]==1) & 
                   (df_final[genres_pref[1]]==1)]\
                       .sort_values(by = 'numVotes', ascending = False)\
                           .head(10)
    
    

    st.write('Nous vous recommandons les 3 films suivants :')
    
    
    for i in range(1, 4):
               
        st.subheader(title(reco['tconst'].iloc[i]))                     # displays french title for 1st reco
        st.image(affiche(reco['tconst'].iloc[i]))                       # displays image
        st.write('Synopsis : ', synopsis(reco['tconst'].iloc[i]))       # displays synopsis
        st.write('Réalisé par :', reco['primaryName'].iloc[i])          # displays movie director(s)
        st.write('Date de sortie : ', str(reco['startYear'].iloc[i]))   # displays release year
        st.title('')                                                    # saut de ligne
        
        
    if st.button('Nos recommandations ne vous plaisent pas ? Demandez en 3 nouvelles'):
        
        for i in range(4, 7):
            
            st.subheader(title(reco['tconst'].iloc[i]))                     # displays french title for 4th reco
            st.image(affiche(reco['tconst'].iloc[i]))                       # displays image
            st.write('Synopsis : ', synopsis(reco['tconst'].iloc[i]))       # displays synopsis
            st.write('Réalisé par :', reco['primaryName'].iloc[i])          # displays movie director(s)
            st.write('Date de sortie : ', str(reco['startYear'].iloc[i]))   # displays release year
            st.title('')                                                    # saut de ligne