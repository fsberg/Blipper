import sqlite3
import json
import os

conn = sqlite3.connect("lager.db")

c = conn.cursor()

#skapar table
def create_table():
    c.execute("""CREATE TABLE lager (artikelnummer,artikelnamn,antal)""")

    conn.commit()


#läs in nya artiklar
def insert_data(x,y,z):
    c.execute("INSERT INTO lager VALUES (?,?,?)", (x,y,z))

    conn.commit()


#Kollar upp artikelnamnet
def check_artname(artnr):
    with open('lager.json') as f:
        data = json.load(f)

    temp =[]

    for item in data['artikel']:        
        if str(artnr) in item.get('artnr'):
            art_namn = item['artnamn']
            return art_namn


#visar allt
def sel_all():
    items = c.execute("SELECT rowid, * FROM lager")
    for item in items:
        print(item)


#updaterar antal
def update_antal(artnr):
    c.execute("SELECT rowid, * FROM lager WHERE artikelnummer = (?)",[artnr,] )

    records = c.fetchall()

    for row in records:
        temp = int(row[3])
        temp = temp + 1

    

    c.execute("UPDATE lager SET antal = ? WHERE artikelnummer = (?)", [temp,artnr,]) 
    conn.commit() 

def scanner():

    inp = input('Input: ')
    inp = inp.upper()
    os.system('cls' if os.name=='nt' else 'clear')
    return inp

def check_db(artnr):
    c.execute("SELECT rowid, * FROM lager WHERE artikelnummer = (?)",[artnr,] )

    records = c.fetchall()

    for row in records:
        temp = row[1]
        return temp


while True:
    z = 1



    scan_art = scanner()

    ret_artnamn = check_artname(scan_art)

    ret_artnum = check_db(scan_art)


    if scan_art == ret_artnum:
        print('update')
        print(scan_art)
        update_antal(scan_art)

    
    else:
        print('Added 1 to ' + scan_art)
        insert_data(scan_art,ret_artnamn,z)

    

    sel_all()
    
conn.close()
