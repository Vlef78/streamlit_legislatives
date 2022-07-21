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


'''
# %% [markdown]
# ### Extraction des insights

# %%
#Stats inscrits
inscrits = data.Inscrits.agg([sum, min, max])
inscrits

# %%
#Stats votants
votants = data.Votants.agg([sum, min, max])
votants 


# %%
#Stats par nuance/nb votants 

tot_vot = data.Votants.sum()
blancs = data.Blancs.sum()
nuls = data.Nuls.sum()

stat_vot = data.groupby(['Nuance']).Voix.sum()  

stat_vot_def = stat_vot.apply(lambda x : round((x/tot_vot)*100,4)) # % par nuance


stat_vot_bl_nul = pd.concat([stat_vot,pd.Series({'BLA' : blancs, 'NUL' : nuls})])
stat_vot_bl_nul = stat_vot_bl_nul.apply(lambda x: round((x/tot_vot)*100,4))# % par nuance avec blancs et nuls
stat_vot_bl_nul

# %%
#Stats par nuance/nb inscrits

tot_inscr = data.Inscrits.sum()
abs = tot_inscr - tot_vot
stat_vot_inscr = data.groupby(['Nuance']).Voix.sum()
stat_vot_inscr = pd.concat([stat_vot,pd.Series({'BLA' : blancs, 'NUL' : nuls, 'ABS' : abs})])
stat_vot_inscr = stat_vot_inscr.apply(lambda x : round((x/tot_inscr)*100,4))
stat_vot_inscr

# %%
#Stat siège député

sieges = data.groupby(['Nuance']).Nuance.count()
sieges

# %%
#Duels

duels = data.loc[:, ['id_circonscription', 'Libellé_département', 'Nuance', 'Victoire_contre']]
duels

# %%
compo_duels = duels.value_counts(['Nuance', 'Victoire_contre'])

# %%
#Stat par circonscription

circ = data.loc[:, ['id_circonscription', 'Libellé_département', 'Nuance']]


# %% [markdown]


'''
