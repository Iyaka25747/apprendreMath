def captureNumber(question):
    isNotInteger = True
    while isNotInteger:

        userInput = input(question)
        #print("Is string: " + str(isinstance(userInput, str)))
        try:
            val = int(userInput)
            isNotInteger = False
        except ValueError:
            print("Batar, ce n'est pas un chiffre !")
            isNotInteger = True
    return int(userInput)

#captureNumber("Entrer un chiffre: ")
