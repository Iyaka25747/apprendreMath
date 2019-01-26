
import json
import random
import time #for measuring elapsed time
from func import *
import os #for terminal screen clearing
import winsound # Son, bruitage 


# print("random :" + str(random.randint(0,20)))

# Récupération des données pour les exercices
with open('data.json', 'r') as file:
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
indexCalcul = nombreDeCalculs
tempsDepart = time.perf_counter()
nombreReponsesFaussesTot = 0
for facteur1 in premierFacteurs:
    for facteur2 in deuxiemeFacteurs:
 #       print("Entrer le résultat: " + str(facteur1)+"x"+str(facteur2)+"=")
  #      print("Entrer le résultat: {facteur1}x{facteur2}".format(facteur1=facteur1,facteur2=facteur2))        
        reponseFausse = True
        nbrTentatives = 0
        while reponseFausse :
            reponse = captureNumber("[{countDown} calculs restant] Entrer le résultat de {facteur1}x{facteur2}: ".format(countDown=indexCalcul,facteur1=facteur1,facteur2=facteur2))
            nbrTentatives = nbrTentatives + 1
            # vérification de la réponse
            if reponse == facteur1 * facteur2:
                reponseFausse = False
                winsound.PlaySound('good.wav', winsound.SND_FILENAME)
            else:
                reponseFausse = True
                winsound.PlaySound('bad.wav', winsound.SND_FILENAME)
                # print("Peux faire mieux ...")
        indexCalcul = indexCalcul - 1
        print("Nombre de tentatives: " + str(nbrTentatives))
        nombreReponsesFaussesTot = nombreReponsesFaussesTot + (nbrTentatives-1)
        #print("Nombre tentative: {nbrTent} et nombre total: {nbrTot}".format(nbrTent = nbrTentatives-1, nbrTot = nombreReponsesFaussesTot))
#Enregistrement des statistiques
tempsFin = time.perf_counter()
dureeExercice = tempsFin - tempsDepart

print("Ouf.... c'est fini, temps passé: {tempsExercice}, Nombre de réponses fausses: {totalReponseFaux}".format(tempsExercice = dureeExercice,totalReponseFaux = nombreReponsesFaussesTot))


