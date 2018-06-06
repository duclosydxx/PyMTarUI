import requests
import datetime
import json

class METAR:
    airportName=""
    temperature=0
    pression=0
    date=""

    def __init__(self, name, temperature, pression, date):
        self.airportName = name
        self.temperature = temperature
        self.pression = pression
        self.date = date



   

def GetMetar(OACI_CODE):
  
    url="http://avwx.rest/api/metar/"+OACI_CODE
    r=requests.get(url)
    tabMETAR = json.loads(r.text)
    d = datetime.date.today()

    # Donnees brutes
    #print(tabMETAR)
    time = tabMETAR["Time"][:2]+"/"+'{:02d}'.format(d.month)+"/"+str(d.year)+"  "+str(int(tabMETAR["Time"][2:4])+2)+"h"+tabMETAR["Time"][4:6]

    # Remplissage de l'objet :
    monMETAR = METAR(tabMETAR["Station"], 
                     tabMETAR["Temperature"],
                     tabMETAR["Altimeter"],
                     time)
    
    return monMETAR