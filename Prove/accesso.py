import csv
#nome = richiesta[1],
#psw = richiesta[2],
print(".  ")
with open('log.csv', mode='r', newline='', encoding='utf-8') as file:
    lettore = csv.reader(file, delimiter=',')
    for riga in lettore:
        print(riga=='ciao')

#with open('log.csv', newline='') as csvfile:
#   print("nws")
#  spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#for row in spamreader:
#   print(', '.join(row))
#csvfile.close
