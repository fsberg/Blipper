import json
import sqlite3

conn = sqlite3.connect("lager.db")
c = conn.cursor()

def check_artname(artnr):
    with open('lager.json') as f1:
        lager = json.load(f1)

    temp =[]

    for item in lager['artikel']:        
        if str(artnr) in str(item.get('artnr')):
            art_namn = item['artnamn']
            return art_namn

def update_namn(artnr,artnamn):

    c.execute("SELECT rowid, * FROM lager WHERE artikelnummer = (?)",[artnr,] )

    records = c.fetchall()

    for row in records:
        temp = row[2]
        temp = artnamn
        #print(temp)
        

        c.execute("UPDATE lager SET artikelnamn = ? WHERE artikelnummer = (?)", [temp,artnr,]) 

    conn.commit()
    #print('ooooo')

def update_nr(artnr_old,artnr):
    c.execute("SELECT rowid, * FROM lager WHERE artikelnummer = (?)",[artnr_old,] )
    #print(artnr)
    #print(artnr_old)

    records = c.fetchall()

    for row in records:
        temp = row[1]
        temp = artnr
        #print(temp)
        

        c.execute("UPDATE lager SET artikelnummer = ? WHERE artikelnummer = (?)", [temp,artnr_old,]) 

        #print(temp)
        conn.commit()

def see_all():

    c.execute("SELECT rowid, * FROM lager")
    items = c.fetchall()
    for item in items:
        print(item)

with open('databas.json') as f1:
     jsondb = json.load(f1)

#print(jsondb)
for i in jsondb:
    #print(i)
    art_nr = i['artnr']
    #print(art_nr)

    ret_artnamn = str(check_artname(art_nr))

    art_nr_old = art_nr

    #print(ret_artnamn)
    d_char ='DD'
    m_char ='MM'
    b_char ='BB'
    g_char ='GG'
    a_char ='\u00c0'

    if d_char in art_nr:
        art_nr = art_nr.replace('DD', 'D')
        #print(art_nr)

    if m_char in art_nr:
        art_nr = art_nr.replace('MM','M')
        #print(art_nr)

    if b_char in art_nr:
        art_nr = art_nr.replace('BB', 'B')
        #print(art_nr)

    if g_char in art_nr:
        art_nr = art_nr.replace('GG', 'G')
        #print(art_nr)

    if a_char in art_nr:
        art_nr = art_nr.replace('\u00c0', 'A')
        #print(art_nr)

    #print(art_nr)
    update_nr(art_nr_old,art_nr)
    update_namn(art_nr,ret_artnamn)