# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 09:30:01 2020

@author: utilisateur
"""

import pandas as pd
import json
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import plot
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html



dateparse = lambda dates : pd.datetime(dates, '%d-%m-%Y')

declaration_avantage = pd.read_csv('declaration_avantage_2020_02_19_04_00.csv', sep=";", parse_dates=["avant_date_signature"], low_memory=False)
declaration_convention = pd.read_csv('declaration_convention_2020_02_19_04_00.csv', sep=";", parse_dates=["conv_date_debut", "conv_date_signature"], low_memory=False )
entreprise = pd.read_csv('entreprise_2020_02_19_04_00.csv', low_memory=False )
"""
declaration_remuneration = pd.read_csv('declaration_remuneration_2020_02_19_04_00.csv', sep=";", parse_dates=["remu_date"], low_memory=False )

"""
declaration_remuneration = pd.read_csv('declaration_remuneration_2020_02_19_04_00.csv', sep=";",low_memory=False )

"""---------------------------------------------------------------"""
"""
# INFO TABLES GENERALES
declaration_avantage.dtypes
declaration_convention.dtypes
declaration_remuneration.dtypes
entreprise.dtypes

declaration_avantage.info()
declaration_convention.info()
declaration_remuneration.info()
entreprise.info()

declaration_remuneration["remu_date"].min()
"""
"""---------------------------------------------------------------"""



"""---------------------------------------------------------------"""
# INFO TABLE AVANTAGE
"""
for col in declaration_avantage.columns :
    print(col + " : "+str(len(list(declaration_convention[col].unique()))))
    
# RECUP ET CREATION DES DICOS DE CORRESPONDANCE

code = []
libelle = []

for col in declaration_avantage.columns :
    print(col + " : "+str(len(list(declaration_avantage[col].unique()))))
    if col == "benef_categorie_code" :
        code.append(list(declaration_avantage[col].unique()))
    elif col == "categorie" :
        libelle.append(list(declaration_avantage[col].unique()))
    elif col == "benef_qualite_code" :
        code.append(list(declaration_avantage[col].unique()))
    elif col == "qualite" :
        libelle.append(list(declaration_avantage[col].unique()))
    elif col == "benef_pays_code" :
        code.append(list(declaration_avantage[col].unique()))
    elif col == "pays" :
        libelle.append(list(declaration_avantage[col].unique()))
    elif col == "benef_titre_code" :
        code.append(list(declaration_avantage[col].unique()))
    elif col == "benef_titre_libelle" :
        libelle.append(list(declaration_avantage[col].unique()))
    elif col == "benef_specialite_code" :
        code.append(list(declaration_avantage[col].unique()))
    elif col == "benef_speicalite_libelle" :
        libelle.append(list(declaration_avantage[col].unique()))
    elif col == "benef_identifiant_type_code" :
        code.append(list(declaration_avantage[col].unique()))
    elif col == "identifiant_type" :
        libelle.append(list(declaration_avantage[col].unique()))

dico_benef_categ = {}
for i in range (0, len(code[0])) :
    dico_benef_categ[code[0][i]] = libelle[0][i]
    
dico_benef_qualite = {}
for i in range (0, len(code[1])) :
    print(str(len(code[1])))
    print(str(len(libelle[1])))
    dico_benef_qualite[code[1][i]] = libelle[1][i]

dico_benef_pays = {}
for i in range (0, len(code[2])) :
    print(str(code[2][i]))
    print(str(libelle[2][i]))
    dico_benef_pays[code[2][i]] = libelle[2][i]
        
dico_benef_titre = {}
for i in range (0, len(code[3])) :
    dico_benef_titre[code[3][i]] = libelle[3][i]
        
dico_benef_specialite = {}
for i in range (0, len(code[4])) :
    dico_benef_specialite[code[4][i]] = libelle[4][i]

dico_benef_ident_type = {}
for i in range (0, len(code[5])) :
    dico_benef_ident_type[code[5][i]] = libelle[5][i]
    
dico_dico_avantage = {"dico_benef_categ": dico_benef_categ, 
                       "dico_benef_qualite": dico_benef_qualite, 
                       "dico_benef_pays" : dico_benef_pays, 
                       "dico_benef_titre" : dico_benef_titre,
                       "dico_benef_specialite" : dico_benef_specialite, 
                       "dico_benef_ident_type" : dico_benef_ident_type}

#nom_table = 'avantage' | 'remuneration' | 'convention'
def save_dico(dico_de_dico, nom_table) :
    for key, value in dico_de_dico.items():
        
        with open('./dico_{}/{}.json'.format(nom_table, key), 'w') as f:
            json.dump(value, f, indent=4)

save_dico(dico_dico_avantage, 'avantage')
"""


"""---------------------------------------------------------------"""

"""---------------------------------------------------------------"""
# INFO TABLE CONVENTION
"""
for col in declaration_convention.columns :
    print(col + " : "+str(len(list(declaration_convention[col].unique()))))
"""
"""---------------------------------------------------------------"""


"""---------------------------------------------------------------"""
# INFO TABLE REMUNERATION
"""
for col in declaration_remuneration.columns :
    print(col + " : "+str(len(list(declaration_remuneration[col].unique()))))
"""
"""---------------------------------------------------------------"""

"""---------------------------------------------------------------"""
# INFO TABLE ENTREPRISE
"""
for col in entreprise.columns :
    print(col + " : "+str(len(list(entreprise[col].unique()))))
"""
"""---------------------------------------------------------------"""



# graph repatition des entreprises par secteurs
secteur_entreprise = pd.value_counts(entreprise['secteur'])
labels = []
values = []

for key, value in secteur_entreprise.items() :
    labels.append(key)
    values.append(value)

fig1 = go.Figure(data=[go.Pie(labels=labels, values=values)])
plot(fig1, auto_open=True)



# proportion des objet de convention :

labels = []
values = []
objet_convention = pd.value_counts(declaration_convention['conv_objet'])
count = 0

for key, value in objet_convention.items() :
    if value >= 89404 :
        labels.append(key)
        values.append(value)
        
    else :
        count += value

labels.append("categories restantes aggrégées (< 1.5%)")
values.append(count)
  
fig2 = go.Figure(data=[go.Pie(labels=labels, values=values)])
plot(fig2, auto_open=True)


# repartition de la distribution d'argent
montant_total_avantage = sum(declaration_avantage['avant_montant_ttc'])
montant_total_remuneration = sum(declaration_remuneration['remu_montant_ttc'])
tab_montant_convention = []

for elt in declaration_convention['conv_montant_ttc'] :
    try :
        elt = int(elt)
        tab_montant_convention.append(elt)
    except : 
       break
montant_total_convention = sum(tab_montant_convention)



fig3 = go.Figure(data=[go.Pie(labels=["avantage : 1.626.196.578", "remuneration : 2.418.180.749", 'convention : 3.963.333.090'], values=[montant_total_avantage, montant_total_remuneration, montant_total_convention])])
plot(fig3, auto_open=True)

# repartition temporel de la distribution d'argent dans convention :

""" pas le temps """








# repartition temporel de la distribution d'argent dans remuneration :

tab_remu_par_date = declaration_remuneration[['remu_date', 'remu_montant_ttc']]

tab_remu_par_date['remu_date'][0][-4:]

"""
tab_remu_par_date['année'] = tab_remu_par_date.loc[col_indexer = 'remu_date'][-4:]
tab_remu_par_date.head()
"""

col = tab_remu_par_date.apply(lambda row : (row["remu_date"][-4:]), axis = 1) 
print(len(col))
print(len(tab_remu_par_date))


for key, value in col.items() :
    if int(value) < 2012 :
        col[key] = "saisie abérante"


print(len(col))
print(len(tab_remu_par_date))

tab_remu_par_date.iloc("année") = col
tab_remu_par_date.head()

df_gb_annee_tab_remu_par_date = tab_remu_par_date.groupby('année')

df_sum_remuneration = df_gb_annee_tab_remu_par_date.sum()


# repartition temporel de la distribution d'argent dans avantage :

tab_avantage_par_date = declaration_avantage[['avant_date_signature', 'avant_montant_ttc']]


col = tab_avantage_par_date.apply(lambda row : (row["avant_date_signature"][-4:]), axis = 1) 
print(len(col))
print(len(tab_avantage_par_date))


for key, value in col.items() :
    if int(value) < 2012 :
        col[key] = "saisie abérante"

print(len(col))
print(len(tab_avantage_par_date))

tab_avantage_par_date["année"] = col

tab_avantage_par_date.tail()

df_gb_annee_tab_avantage_par_date = tab_avantage_par_date.groupby('année')

df_sum_avantage = df_gb_annee_tab_avantage_par_date.sum()



# creation du graph en bar en somme de montant :
date_obj = df_gb_annee_tab_remu_par_date.nunique().index
date = []
for elt in date_obj :
    print(elt)
    date.append(elt)
    


fig4 = go.Figure(data=[
    go.Bar(name='rémunertation', x=date, y=df_sum_remuneration['remu_montant_ttc']),
    go.Bar(name='avantage', x=date, y=df_sum_avantage['avant_montant_ttc'])
])
# Change the bar mode
fig4.update_layout(barmode='stack')
plot(fig4, auto_open=True)

# creation du graph en moustache de la moyenne :
df_avg_remuneration = df_gb_annee_tab_remu_par_date.mean()
df_avg_remuneration["année"] = date
df_avg_avantage = df_gb_annee_tab_avantage_par_date.mean()
df_avg_avantage["année"] = date


df = px.data.tips()
fig5 = px.box(tab_remu_par_date, y="remu_montant_ttc")


plot(fig5, auto_open=True)

#######################################################################################################
#######################################################################################################
#                                           COLOMBE                                                   #
#######################################################################################################
#######################################################################################################




#avantage.info() # affiche les informations de la table avantage
##print("les donnaées statistiques de la base avantage")
#avantage.describe().round(2)# affichage des donnees statistiques de la table avantage avec 2 chiffres en arrondi
categorie_benef_avantage = declaration_avantage.groupby('categorie')["entreprise_identifiant"].count() #compte les données selon la qualite des beneficiaires
#print("Le nombre par categorie des beneficiaires est")
#print(categorie_benef_avantage) # Affichage des valeurs par categorie
df_avant_plus = pd.DataFrame(categorie_benef_avantage)
#print(df_avant_plus) # Affichage du dataframe
df_avant_plusR = df_avant_plus['entreprise_identifiant'].sort_values()


dicto = {}
dicto = df_avant_plusR
#print("le dict est", dict)
liste1_categ_benef_avant = [] 
liste2_categ_benef_avant = [] 
j = 0
somme = 0

for cle,valeur in dicto.items():
    #print(cle, valeur)
    if valeur > 10000 :
       # print(cat)
        liste2_categ_benef_avant.append(valeur)# recupération des valeurs des catégories
        liste1_categ_benef_avant.append(cle) # recupération des noms des categories
        j = j + 1
    else :
        somme = somme + valeur
        #liste_categ_benef_avant[j] = somme

liste2_categ_benef_avant.append(somme)
liste1_categ_benef_avant.append("Autres")
#Création d'un dataframe qui stocke les données
categ_benef_avant = pd.DataFrame({'categorie':liste1_categ_benef_avant, 'valeur':liste2_categ_benef_avant})

ProfSant_benef_avantage = declaration_avantage.groupby('qualite')["categorie"].count() #compte les données selon la qualite des beneficiaires



declaration_avantage[declaration_avantage['categorie'] == 'Professionnel de santé'].groupby(['qualite'])['categorie'].count() #compte les données selon la qualite des beneficiaires
#print(ProfSant_benef_avantage) 
avantage_pro_sante= declaration_avantage[declaration_avantage['categorie']=='Professionnel de santé']['qualite']
#print(avantage_pro_sante)
ProfSant_benef_avant = pd.DataFrame({'Index':avantage_pro_sante.index.values,'qualite':avantage_pro_sante}) #, 'valeur':liste2_categ_benef_avant})
print(ProfSant_benef_avant)
ProfSant_benef_avantage = ProfSant_benef_avant.groupby(['qualite'])['Index'].count() #compte les données selon la qualite des beneficiaires
print(ProfSant_benef_avantage)

#plot(categ_benef_avant['categorie'],categ_benef_avant['valeur'])
name = categ_benef_avant['categorie']
data = categ_benef_avant['valeur']
plt.pie(data, labels=name, startangle=90, shadow=True)
plt.axis('equal')
plt.show()





#######################################################################################################
#######################################################################################################
#                                           DASHBOARD                                                 #
#######################################################################################################
#######################################################################################################






external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__)

app.layout = html.Div(style = {"fontFamily" : "Roboto"}, children = [
        html.Div([
                

                        html.H1(children='Projet Transparence Santé'),
                        html.Img(src="/assets/index.png", className="simplon"),
                        html.H4(children = 'By Colombe, Vincent, et Nicolas')

            ], className="title"),

    html.Div([
        html.Div([
                html.H3(children = "Nombre d'entreprise par secteurs d'activité", style = { 'textAlign' : 'center' ,'backgroundColor' : '#ceffab'} ),
                dcc.Graph(
                        id='graph1',
                        figure=  fig1
                        )                
                ], className="six columns", style={'width' : '49%'}),
        html.Div([
                html.H3(children = 'Objet de Convention',style = { 'textAlign' : 'center', 'backgroundColor' : '#ffe8e8'} ),
                dcc.Graph(
                        id='graph2',
                        figure=  fig2
                        )                
                ], className="six columns", style={'width' : '49%'}),
            ], className="row", style = {'display' : 'flex', 'flex-direction': 'row', 'width' : '100%'}),
                
        html.Hr(),
        
        html.Div([
                html.H3(children = "Répartition generale des depenses engagées",  style = { 'backgroundColor' : '#fde8ff'}),
                html.H3(children = "Total = 8 007 710 417‬ milliards d'euros"),
                dcc.Graph(
                        id='graph3',
                        figure=  fig3
                        )                
                ], style={'textAlign' : 'center'}),
                
         html.Hr(),   
         
           html.Div([
                html.H3(children = "Répartition temporelle des depenses engagées", style = { 'backgroundColor' : '#e8f1ff'}),
                dcc.Graph(
                        id='graph4',
                        figure=  fig4
                        )                
                ], style={'textAlign' : 'center'}),

        html.Hr(),      

                
])               


if __name__ == '__main__':
    app.run_server(debug=False)




