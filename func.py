def captureNumber():
    isNotInteger = True
    while isNotInteger: 
            
        userInput = input("réponse: ")
        print("Is string: " + str(isinstance(userInput, str)))
        try:
             val = int(userInput)
        except ValueError:
             print("That's not an int!")

             
        if isinstance(userInput, str):
            userInput = int(userInput)
            isNotInteger = False
    return int(userInput)

captureNumber()