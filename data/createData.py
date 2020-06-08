import time
import random

while True:
    timeVal = time.time()
    yVal = random.random()

    with open('data.csv', 'a') as dataFile:
        dataFile.write(f"{timeVal};{yVal}\n")

    time.sleep(1)
