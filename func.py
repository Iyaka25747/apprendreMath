import time
import winsound # Son, bruitage 
import os #for terminal screen clearing

# Capture d'un choix qui ne peut qu'un chiffre
def captureNumber(questionText):
    isNotInteger = True
    while isNotInteger:

        userInput = input(questionText)
        #print("Is string: " + str(isinstance(userInput, str)))
        try:
            val = int(userInput)
            isNotInteger = False
        except ValueError:
            print("Batar, ce n'est pas un chiffre !")
            isNotInteger = True
    return int(userInput)

# Selection d'un element valeur parmis une liste de valeur d'une list
def choisirElement(listOfValues):
    # Affichage des valeurs possibles
    position = -1
    for element in listOfValues:
        position = position + 1
        print("[{position}] {value}".format(position=position, value=element))
    #Choix d'une valeur
    choixFaux = True
    while choixFaux:
        capturedNumber = captureNumber("Choix: ")
        # on s assure que c'est un choix possible
        if capturedNumber >= len(listOfValues):
            choixFaux = True
        else:
            choixFaux = False
    chosenValue = listOfValues[capturedNumber]
    #print("Vous avez choisi: " + str(chosenValue))
    return chosenValue


# Fonction pour choisir un exercice dans un dictionnaire dataExercice
def choisirExercice(dataExercice):
    # affichage des exercices possibles    
    index = -1
    print("Liste des exercices:")
    for exercicePossible in dataExercice.keys():
        index = index + 1
        print("[{indexExercice}] Exercices: {exerciceNom}".format(indexExercice = index, exerciceNom = exercicePossible ))
    # Saisie du choix de l'exercice
    reponseFausse = True
    while reponseFausse:
        noExercice = captureNumber("Choix: ")
        if noExercice <= index:
            reponseFausse = False
    # Récupèration du titre de l'exercice
    index = -1
    for exercicePossible in dataExercice.keys():
        index = index + 1
        if noExercice == index:
            nomExerciceChoisi = exercicePossible
    # Affichage du choix
    print("Tu as choisis: " + nomExerciceChoisi)
    return nomExerciceChoisi

def executeMulitplication(listMultiplications, soundActive, badSound, goodSound, currentDate, currentTime, nomJoueur, nomTypeCalculChoisi, nomExerciceChoisi):
    # Récupération des facteurs de multiplication de l exercice
    #facteursCalculs = dataExercices[nomTypeCalculChoisi][nomExerciceChoisi]
    premierFacteurs = listMultiplications["premier facteurs"]
    deuxiemeFacteurs = listMultiplications["deuxieme facteurs"]
    nombreDeCalculs = len(premierFacteurs) * len(deuxiemeFacteurs)
    print("Nombre de calculs à faire: {0}".format(nombreDeCalculs))

    # Exercices
    nombreCalculRestant = nombreDeCalculs
    tempsTotalDepart = time.perf_counter()
    nombreReponsesFaussesTot = 0
    recordsCalculs = []
    indexCalcul = 0
    for facteur1 in premierFacteurs:
        for facteur2 in deuxiemeFacteurs:
            reponseFausse = True
            nbrTentatives = 0
            tempsDepartCalcul = time.perf_counter()
            recordCalcul = {}
            while reponseFausse:
                reponse = captureNumber("[{countDown} calculs restant] Entrer le résultat de {facteur1}x{facteur2}: ".format(
                    countDown=nombreCalculRestant, facteur1=facteur1, facteur2=facteur2))
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
            calcul = "{facteur1}x{facteur2}".format(
                facteur1=facteur1, facteur2=facteur2)
            tempsFinCalcul = time.perf_counter()
            dureeCalcul = round(tempsFinCalcul - tempsDepartCalcul, 1)
            print("Nombre de tentatives: " + str(nbrTentatives))

            # enregistrement du resultat
            recordLine = [currentDate, currentTime , nomJoueur, nomTypeCalculChoisi, nomExerciceChoisi, calcul, nbrTentatives, dureeCalcul]
            if nbrTentatives > 1:
                #calculsRecords.append(recordCalcul) # ajout à la liste
                recordsCalculs.append(recordLine)
            nombreReponsesFaussesTot = nombreReponsesFaussesTot + (nbrTentatives-1)
        
    #Statistiques globales
    tempsTotalFin = time.perf_counter()
    dureeExercice = round(tempsTotalFin - tempsTotalDepart, 1)
    print("temps passé: {tempsExercice} secondes, Nombre de réponses fausses: {totalReponseFaux}".format(tempsExercice = dureeExercice,totalReponseFaux = nombreReponsesFaussesTot))
    return recordsCalculs