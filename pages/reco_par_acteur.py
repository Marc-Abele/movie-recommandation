import bs4
import pandas as pd
import requests
import streamlit as st
from bs4 import BeautifulSoup
from outils import affiche, title, synopsis, pays
import time


# import du dataframe actors
actors = pd.read_csv('actors_names_movie_rating.csv')

list_actors = list(actors['primaryName'].unique())


acteur_pref = st.multiselect('Choisissez votre acteur préféré',
                             options = list_actors,
                             max_selections = 1)

if len(acteur_pref) == 1:
    
    reco_acteur = actors[actors['primaryName'] == acteur_pref[0]].sort_values(by = 'numVotes', ascending = False)
           
    if st.button('Conseillez-moi !'):
        
        st.write('Nous vous recommandons les 3 films suivants :')

        for i in range(1, 4):
            st.subheader(title(reco_acteur['tconst'].iloc[i]))                 # displays french title for 1st reco
            st.image(affiche(reco_acteur['tconst'].iloc[i]))                   # displays image
            st.write('Synopsis : ', synopsis(reco_acteur['tconst'].iloc[i]))   # displays synopsis
            if reco_acteur['genre2'].iloc[i] == '0':
                st.write('Genre : ', reco_acteur['genre1'].iloc[i])
            elif reco_acteur['genre3'].iloc[i] == '0':
                st.write('Genres : ', reco_acteur['genre1'].iloc[i] + ", " + reco_acteur['genre2'].iloc[i])
            else :
                st.write('Genres : ', reco_acteur['genre1'].iloc[i] + ", " + reco_acteur['genre2'].iloc[i] + ", " + reco_acteur['genre3'].iloc[i])
            
            st.title('')   # saut de ligne