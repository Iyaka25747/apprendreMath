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

# Selection du jouer qui fera l'exercice
def selectionJoueur(dataSettings):
    # Affichage et selection du joueur
    print("Joueurs: ")
    users = dataSettings["users"]
    for user in users:
        print("[{index}] {user}".format(index=users.index(user), user=user))
    choixFaux = True
    while choixFaux:
        joueurNo = captureNumber("Choix du joueur: ")
        if joueurNo > len(users):
            choixFaux = True
        else:
            choixFaux = False
    nomJoueur = users[joueurNo]
    print("Vous avez choisi: " + str(nomJoueur))
    return nomJoueur

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
        if noExercice < index:
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
