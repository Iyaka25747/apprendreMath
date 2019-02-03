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
with open("settings.json", "r") as file:
    dataSettings = json.load(file)
    file.close()

# Initialization des sons
soudSetting = dataSettings["son"]
if soudSetting["active"] == "on":
    soundActive = True
elif soudSetting["active"] == "off":
    soundActive = False
else:
    print("ERROR in setting parameter for -son- key")
    enterKey = input("press a key to continue")
badSound = soudSetting["bad_sound"]
goodSound = soudSetting["good_sound"]


# initialisation du temps
maintenant = datetime.datetime.today()
currentDate = "{day}.{month}.{year}".format(year = maintenant.year, month=  maintenant.month, day=  maintenant.day)#datetime.date.today()
currentTime = "{hour}:{minute}:{second}".format(hour = maintenant.hour, minute=  maintenant.minute, second=  maintenant.second)
print("Date: {0}, Time:{1}".format(currentDate, currentTime))

#Fichier source exercices
exercicesFile = 'exercices.json'

#initialisation du fichier de statistiques
recordFile = "records.csv"
exerciceRecord = [] # Enregistrement d'un calculs "Date", "Time", "Joueur", "Nom du test", "Calcul", "nbr. Tentatives", "Duree"
calculsRecords = [] # enregistrement des calculs faux pour les statistiques

# Affichage et selection du joueur
print("Joueurs: ")
users = dataSettings["users"]
nomJoueur = choisirElement(users)
    
# Affichage et selection de l exercice
with open(exercicesFile, 'r') as file:
    dataExercices = json.load(file)
    file.close()
# recuperation de la liste des exercices
listExercices = []
for exercicePossible in dataExercices.keys():
    listExercices.append(exercicePossible)
#selection d un exercice dans la liste
nomExerciceChoisi = choisirElement(listExercices)


##########################
# Execution de l'exercice#
##########################

# Récupération des facteurs de multiplication de l exercice
facteursCalculs = dataExercices[nomExerciceChoisi]
premierFacteurs = facteursCalculs["premier facteurs"]
deuxiemeFacteurs = facteursCalculs["deuxieme facteurs"]
nombreDeCalculs = len(premierFacteurs) * len(deuxiemeFacteurs)
print("Nombre de calculs à faire: {0}".format(nombreDeCalculs))

#Clear terminal screen
os.system('cls' if os.name == 'nt' else 'clear')

# Exercices
nombreCalculRestant = nombreDeCalculs
tempsTotalDepart = time.perf_counter()
nombreReponsesFaussesTot = 0
indexCalcul = 0
for facteur1 in premierFacteurs:
    for facteur2 in deuxiemeFacteurs:     
        reponseFausse = True
        nbrTentatives = 0
        tempsDepartCalcul = time.perf_counter()
        recordCalcul = {}
        while reponseFausse :
            reponse = captureNumber("[{countDown} calculs restant] Entrer le résultat de {facteur1}x{facteur2}: ".format(countDown=nombreCalculRestant,facteur1=facteur1,facteur2=facteur2))
            nbrTentatives = nbrTentatives + 1
            # vérification de la réponse
            if reponse == facteur1 * facteur2:
                reponseFausse = False
                if soundActive == True:
                    winsound.PlaySound(goodSound, winsound.SND_FILENAME)
            else:
                reponseFausse = True
                if soundActive == True:
                    winsound.PlaySound(badSound, winsound.SND_FILENAME)
                # print("Peux faire mieux ...")
        indexCalcul = indexCalcul + 1
        nombreCalculRestant = nombreCalculRestant - 1
        calcul = "{facteur1}x{facteur2}".format(facteur1=facteur1,facteur2=facteur2)
        tempsFinCalcul = time.perf_counter()
        dureeCalcul = round(tempsFinCalcul - tempsDepartCalcul, 1)
        print("Nombre de tentatives: " + str(nbrTentatives)) 

        # Statistic calcul
        list1 = [currentDate, currentTime , nomJoueur, nomExerciceChoisi, calcul, nbrTentatives, dureeCalcul]
        if nbrTentatives > 1:
            #calculsRecords.append(recordCalcul) # ajout à la liste
            calculsRecords.append(list1)
        nombreReponsesFaussesTot = nombreReponsesFaussesTot + (nbrTentatives-1)
        
#Statistiques globales
tempsTotalFin = time.perf_counter()
dureeExercice = round(tempsTotalFin - tempsTotalDepart, 1)

#Enregistrement des statistiques
myFile = open(recordFile, 'a')
print("Enregistrement des calculs dans {fichier}".format(fichier = recordFile ))
with myFile:
    writer = csv.writer(myFile, delimiter=',', lineterminator='\n')
    writer.writerows(calculsRecords)
print("Fin de l'enregistrement")
myFile.close()

print("\nOuf.... c'est fini ...")
print("temps passé: {tempsExercice} secondes, Nombre de réponses fausses: {totalReponseFaux}".format(tempsExercice = dureeExercice,totalReponseFaux = nombreReponsesFaussesTot))
fin = input("Terminé")
