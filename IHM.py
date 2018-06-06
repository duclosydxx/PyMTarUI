# -*-coding:Latin-1 -*
# On importe Tkinter
from Tkinter import *
from Weather import GetMetar
 

selectAirport=None
monObjetMETAR=None
fenetre=None
textCode=None
textTemp=None
textPression=None
textDate=None


def UpdateIHM(event):
    w = event.widget
    index = int(w.curselection()[0])
    print(textCode.get())

    correponsdingOACIAirport = {
    0:"LFBP",
    1:"LFBZ",
    2:"LFBO",
    3:"LFPO",
    4:"LFBT",
    5:"LFBD"
    }
    monObjetMETAR = GetMetar(correponsdingOACIAirport[index])
    textCode.delete(0, 'end')
    textDate.delete(0, 'end')
    textPression.delete(0, 'end')
    textTemp.delete(0, 'end')
    textCode.insert(0, monObjetMETAR.airportName)
    textDate.insert(0, monObjetMETAR.date)
    textPression.insert(0,monObjetMETAR.pression+" hPa")
    textTemp.insert(0,monObjetMETAR.temperature+" "+u'\xb0'+"C")




fenetre = Tk()
fenetre.geometry("500x500")
Label(fenetre, text="Décodage de bulletin METAR").pack
selectAirport = Listbox(fenetre)

selectAirport.insert(0,"Pau-Pyrénées") #LFBO
selectAirport.insert(1,"Biarritz") #LFBZ
selectAirport.insert(2,"Toulouse-Blagnac") #LFBO
selectAirport.insert(3,"Paris-Orly")   #LFPO
selectAirport.insert(4,"Tarbes") #LFBT
selectAirport.insert(5,"Bordeaux") #LFBD

selectAirport.bind('<<ListboxSelect>>', UpdateIHM)

TitleAirport=Label(fenetre, text="OACI Code")
textCode=Entry()
textCode.insert(END, "N/A")


TitleTemp=Label(fenetre, text="Température")
textTemp=Entry()
textTemp.insert(END, "N/A")

TitlePress=Label(fenetre, text="Pression")
textPression=Entry()
textPression.insert(END, "N/A")

TitleDate=Label(fenetre, text="Date de création")
textDate=Entry()
textDate.insert(END, "N/A")
selectAirport.pack()
TitleAirport.pack()
textCode.pack()
TitleTemp.pack()
textTemp.pack()
TitlePress.pack()
textPression.pack()
TitleDate.pack()
textDate.pack()
fenetre.mainloop()