tablica = [0] * 10

import random

for i in range(0, len(tablica)):
    tablica[i] = random.randrange(10,100)

for i in range(0,len(tablica)):
    print(tablica[i], end=", ")

for j in range(0,len(tablica)):
    for i in range(0,len(tablica)-1-j):
        if tablica[i] > tablica[i + 1]:
            rob = tablica[i]
            tablica[i] = tablica[i + 1]
            tablica[i + 1] = rob
print("__________");
for i in range(0,len(tablica)):
    print(tablica[i], end=", ")
	
