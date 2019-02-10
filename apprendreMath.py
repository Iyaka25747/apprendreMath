# Under dev

import json
import random
import time #for measuring elapsed time, date
from func import *
import os #for terminal screen clearing
import winsound # Son, bruitage 
import datetime #for date
import time
import csv #for statiristics logs

###############
# Initialisation
################

# Récupération des paramètres généraux
class SettingGlobal(object):
    """Global class to hold the settings"""
globalSettings = SettingGlobal()

with open("settings.json", "r") as file:
    dataSettings = json.load(file)
    file.close()

# Initialization des sons
soudSetting = dataSettings["son"]
if soudSetting["active"] == "on":
    globalSettings.soundActive = True
elif soudSetting["active"] == "off":
    globalSettings.soundActive = False
else:
    print("ERROR in setting parameter for -son- key")
    enterKey = input("press a key to continue")
globalSettings.badSound = soudSetting["bad_sound"]
globalSettings.goodSound = soudSetting["good_sound"]

random = dataSettings["random"]

# initialisation du temps
maintenant = datetime.datetime.today()
globalSettings.currentDate = "{day}.{month}.{year}".format(year = maintenant.year, month=  maintenant.month, day=  maintenant.day)#datetime.date.today()
globalSettings.currentTime = "{hour}:{minute}:{second}".format(hour = maintenant.hour, minute=  maintenant.minute, second=  maintenant.second)
print("Date: {0}, Time:{1}".format(globalSettings.currentDate, globalSettings.currentTime))

#Fichier source exercices
exercicesFile = 'exercices.json'
with open(exercicesFile, 'r') as file:
    dataExercices = json.load(file)
    file.close()

#initialisation du fichier de statistiques
recordFile = "records.csv"
exerciceRecord = [] # Enregistrement d'un calculs "Date", "Time", "Joueur", "Nom du test", "Calcul", "nbr. Tentatives", "Duree"
recordsCalculs = [] # enregistrement des calculs faux pour les statistiques

# Affichage et selection du joueur
print("Joueurs: ")
users = dataSettings["users"]
nomJoueur = choisirElement(users)

# Affichage et selection de la categorie multiplication, addition, division...
listElement = list(dataExercices.keys())
nomTypeCalculChoisi = choisirElement(listElement)

# Affichage et selection de l exercice
# recuperation de la liste des exercices
listElement = list(dataExercices[nomTypeCalculChoisi].keys())
nomExerciceChoisi = choisirElement(listElement)

# Choix du mode d exercice trouver le résultat Multiplication ou d une Division
listElement = ["Multiplication", "Division"]
print("Que veux tu exercer ?")
modeExerciceChoisi = choisirElement(listElement)


###########################
# Execution de l'exercice #
###########################

#Clear terminal screen
os.system('cls' if os.name == 'nt' else 'clear')
if nomTypeCalculChoisi == "Multiplication-Division":
    if modeExerciceChoisi == "Multiplication":
        resultatsCalculs = executeMulitplication(dataExercices[nomTypeCalculChoisi][nomExerciceChoisi], random, globalSettings, nomJoueur, nomTypeCalculChoisi, nomExerciceChoisi,modeExerciceChoisi)
    else:
        resultatsCalculs = executeDivision(dataExercices[nomTypeCalculChoisi][nomExerciceChoisi],random, globalSettings, nomJoueur, nomTypeCalculChoisi, nomExerciceChoisi,modeExerciceChoisi)
else:
    print("... en construction...")

#Enregistrement des résultats
myFile = open(recordFile, 'a')
print("Enregistrement des calculs dans {fichier}".format(fichier = recordFile ))
with myFile:
    writer = csv.writer(myFile, delimiter=',', lineterminator='\n')
    writer.writerows(resultatsCalculs)
print("Fin de l'enregistrement")
myFile.close()

print("\nOuf.... c'est fini ...\n")

fin = input("Terminé, press une touche...")
