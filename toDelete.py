#elapsed time
import time


start = time.perf_counter()
print("hello" + str(start))
end = time.perf_counter()
elapsed = end - start
print(elapsed)

import winsound
goodSound = "good.wav"
winsound.PlaySound("bad.wav", winsound.SND_FILENAME)
winsound.PlaySound(goodSound, winsound.SND_FILENAME)

import json
with open("test.json", 'a') as f:
    f.write(json.dumps("Hello*", indent=4))

import csv

row = ['4', ' Danny', ' New York']

with open('test.csv', 'a') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(row)

csvFile.close()