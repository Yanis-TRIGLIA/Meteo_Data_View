#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 15:42:08 2022

@author: t21204574
"""


import pandas
"""
Utlilsation de la bibliotheque Panda
"""
Meteo = pandas.read_csv("/amuhome/t21204574/SAE 2.04/sql.csv");
"""
Importation de la base de donnée Meteo au format csv
"""
import numpy as np 

#%%
"""
Analyse 1
Ci dessous et representer les temperature enregistrée de la ville de Marseille qui sont superieur a 25°. 
"""
Marseille  = Meteo.loc[(Meteo["NOML"] == "Marseille") & (Meteo["NOMM"] == "Temperature") & (Meteo["MESURE"]>"25°C") ]
print (Marseille.MESURE)


#%%
"""
Analyse 2
A revoir temperature max
"""
temperature = Meteo.loc[(Meteo["NOMM"] == "Temperature") & (Meteo["DATEDEB"] > "2021-01-01") & (Meteo["DATEFIN"] <"2021-12-31") & (Meteo["NOML"] =="PACA")]
print(temperature["MESURE"].describe())

#%%
"""
Analyse 3
Ci dessous et representer les statistique (compteur,frequence,taux d'apparition les plus elevée) 
pour toutes les categories meteorologique concernant la ville de Renne. 
"""

Rennes  = Meteo.loc[Meteo["NOML"] == "Rennes"]
print(Rennes["CATEGORIE"].describe())

#%%
"""
Analyse 4
Analyse des crue sur l'ensemble de l'année 2021 a l'echelle de la France
"""
Crue  = Meteo.loc[(Meteo["CATEGORIE"] == "Crue") & (Meteo["DATEREL"] > "2021-01-01") & (Meteo["DATEREL"] >"2021-12-31")]
print(Crue["NOML"].describe())

#%%
"""
Analyse 5
A revoir nombre de station par lieu
"""
Paca = Meteo.loc[Meteo["NOML"] == "Occitanie"]
donnees = Paca.groupby("NOML")["IDS"].count()
print(donnees)

#%%
"""
Analyse 6
Ci dessous et presenter une analyse Meteorologique de la region Paca sur l'ensemble de la Base de donnée 
et representer sous forme d'un diagramme circulaire
avec bien evidement l'importation de la bibliotheque pyplot necessaire au tracer du diagramme'
"""
import matplotlib.pyplot as plt

Paca = Meteo.loc[Meteo["NOML"] == "Marseille"]
donnees = Paca.groupby("CATEGORIE")["CATEGORIE"].count()
print(donnees)

donnees.plot.pie(autopct = lambda z: str(round(z, 2)) + '%', pctdistance = 0.6)
plt.show()

#%%
"""
Analyse 7
Nombre de relevée effectuée dans la region Occitanie
"""
Paca = Meteo.loc[Meteo["NOML"] == "Occitanie"]
donnees = Paca["IDR"].count()
print(donnees)

#%%
"""
Analyse 8
Revoir comment afficher les degres sur le diagramme en boite (car valeur non numérique)
"""


#%%
"""
Analyse 9
"""
print("Affichage des données pour chaque lieu :")
data = Meteo.groupby("NOML")[["TEL", "NOMM", "MESURE"]]
print(data.describe())
#%%    
"""
Analyse 10
"""   
print("Proportion des conditions météorologique dans l'hexagone :")
cat = Meteo.groupby("CATEGORIE")["CATEGORIE"].count()
print(cat)
cat.plot.pie(autopct = lambda z: str(round(z, 2)) + '%', pctdistance = 0.6)
plt.show()

#%%    
"""
Analyse 11
"""
print("Difference de température (min/max) :")

temp = Meteo.loc[(Meteo["NOMM"] == "Temperature") & (Meteo["NOML"] == "Marseille")]
c = ['Temperature']
tmpMax = [temp.MESURE.max()]
tmpMin = [temp.MESURE.min()]
print("Temperature max",tmpMax)
print("Temperature min",tmpMin)
plt.bar(c,tmpMax,align='center')
plt.bar(c,tmpMin,color='red',width=0.5)
plt.show()   

#%%    
"""
Analyse 12
Diagramme en boites des niveaux
"""
Meteo["NIVEAU"].plot.box(whis=[0,100],vert=False)
plt.title("Diagramme en boite des niveaux d'alerte")
plt.show()

#%%    
"""
Analyse 13
Analyse des differentes mesures prélevées en france 
"""

tmp = Meteo.groupby("NOMM")["MESURE"].describe()
tmp.plot.bar(width=0.5,edgecolor='black')
plt.title("Mesure dans l'Hexagone")
plt.show()
    
#%%    
"""
Analyse 14

"""
crue = Meteo.loc[Meteo["NOMM"] == "Pluie"]
crue["MESURE"].plot.box(whis=[0,100],vert=False)
plt.title("Diagramme en boite du niveau de pluie")
plt.show()
print(" ")
    
sun = Meteo.loc[Meteo["NOMM"] == "Soleil"]
sun["MESURE"].plot.box(whis=[0,100],vert=False)
plt.title("Diagramme en boite du niveau d'Ensoleillement")
plt.show()
print(" ")
    
cel = Meteo.loc[Meteo["NOMM"] == "Temperature"]
cel["MESURE"].plot.box(whis=[0,100],vert=False)
plt.title("Diagramme en boite de la temperature")
plt.show()
print(" ")

#%%
"""
Analyse 15

"""

print("Mesure de printemps")
spring = Meteo.loc[(Meteo["DATEDEB"] > "2021-08-18") & (Meteo["DATEFIN"] < "2021-10-21")]
donnees1 = spring.groupby("NOML")[["NOMM","MESURE"]]
print(donnees1.describe())
print("||||")
print("||||")
print("Mesure de été")
summer = Meteo.loc[(Meteo["DATEDEB"] >= "2021-06-21") & (Meteo["DATEFIN"] <= "2021-09-21")]
donnees2 = summer.groupby("NOML")[["NOMM", "MESURE"]]
print(donnees2.describe())
print("||||")
print("||||")
print("Mesure de automne")
fall = Meteo.loc[(Meteo["DATEDEB"] >= "2021-09-21") & (Meteo["DATEFIN"] <= "2021-12-21")]
donnees3 = fall.groupby("NOML")[["NOMM", "MESURE"]]
print(donnees3.describe())
print("||||")
print("||||")
print("Mesure de hiver")
winter = Meteo.loc[(Meteo["DATEDEB"] >= "2021-12-21") & (Meteo["DATEFIN"] <= "2021-03-20")]
donnees4 = winter.groupby("NOML")[["NOMM", "MESURE"]]
print(donnees4.describe())
 
#%%   
"""
Analyse 16

"""
