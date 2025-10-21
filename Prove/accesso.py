import csv
nome = "ciao"
psw = "bello"
with open('log.csv', mode='r', newline='', encoding='utf-8') as file:
    lettore = csv.reader(file, delimiter=',')
    for riga in lettore:
        print(riga)
        if riga[0]==nome and riga[1]==psw :
            print("coretto")
            break
        else:
         print("password o nome incoretti"),

