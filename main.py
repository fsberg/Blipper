import json

def write(nyart_dict, filename='lager.json'):
    with open('lager.json', 'w') as json_file:
        json.dump(nyart_dict, json_file, indent=2)

def nytt(x,y):
    ny_art = x
    ny_namn = y
    ny_antal = 1

    with open('lager.json', 'r') as json_file:

        data = json.load(json_file)

        temp = data['lager']

        nyart_dict = {artikel:{ 
        "artnr": ny_art,
        "artnamn": ny_namn,
        "antal": ny_antal
        }
        }

        temp.append(nyart_dict)
    write(data)    
    print('Ny artikel upplagd')

def inmat():
    skannad_art = input('Skanna artikel: ')
    #debug 
    #print(skannad_art)
    return skannad_art

def open_json():
    with open('lager.json') as f:
        data = json.load(f)
    return data
    #print(data)

def bef(x,y):
    data = open_json()
    temp =[]
    for item in data["lager"],["artikel"]:
        temp.append(item['artnr'])
        

    if x in temp:
        print('Added one to ' + x )



        lager_plus(x)

    else:
        nytt(x,y)
    #print(temp)


def lager_plus(x):

    data = open_json()
    temp = []
    for item in data["lager"]:
       temp = item['rader']["antal"]
       print(item)

       #temp.append(item['artnr'])
    
    print(temp)

    data["antal"] = 2

    print(["antal"])

    write(data)

    #with open("lager.json", "w") as json_file:
     #   json.dump(data, json_file)




input_art = inmat()

ny_namn='nytt namn'
ny_antal=1

bef(input_art,ny_namn)
#nytt(z,d,e)



"""
if kolla om finns i json
    öka antal med 1

else nytt()
    hämta artnamn ur lista och skriv artnr artnama och ntal till json
"""