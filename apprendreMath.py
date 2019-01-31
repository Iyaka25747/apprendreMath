#try csv log 1
import json
import random
import time #for measuring elapsed time, date
from func import *
import os #for terminal screen clearing
import winsound # Son, bruitage 
import datetime #for date
import time
import csv #for statiristics logs


#Initialization des sons
#badSound = "bad.waw"
soundActive = False
badSound = "Batar.wav"
goodSound = "good.wav"
#initialisation du fichier de statistiques
recordFile = "records.csv"
maintenant = datetime.datetime.today()
currentDate = "{year}-{month}-{day}".format(year = maintenant.year, month=  maintenant.month, day=  maintenant.day)#datetime.date.today()
currentTime = "{hour}:{minute}:{second}".format(hour = maintenant.hour, minute=  maintenant.minute, second=  maintenant.second)
print("Date: {0}, Time:{1}".format(currentDate, currentTime))
exerciceRecord = []
# Enregistrement des calculs "Date","Joueur", "Nom du test", "Calcul", "nbr. Tentatives", "Duree"
calculsRecords = [] # enregistrement des calculs faux pour les statistiques
print("Date: " + str(currentDate))
# print("random :" + str(random.randint(0,20)))
# Récupération des paramètres généraux
with open("settings.json", "r") as file:
    dataSettings = json.load(file)

# Affichage et selection du joueur
print("Joueurs: ")
users = dataSettings["users"]
for user in users:
    print("[{index}] {user}".format(index = users.index(user), user = user )) 
choixFaux = True
while choixFaux:
    joueurNo = captureNumber("Choix du joueur: ")
    if joueurNo > len(users):
        choixFaux = True
    else:
        choixFaux = False
nomJoueur = users[joueurNo]
print("Vous avez choisi: " + str(nomJoueur))

# Récupération des données pour les exercices
with open('exercices.json', 'r') as file:
    dataExercice = json.load(file)
    # print(json.dumps(dataExercice, indent=4))
    # a= type(dataExercice)
    # print(a)

# Récupération des exerices dans la liste titresExercices
exercices = []
for valeur in dataExercice.keys():
    exercices.append(valeur)
    # print("Exercices: " + str(titresExercices))

# Affichage des exercices et selection

# affichage des exercices
nbrExercices = len(exercices)
print(str(nbrExercices) + " exercices aux choix")
index = 0
for valeur in exercices:
    print("[" + str(index) + "] Exercices: " + valeur)
    index = index + 1

# Saisie du choix
reponseFausse = True
while reponseFausse:
    noExercice = captureNumber("Choix: ")
    if noExercice < nbrExercices:
        reponseFausse = False
print("Tu as choisis: " + exercices[noExercice])
nomExerciceChoisi = exercices[noExercice]

##########################
# Execution de l'exercice#
##########################

# Récupération des facteurs de multiplication de l exercice
premierFacteurs = dataExercice[exercices[noExercice]]["premier facteurs"]
deuxiemeFacteurs = dataExercice[exercices[noExercice]]["deuxieme facteurs"]
nombreDeCalculs = len(premierFacteurs) * len(deuxiemeFacteurs)
#print("Nombre de calculs à faire: {0}".format(nombreDeCalculs))

#Clear terminal screen
os.system('cls' if os.name == 'nt' else 'clear')

# Exercices
nombreCalculRestant = nombreDeCalculs
tempsTotalDepart = time.perf_counter()
nombreReponsesFaussesTot = 0
indexCalcul = 0
for facteur1 in premierFacteurs:
    for facteur2 in deuxiemeFacteurs:
        #print("Entrer le résultat: " + str(facteur1)+"x"+str(facteur2)+"=")
        #print("Entrer le résultat:
        #{facteur1}x{facteur2}".format(facteur1=facteur1,facteur2=facteur2))        
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
        
        #recordCalcul = '+'.join(str(e) for e in list1) 
        #recordCalcul = {"Calcul": calcul, "Nombre de tentatives": str(nbrTentatives), "Duree": str(dureeCalcul) }
        if nbrTentatives > 1:
            #calculsRecords.append(recordCalcul) # ajout à la liste
            calculsRecords.append(list1)
        nombreReponsesFaussesTot = nombreReponsesFaussesTot + (nbrTentatives-1)
        #print("Nombre tentative: {nbrTent} et nombre total: {nbrTot}".format(nbrTent = nbrTentatives-1, nbrTot = nombreReponsesFaussesTot))
    

#Statistiques globales
tempsTotalFin = time.perf_counter()
dureeExercice = tempsTotalFin - tempsTotalDepart

#Enregistrement des 0statistiques
myFile = open(recordFile, 'a')
with myFile:
    writer = csv.writer(myFile, delimiter=',', lineterminator='\n')
    writer.writerows(calculsRecords)
myFile.close()

print("Ouf.... c'est fini, temps passé: {tempsExercice}, Nombre de réponses fausses: {totalReponseFaux}".format(tempsExercice = dureeExercice,totalReponseFaux = nombreReponsesFaussesTot))


