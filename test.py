import json
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))


exercicesFile = "exercices.json"
with open(dir_path + '/' + exercicesFile, 'r') as file:
    dataExercices = json.load(file)
    # print('hello')
    inTxt = input('hello')
    file.close()
