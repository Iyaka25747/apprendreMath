import json
import random
# print("random :" + str(random.randint(0,20)))

#Récupération des données pour les exercices
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
nbrExercices = len(exercices)
print(str(nbrExercices) + " exercices aux choix")
index = 0
for valeur in exercices:
    print("[" + str(index) + "] Exercices: " + valeur)
    index = index + 1

reponseFausse = True
while reponseFausse:
    noExercice = int(input("Entrer le no de l'exercice: "))
    if noExercice < nbrExercices:
        reponseFausse = False
print("Tu as choisis: " + exercices[noExercice])


# Execution de l'exercice

#Récupération des facteurs de multiplication de l exercice
premierFacteurs = dataExercice[exercices[noExercice]]["premier facteurs"]
deuxiemeFacteurs =  dataExercice[exercices[noExercice]]["deuxieme facteurs"]

#Exercices
indexCalcul = 1
for facteur1 in premierFacteurs:
    for facteur2 in deuxiemeFacteurs:
        print("Combien font: " + str(facteur1)+"x"+str(facteur2)+"=")
        

        reponseFausse = True
        nbrTentatives = 0
        while reponseFausse :
            reponse = int(input("réponse: "))
            nbrTentatives = nbrTentatives + 1
            # vérification de la réponse
            if reponse == facteur1 * facteur2:
                reponseFausse = False
            else:
                reponseFausse = True
        print("Nombre de tentatives: " + str(nbrTentatives))
##########################################################################
exercice = dataExercice[exercices[0]]

# premierL = exercice[0]
# premierL = dataExercice["Multiplication"][0]
# print(premierL)
# premierFacteurList = premierL["list 1er facteur"]
# print(premierFacteurList)
# deuxiemeFacteurList = premierL["list 2eme facteur"]
# print(deuxiemeFacteurList)
premierFacteurList = exercice["list 1er facteur"]
deuxiemeFacteurList = exercice["list 2eme facteur"]
print("1ers facteur :" + str(premierFacteurList) )
print("2emes facteur :" + str(deuxiemeFacteurList) )
for facteur1 in premierFacteurList:
    # print(facteur1)
    for facteur2 in deuxiemeFacteurList:
        print("Multiplication " + str(facteur1) + "*" + str(facteur2) + " : " + str(facteur1 * facteur2))
    
