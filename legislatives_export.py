# %% [markdown]
# ### Initialisation

# %%
import streamlit
import pandas as pd
import plotly.express as px

streamlit.title('Carte des résulats aux élections législavives françaises 2022')
streamlit.header('C\'est pas trop dégueu, non ?')


# %% [markdown]
# ### Chargement et préparation des données

# %%

data = pd.read_csv('data_leg_final.csv')
data


# %%
import json

with open('france-circonscriptions-legislatives-2012.json', 'r') as file:
    circonscriptions = json.load(file)

# %%
# ### Visualisation
labels = {
    'Libellé_circonscription' : 'Circonscription',
    'Libellé_département' : 'Département',
    'Victoire_contre' : 'Adversaire', 
}

hdat = {
    'Libellé_circonscription' : True,
    'Libellé_département' : True,
    'Prénom' : True, 
    'Nom' : True, 
    'Victoire_contre' : True, 
    'id_circonscription' : False

    
}

color_map = {
    'Divers' : '#C7C7C7',                                    
    'Divers centre' : '#FAC577',                       
    'Divers droite' : '#adc1fd',        
    'Divers gauche' : '#ffc0c0',                          
    'Droite souverainiste' : '#8040C0',                      
    'Ensemble!' : '#ffeb00',                            
    'Les Républicains' : '#0066cc',                      
    'NUPES' : '#BB1840',                                 
    'Rassemblement National' : '#0D378A',                 
    'Régionalistes' : '#DCBFA3',                           
    'Union des démocrates et indépendants' : '#ffed99' }


fig = px.choropleth_mapbox(data, geojson=circonscriptions, featureidkey='properties.ID', locations='id_circonscription', hover_data=hdat,
                            color='Nuance', color_discrete_map= color_map, center={"lat": 46.3622, "lon":1.5231}, labels=labels, mapbox_style="carto-positron", zoom=4)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()


