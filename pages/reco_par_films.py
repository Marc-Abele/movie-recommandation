import streamlit as st
import bs4
import pandas as pd
import requests
from bs4 import BeautifulSoup
from sklearn.neighbors import NearestNeighbors
from outils import affiche, title, synopsis, pays

st.title('Recommandations par films')

df_final = pd.read_csv('df_fin_fin.csv')



X = df_final[['startYear_div', 'runtimeMinutes_rs', 'averageRating_div', 'numVotes_mms',
              'Action', 'Adult', 'Adventure', 'Animation', 'Biography', 'Comedy',
              'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'Film-Noir',
              'Game-Show', 'History', 'Horror', 'Music', 'Musical', 'Mystery', 'News',
              'Reality-TV', 'Romance', 'Sci-Fi', 'Short', 'Sport', 'Talk-Show',
              'Thriller', 'War', 'Western']]


distanceKNN = NearestNeighbors(n_neighbors=10).fit(X)

choix = st.multiselect(label = 'Sélectionnez au moins un film (max. 2)',
               options = df_final['originalTitle'],
               max_selections = 2)

if st.button('Conseillez-moi !'):
    
    if len(choix) == 0:
        st.write('Sélectionnez au moins un film !')
        st.markdown("![Alt Text](https://i.gifer.com/uBt.gif)")
        
    if len(choix) == 1:
        reco_films = df_final.iloc[distanceKNN.kneighbors(X.iloc[df_final[df_final['originalTitle']==choix[0]].index])[1][0][:]]
        
        st.write('Nous vous recommandons les 3 films suivants :')
        
        for i in range(1, 6):
            st.subheader(title(reco_films['tconst'].iloc[i]))                 # displays french title for 1st reco
            st.image(affiche(reco_films['tconst'].iloc[i]))                   # displays image
            st.write('Synopsis : ', synopsis(reco_films['tconst'].iloc[i]))   # displays synopsis
            st.write('Réalisé par :', reco_films['primaryName'].iloc[i])      # displays movie director(s)
            st.write('Date de sortie : ', str(reco_films['startYear'].iloc[i]))   # displays release year
            st.title('')   # saut de ligne

            

    if len(choix) == 2:
        reco_films = df_final.iloc[distanceKNN.kneighbors([((X.iloc[df_final[df_final['originalTitle'] == choix[0]].index]).squeeze('rows') +\
            (X.iloc[df_final[df_final['originalTitle'] == choix[1]].index]).squeeze('rows'))/2])[1][0][:]]
        
        st.write('Nous vous recommandons les 3 films suivants :')
        
        for i in range(6):
            st.subheader(title(reco_films['tconst'].iloc[i]))                 # displays french title for 0st reco
            st.image(affiche(reco_films['tconst'].iloc[i]))                   # displays image
            st.write('Synopsis : ', synopsis(reco_films['tconst'].iloc[i]))   # displays synopsis
            st.write('Réalisé par :', reco_films['primaryName'].iloc[i])      # displays movie director(s)
            st.write('Date de sortie : ', str(reco_films['startYear'].iloc[i]))   # displays release year
            st.title('')   # saut de ligne
