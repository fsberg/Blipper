import sqlite3
import json
import os

conn = sqlite3.connect("lager.db")

c = conn.cursor()


def del_all():
    c.execute("SELECT rowid, * FROM lager")
    items = c.fetchall()

    for item in items:
        temp = item[0]
        c.execute("DELETE from lager WHERE rowid = (?)", [temp,])
        conn.commit()

def del_one():
    c.execute("SELECT rowid, * FROM lager")
    items = c.fetchall()

    temp = input('number to delete? ')

    c.execute("DELETE from lager WHERE rowid = (?)", [temp,])
    conn.commit()

def exp_json():
    c.execute("SELECT * FROM lager")

    items = c.fetchall()
    
    art=[]
    for item in items:
        temp = {"artnr": item[0], "namn": item[1], "antal":item[2]}
        art.append(temp)
    print(art)

    with open("databas.json", "w",) as json_file:
        json.dump(art, json_file, indent=4)

    print('exported to json')

def see_all():

    os.system('cls' if os.name=='nt' else 'clear')

    c.execute("SELECT rowid, * FROM lager")
    items = c.fetchall()
    for item in items:
        print(item)

def art_minus(artnr,antal):
    c.execute("SELECT rowid, * FROM lager WHERE artikelnummer = (?)",[artnr,] )

    records = c.fetchall()

    for row in records:
        temp = int(row[3])
        temp = temp - antal

    

    c.execute("UPDATE lager SET antal = ? WHERE artikelnummer = (?)", [temp,artnr,]) 
    conn.commit()




#while True:
#    see_all()
#    del_one()


exp_json()
#see_all()
#del_all()
"""
while True:
    see_all()
    artnr = input('Fyll i artikelnr: ')
    antal = int(input('Antal att ta bort: '))
    art_minus(artnr,antal)
"""




conn.close()