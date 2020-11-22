napis = "122222122345678"
dl = len( napis )
niemalejacy = True
for i in range(0, dl-1):
    if napis[i] > napis[i+1]:
        niemalejacy = False
        break
print( niemalejacy )

liczby1 = "C:\\Users\\tristan\\Documents\\materialy_szkolne\\matura\\2015-zbior_zadan\\dane\\62\\liczby1.txt"
liczby2 = "C:\\Users\\tristan\\Documents\\materialy_szkolne\\matura\\2015-zbior_zadan\\dane\\62\\liczby2.txt"

plik1 = open( liczby1 )
maks = 0
mini = 0o7777777
print( min )

for linijka in plik1:
    liczba = int(linijka)
    if liczba > maks:
        maks = liczba
    if liczba < mini:
        mini = liczba

print( maks, " ", mini )