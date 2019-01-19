import json
import random
# print("random :" + str(random.randint(0,20)))

with open('parameters.json', 'r') as f:
    parameters = json.load(f)
# print(json.dumps(parameters, indent=4))
# a= type(parameters)
# print(a)
exercice = parameters["Multiplication"]
print(exercice)
# premierL = exercice[0]
# premierL = parameters["Multiplication"][0]
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
    
noExercice = input("Entrer le no de l'exercice: ")
print(noExercice)