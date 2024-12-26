#Kniffel: Spieler spielt gegen regelbasierten Bot

import random
import tkinter as tk
from tkinter import messagebox
from collections import Counter

#Kontrolle der Optionen
def is2erPasch(wuerfel):
    count = 1
    for i in range(len(wuerfel)-1):
        zahl = wuerfel[i]
        if wuerfel[i+1]==zahl:
            count = count + 1
        else:
            count= 1
        if count == 2:
            return True
    return False

def get2erPasch(wuerfel):
    # findet alle zahlen, die einen 2er Pasch
    zahlen = []
    for i in range(0,5):
        if wuerfel.count(wuerfel[i]) >=2 :
            zahlen.append(wuerfel[i])
    return zahlen

def is3erPasch(wuerfel):
    count = 1
    for i in range(len(wuerfel)-1):
        zahl = wuerfel[i]
        if wuerfel[i+1]==zahl:
            count = count + 1
        else:
            count= 1
        if count == 3:
            return True
    
    return False

def is4erPasch(wuerfel):
    count = 1
    for i in range(len(wuerfel)-1):
        zahl = wuerfel[i]
        if wuerfel[i+1]==zahl:
            count = count + 1
        else:
            count= 1
        if count == 4:
            return True
    
    return False

def get4erPasch(wuerfel):
    # findet alle zahlen, die einen 4er Pasch
    zahlen = []
    for i in range(0,5):
        if wuerfel.count(wuerfel[i]) >= 4 :
            zahlen.append(wuerfel[i])
    return zahlen

def get3erPasch(wuerfel):
    # findet alle zahlen, die einen 3er Pasch
    zahlen = []
    for i in range(0,5):
        if wuerfel.count(wuerfel[i]) >= 3 :
            zahlen.append(wuerfel[i])
    return zahlen


def isKniffel(wuerfel):
    count = 1
    for i in range(len(wuerfel)-1):
        zahl = wuerfel[i]
        if wuerfel[i+1]==zahl:
            count = count + 1
        else:
            count= 1
        if count == 5:
            return True
    
    return False

def iskleineStraße(wuerfel):
    wuerfel = list(set(wuerfel))
    wuerfel.sort()
    count = 1
    for i in range(len(wuerfel)-1):
        zahl = wuerfel[i]
        if wuerfel[i+1]==zahl+1:
            count = count + 1
        else:
            count = 1
        if count == 4:
            return True
    
    return False

def isgroßeStraße(wuerfel):
    count = 1 
    for i in range(len(wuerfel)-1):
        zahl = wuerfel[i]
        if wuerfel[i+1]==zahl+1:
            count = count + 1
        else:
            count = 1
        if count == 5:
            return True
    return False

def isFullHouse(wuerfel):
    if len(set(wuerfel))==2 and is4erPasch(wuerfel) == False:
        return True
    return False

#alle Optionen in einer Liste
#Spieler
def getOptionen(spielblockspieler, wuerfel):    
    optionen = []
    
    #Text (zahlen) von würfelbuttons
    wuerfel_zahlen=[]
    for i in wuerfel:
        current_num= i.cget("text")
        wuerfel_zahlen.append(int(current_num))
    wuerfel_zahlen.sort()

    
    if 1 in wuerfel_zahlen and spielblockspieler["1"]==0:
        optionen.append("1")
    if 2 in wuerfel_zahlen and spielblockspieler["2"]==0:
        optionen.append("2")
    if 3 in wuerfel_zahlen and spielblockspieler["3"]==0:
        optionen.append("3")
    if 4 in wuerfel_zahlen and spielblockspieler["4"]==0:
        optionen.append("4")
    if 5 in wuerfel_zahlen and spielblockspieler["5"]==0:
        optionen.append("5")
    if 6 in wuerfel_zahlen and spielblockspieler["6"]==0:
        optionen.append("6")
    if is3erPasch(wuerfel_zahlen) and spielblockspieler["3er Pasch"]==0:
        optionen.append("3er Pasch")
    if is4erPasch(wuerfel_zahlen) and spielblockspieler["4er Pasch"]==0:
        optionen.append("4er Pasch")
    if isKniffel(wuerfel_zahlen) and spielblockspieler["Kniffel"]==0:
        optionen.append("Kniffel")
    if iskleineStraße(wuerfel_zahlen) and spielblockspieler["kleine Straße"]==0:
        optionen.append("kleine Straße")
    if isgroßeStraße(wuerfel_zahlen) and spielblockspieler["große Straße"]==0:
        optionen.append("große Straße")
    if isFullHouse(wuerfel_zahlen) and spielblockspieler["Full House"]==0:
        optionen.append("Full House")
    if spielblockspieler["Chance"]==0:
        optionen.append("Chance")
        
    return optionen

def getstreichenOptionen(spielblockspieler, wuerfel):
    #Text (zahlen) von würfelbuttons
    wuerfel_zahlen=[]
    for i in wuerfel:
        current_num= i.cget("text")
        wuerfel_zahlen.append(int(current_num))
    wuerfel_zahlen.sort()
    
    streichen_optionen = []
    
    if spielblockspieler["1"]==0:
        streichen_optionen.append("1")
    if spielblockspieler["2"]==0:
        streichen_optionen.append("2")
    if spielblockspieler["3"]==0:
        streichen_optionen.append("3")
    if spielblockspieler["4"]==0:
        streichen_optionen.append("4")
    if spielblockspieler["5"]==0:
        streichen_optionen.append("5")
    if spielblockspieler["6"]==0:
        streichen_optionen.append("6")
            
            
    if spielblockspieler["3er Pasch"]==0:
        streichen_optionen.append("3er Pasch")
    if spielblockspieler["4er Pasch"]==0:
        streichen_optionen.append("4er Pasch")
    if spielblockspieler["Kniffel"]==0:
        streichen_optionen.append("Kniffel")
    if spielblockspieler["kleine Straße"]==0:
        streichen_optionen.append("kleine Straße")
    if spielblockspieler["große Straße"]==0:
        streichen_optionen.append("große Straße")
    if spielblockspieler["Full House"]==0:
        streichen_optionen.append("Full House")
    if spielblockspieler["Chance"]==0:
        streichen_optionen.append("Chance")
    
    return streichen_optionen

#Bot Optionen
def getOptionenBot(spielblockbot):    
    optionen = []
    
    global botwuerfel
    botwuerfel.sort()
    
    if 1 in botwuerfel and spielblockbot["1"]==0:
        optionen.append("1")
    if 2 in botwuerfel and spielblockbot["2"]==0:
        optionen.append("2")
    if 3 in botwuerfel and spielblockbot["3"]==0:
        optionen.append("3")
    if 4 in botwuerfel and spielblockbot["4"]==0:
        optionen.append("4")
    if 5 in botwuerfel and spielblockbot["5"]==0:
        optionen.append("5")
    if 6 in botwuerfel and spielblockbot["6"]==0:
        optionen.append("6")
    if is3erPasch(botwuerfel) and spielblockbot["3er Pasch"]==0:
        optionen.append("3er Pasch")
    if is4erPasch(botwuerfel) and spielblockbot["4er Pasch"]==0:
        optionen.append("4er Pasch")
    if isKniffel(botwuerfel) and spielblockbot["Kniffel"]==0:
        optionen.append("Kniffel")
    if iskleineStraße(botwuerfel) and spielblockbot["kleine Straße"]==0:
        optionen.append("kleine Straße")
    if isgroßeStraße(botwuerfel) and spielblockbot["große Straße"]==0:
        optionen.append("große Straße")
    if isFullHouse(botwuerfel) and spielblockbot["Full House"]==0:
        optionen.append("Full House")
    if spielblockbot["Chance"]==0:
        optionen.append("Chance")
    return optionen

def getstreichenOptionenBot(spielblockbot):
    streichen_optionen = []
    
    if spielblockbot["1"]==0:
        streichen_optionen.append("1")
    if spielblockbot["2"]==0:
        streichen_optionen.append("2")
    if spielblockbot["3"]==0:
        streichen_optionen.append("3")
    if spielblockbot["4"]==0:
        streichen_optionen.append("4")
    if spielblockbot["5"]==0:
        streichen_optionen.append("5")
    if spielblockbot["6"]==0:
        streichen_optionen.append("6")
              
    if spielblockbot["3er Pasch"]==0:
        streichen_optionen.append("3er Pasch")
    if spielblockbot["4er Pasch"]==0:
        streichen_optionen.append("4er Pasch")
    if spielblockbot["Kniffel"]==0:
        streichen_optionen.append("Kniffel")
    if spielblockbot["kleine Straße"]==0:
        streichen_optionen.append("kleine Straße")
    if spielblockbot["große Straße"]==0:
        streichen_optionen.append("große Straße")
    if spielblockbot["Full House"]==0:
        streichen_optionen.append("Full House")
    if spielblockbot["Chance"]==0:
        streichen_optionen.append("Chance")
    
    return streichen_optionen

#auswahl würfel die nochmal gewürfelt werden sollen
def auswahl_wuerfeln(button):
    current_color = button.cget("bg")
    if current_color == "#fef9e7":
        button.config(bg="#d6eaf8")
    else:
        button.config(bg="#fef9e7")

def spieler_wuerfelt():
    global zug
    if zug<2:
        for button in wuerfel:  
            if button.cget("bg") == "#fef9e7":
                neue_zahl = random.randint(1, 6) 
                button.config(text=str(neue_zahl)) 
        zug = zug+1
    else: 
        messagebox.showinfo("Zug vorbei", "Maximal drei Würfe! Bitte Ergebnis eintragen oder streichen.")
         
#fenster mit optionen
def optionen_zeigen():
    global eintragenroot
    eintragenroot = tk.Toplevel()
    eintragenroot.title("Eintrageoptionen")
    eintragenroot.configure(bg="#d1f2eb")
    optionen = getOptionen(spielblockspieler, wuerfel)
    #wenn es keine optionen gibt
    if not optionen:
        messagebox.showinfo("Fehler", "Du kannst nichts eintragen. Streiche oder würfle erneut.")
        eintragenroot.destroy()
    for option in optionen:
        optionbutton = tk.Button(eintragenroot, text=option, bg = "#d1f2eb", activebackground="#a9dfbf", command= lambda option = option:option_geklickt(option))
        optionbutton.pack()
    
#wenn option angeklickt
def option_geklickt(name):
    buttonname=name 
    
    wuerfel_zahlen=[]
    for i in wuerfel:
        current_num= i.cget("text")
        wuerfel_zahlen.append(int(current_num))
    wuerfel_zahlen.sort()
    
    counter = Counter(wuerfel_zahlen)
    
    global punkte
    if buttonname == "1":
        x = 0
        for i in wuerfel_zahlen:
            if i == 1:
                x=x+1
        spielblockspieler["1"]=x
        punkte = punkte + x
        listboxspieler.delete(1)
        listboxspieler.insert(1, "")
   
    elif buttonname == "2":
        x = 0
        for i in wuerfel_zahlen:
            if i == 2:
                x=x+2
        spielblockspieler["2"]=x
        punkte = punkte + x
        listboxspieler.delete(2)
        listboxspieler.insert(2, "")
    
    elif buttonname == "3":
        x = 0
        for i in wuerfel_zahlen:
            if i == 3:
                x=x+3
        spielblockspieler["3"]=x
        punkte = punkte + x
        listboxspieler.delete(3)
        listboxspieler.insert(3, "")
    
    elif buttonname == "4":
        x = 0
        for i in wuerfel_zahlen:
            if i == 4:
                x=x+4
        spielblockspieler["4"]=x
        punkte = punkte + x
        listboxspieler.delete(4)
        listboxspieler.insert(4, "")
      
    elif buttonname == "5":
        x = 0
        for i in wuerfel_zahlen:
            if i == 5:
                x=x+5
        spielblockspieler["5"]=x
        punkte = punkte + x
        listboxspieler.delete(5)
        listboxspieler.insert(5, "")

    elif buttonname == "6":
        x = 0
        for i in wuerfel_zahlen:
            if i == 6:
                x=x+6
        spielblockspieler["6"]=x
        punkte = punkte + x
        listboxspieler.delete(6)
        listboxspieler.insert(6, "")


    elif buttonname == "3er Pasch":
        x=0
        for zahl, count in counter.items():
            if count == 3:
                x = zahl * 3
        spielblockspieler["3er Pasch"] = x
        punkte = punkte + x
        listboxspieler.delete(7)
        listboxspieler.insert(7, "")
    
    elif buttonname == "4er Pasch":
        x=0
        for zahl, count in counter.items():
            if count == 4:
                x = zahl * 4
        spielblockspieler["4er Pasch"] = x
        punkte = punkte + x
        listboxspieler.delete(8)
        listboxspieler.insert(8, "")


    elif buttonname == "Full House":
        spielblockspieler["Full House"] = 25
        punkte = punkte + 25
        listboxspieler.delete(9)
        listboxspieler.insert(9, "")
    
    elif buttonname == "kleine Straße":
        spielblockspieler["kleine Straße"] = 30
        punkte = punkte + 30
        listboxspieler.delete(10)
        listboxspieler.insert(10, "")
        
    elif buttonname == "große Straße":
        spielblockspieler["große Straße"] = 40
        punkte = punkte + 40
        listboxspieler.delete(11)
        listboxspieler.insert(11, "")
        
    elif buttonname == "Kniffel":
        spielblockspieler["Kniffel"] = 50
        punkte = punkte + 50
        listboxspieler.delete(12)
        listboxspieler.insert(12, "")
        
    elif buttonname == "Chance":
        x=0
        for i in wuerfel_zahlen:
            x = x+i
        spielblockspieler["Chance"] = x
        punkte = punkte + x
        listboxspieler.delete(13)
        listboxspieler.insert(13, "")
        
    #Kniffel Bonus
    summeoben = 0
    for o in spielblockspieler:
        if o == "1" or o =="2" or o =="3"or o =="4"or o =="5"or o =="6" and spielblockspieler[o]!="x":
            summeOben = summeoben + int(spielblockspieler[o])
    
    if int(summeOben) >= 63:
        botpunkte = botpunkte + 35
    if int(summeOben) >= 63:
        punkte = punkte + 35
    
    #punktanzeige aktualisieren
    spielerpunkte.configure(text="Punkte: " +str(punkte))   
    
    print("Spielblock Spieler: "+ str(spielblockspieler))
    eintragenroot.destroy()
    botzug()
    
#fenster mit streichoptionen
def streichen_zeigen():
    global streichenroot
    streichenroot = tk.Toplevel()
    streichenroot.title("Eintrageoptionen")
    streichenroot.configure(bg="#fadbd8")
    streichoptionen = getstreichenOptionen(spielblockspieler, wuerfel)

 
    for s_option in streichoptionen:
        optionbutton = tk.Button(streichenroot, text=s_option, bg = "#fadbd8", activebackground="#f5b7b1",command= lambda s_option = s_option:streichenoption_geklickt(s_option))
        optionbutton.pack()

#wenn streichoption angeklickt
def streichenoption_geklickt(name):
    buttonname=name 
    
    wuerfel_zahlen=[]
    for i in wuerfel:
        current_num= i.cget("text")
        wuerfel_zahlen.append(int(current_num))
    wuerfel_zahlen.sort()
    
    spielblockspieler[buttonname] = "x"
    #bei streichen listbox eintrag löschen
    spielblockspielerlist = list(spielblockspieler.keys())
    listboxspieler.delete(spielblockspielerlist.index(buttonname)+1)
    listboxspieler.insert(spielblockspielerlist.index(buttonname)+1, "")
   
    print("Spielblock Spieler: "+ str(spielblockspieler))
    
    streichenroot.destroy()
    botzug()

#spiel restart
def restart():
    global runde
    runde = 0
    rundenanzeige.config(text="Runde "+ str(runde)+ " von 13")
    
    global punkte
    punkte = 0
    spielerpunkte.config(text = "Punkte: "+ str(punkte))
    
    global botpunkte
    botpunkte = 0
    botpunktelabel.config(text = "Punkte: "+ str(botpunkte))
    
    global spielblockspieler
    global spielblockbot
    
    listboxspieler.insert(1, "1")
    listboxspieler.insert(2, "2")
    listboxspieler.insert(3, "3")
    listboxspieler.insert(4, "4")
    listboxspieler.insert(5, "5")
    listboxspieler.insert(6, "6")
    listboxspieler.insert(7, "3er Pasch")
    listboxspieler.insert(8, "4er Pasch")
    listboxspieler.insert(9, "Full House")
    listboxspieler.insert(10, "kleine Straße")
    listboxspieler.insert(11, "große Straße")
    listboxspieler.insert(12, "Kniffel")
    listboxspieler.insert(13, "Chance")
    
    listboxbot.insert(1, "1")
    listboxbot.insert(2, "2")
    listboxbot.insert(3, "3")
    listboxbot.insert(4, "4")
    listboxbot.insert(5, "5")
    listboxbot.insert(6, "6")
    listboxbot.insert(7, "3er Pasch")
    listboxbot.insert(8, "4er Pasch")
    listboxbot.insert(9, "Full House")
    listboxbot.insert(10, "kleine Straße")
    listboxbot.insert(11, "große Straße")
    listboxbot.insert(12, "Kniffel")
    listboxbot.insert(13, "Chance")
    
    #Startspielblock Spieler
    spielblockspieler = {
             "1": 0,
             "2": 0,
             "3": 0,
             "4": 0,
             "5": 0,
             "6": 0,
             "3er Pasch": 0,
             "4er Pasch": 0,
             "Full House": 0,
             "kleine Straße": 0,
             "große Straße": 0,
             "Kniffel": 0,
             "Chance": 0}

    #Startspielblock Bot
    spielblockbot = {
             "1": 0,
             "2": 0,
             "3": 0,
             "4": 0,
             "5": 0,
             "6": 0,
             "3er Pasch": 0,
             "4er Pasch": 0,
             "Full House": 0,
             "kleine Straße": 0,
             "große Straße": 0,
             "Kniffel": 0,
             "Chance": 0}
 
    spielzug()    

#was bot nochmal würfeln soll
def bot_nochmal(spielblockbot):
    global botwuerfel
    wuerfel = botwuerfel
    optionen = getOptionenBot(spielblockbot)
    
    #4er Pasch versuchen 
    if "3er Pasch" in optionen:
        wuerfel.sort()
        count = 1
        paschzahl=0
        for i in range(len(wuerfel)-1):
            zahl = wuerfel[i]
            if wuerfel[i+1]==zahl:
                count = count + 1
            else:
                count= 1
            if count == 3:
                paschzahl=zahl
                for i in wuerfel:
                    if i != paschzahl: 
                        wuerfel.remove(i)
                        wuerfel.append(random.randint(1,6))
                        optionen = getOptionenBot(spielblockbot)
    #Kniffel versuchen 
    elif "4er Pasch" in optionen:
        wuerfel.sort()
        count = 1
        paschzahl=0
        for i in range(len(wuerfel)-1):
            zahl = wuerfel[i]
            if wuerfel[i+1]==zahl:
                count = count + 1
            else:
                count= 1
            if count == 4:
                paschzahl=zahl
                for i in wuerfel:
                    if i != paschzahl: 
                        wuerfel.remove(i)
                        wuerfel.append(random.randint(1,6))
                        optionen = getOptionenBot(spielblockbot)      
    #große Straße versuchen                                   
    elif "kleine Straße" in optionen:
        wuerfel.sort()
        #fall von duplikaten --> set() entfernt duplikate
        if len(set(wuerfel)) <5:
            for i in range(0,5):
                if wuerfel.count(wuerfel[i]) > 1:
                    # wuerfel den index neu
                    wuerfel[i] = random.randint(1,6)
                    break
        else:
            #keine duplikate
            # am Anfang oder Ende ist das Problem
            if wuerfel[1] != wuerfel[0]+1:
                # der erste muss neu gewürfelt werden
                wuerfel[0] = random.randint(1,6)
            elif wuerfel[4] != wuerfel[3]+1:
                # der letzte muss neu gewürfelt werden
                wuerfel[4] = random.randint(1,6)
    
    #3er/4er Pasch/Kniffel versuchen     
    elif is2erPasch(wuerfel):
        wuerfel.sort()
        zahl = 0
        for i in range(0,5):
            if wuerfel.count(wuerfel[i]) ==2 :
                if wuerfel[i] > zahl:
                    zahl = wuerfel[i]
        for i in wuerfel:
            if i != zahl:
                wuerfel.remove(i)
                wuerfel.append(random.randint(1,6))
                
    #bspw. 1,2,3,5,6: höchste verfügbare zahl wird beibehalten, rest neu                 
    elif "kleine Straße" not in optionen and not is2erPasch(wuerfel):
        wuerfel.sort()
        x = 0
        for i in wuerfel:
            if i > 0 and spielblockbot[str(i)] != "x" and spielblockbot[str(i)] !=0:
                x = i
        for k in range(len(wuerfel)):
            if wuerfel[k] != x:
                wuerfel[k] = random.randint(1,6)
                
#ein spielzug (spieler)
def spielzug():
    global zug
    global runde 
    #buttons freigeben 
    Nochmalwürfeln.config(state=tk.NORMAL)
    Streichen.config(state=tk.NORMAL)
    Eintragen.config(state=tk.NORMAL)
    
    #ALLE WÜRFEL WIEDER BLAU 
    for w in wuerfel:
        w.config(bg="#d6eaf8")
    
    runde = runde + 1
    rundenanzeige.config(text="Runde : " + str(runde)+" von 13")
    
    zug = 0
    spielerlabel.config(fg="green")
    botlabel.config(fg="red")
            
    for i in wuerfel:
        i.config(text = str(random.randint(1,6)))  
    
#ein spielzug (bot)
def botzug():
    global runde
    global spielblockbot
    global botwuerfel
    global botpunkte
    #print("Zug Bot")    
    spielerlabel.config(fg="red")
    botlabel.config(fg="green")
    #5 random würfel
    botwuerfel = []
    for i in range(5):
        botwuerfel.append(random.randint(1,6))
    print("Bot 1. Wurf " +str(botwuerfel))
    
    #spieler buttons deaktivieren
    Nochmalwürfeln.config(state=tk.DISABLED)
    Streichen.config(state=tk.DISABLED)
    Eintragen.config(state=tk.DISABLED)

    #Wann nochmal gewürfelt werden soll  
    optionen = getOptionenBot(spielblockbot)
    
    #nicht nochmal würfeln in diesen fällen
    if "Kniffel" in optionen or "Full House" in optionen or "große Straße" in optionen:
        pass
    
    #nochmal würfeln in diesen fällen
    elif "3er Pasch" in optionen or "4er Pasch" in optionen:
        bot_nochmal(spielblockbot)
        print("Bot 2. Wurf " +str(botwuerfel))
     
    else:
        bot_nochmal(spielblockbot)
        print("Bot 2. Wurf " +str(botwuerfel))
        optionen = getOptionenBot(spielblockbot)
        if "Kniffel" in optionen or "Full House" in optionen or "große Straße" in optionen:            
            pass
        else:
            #nochmal würfeln 
            bot_nochmal(spielblockbot)
            print("Bot 3. Wurf " +str(botwuerfel))

    
    #eintragen für den bot
    eintragen = ""
    optionen = getOptionenBot(spielblockbot)
    print("Optionen (Bot): "+str(optionen))
    #wenn es optionen gibt
    if len(optionen)> 0:
        #hierarchische abarbeitung der optionen
        if "Kniffel" in optionen:
            eintragen = "Kniffel"
        elif "große Straße" in optionen:
            eintragen = "große Straße"
        elif "Full House" in optionen:
            eintragen = "Full House"
        elif "kleine Straße" in optionen:
            eintragen = "kleine Straße"
        else:
            #sonst random
            auswählen = random.randint(0, len(optionen)-1)
            computer_eintrag = optionen[auswählen]
            eintragen = computer_eintrag
            
            #nach besseren optionen prüfen
            if is4erPasch(botwuerfel):
                pasch_zahlen = get4erPasch(botwuerfel)
                pasch_zahlen.sort()
                #zahl für 4er Pasch sollte >= 4
                if "4er Pasch" in optionen and pasch_zahlen[0] >=4:
                    eintragen = "4er Pasch"
                #sonst wird es bei "1","2","3" eingetragen
                elif str(pasch_zahlen[0]) in optionen:
                    eintragen = str(pasch_zahlen[0]) 
                        
            elif is3erPasch(botwuerfel):
                pasch_zahlen = get3erPasch(botwuerfel)
                pasch_zahlen.sort()
                #zahl für 3er Pasch sollte >= 4
                if "3er Pasch" in optionen and pasch_zahlen[0] >=4:
                    eintragen = "3er Pasch"
                #sonst bei "1","2","3" eingetragen
                elif str(pasch_zahlen[0]) in optionen:
                    eintragen = str(pasch_zahlen[0]) 
            
            #nur zwei gleiche zahlen       
            elif is2erPasch(botwuerfel) and not is3erPasch(botwuerfel):
                pasch_zahlen = get2erPasch(botwuerfel)
                pasch_zahlen.sort()
                for zahl in pasch_zahlen:
                    if str(zahl) in optionen:
                        eintragen = str(zahl)
                        break
            else:
                #sonst bei "1","2",... eintragen
                botwuerfel.sort()
                for i in botwuerfel:
                    if str(i) in optionen:
                        eintragen = str(i)
                        break
                        
                #summiert ersten sechs Einträge
                keys = ["1","2", "3", "4", "5","6"]
                key_val = 0
                for key in keys:
                    #wenn key von "1","2",.. int ist (=nicht gestrichen)
                    if type(spielblockbot[key]) == type(1):
                        #key_val = summe values von "1","2",...
                        key_val = key_val + spielblockbot[key]
                
                #überprüfen ob bonus mit i geschafft werden kann 
                for i in botwuerfel: 
                    if i*botwuerfel.count(i) + key_val >= 63:
                        if str(i) in optionen:
                            eintragen = str(i)
                    
    #keine optionen = streichen
    else:
        streichen_optionen = getstreichenOptionenBot(spielblockbot)
    
        if "Kniffel" in streichen_optionen:
            spielblockbot["Kniffel"]="x"
            listboxbot.delete(12)
            listboxbot.insert(12, "")
                
        elif "4er Pasch" in streichen_optionen:
            spielblockbot["4er Pasch"]="x"
            listboxbot.delete(8)
            listboxbot.insert(8, "")
                
        elif "große Straße" in streichen_optionen:
            spielblockbot["große Straße"]="x"
            listboxbot.delete(11)
            listboxbot.insert(11, "")
            
        elif "1" in streichen_optionen:
            spielblockbot["1"]="x"
            listboxbot.delete(1)
            listboxbot.insert(1, "")
            
        elif "Full House" in streichen_optionen:
            spielblockbot["Full House"]="x"
            listboxbot.delete(9)
            listboxbot.insert(9, "")
            
        elif "3er Pasch" in streichen_optionen:
            spielblockbot["3er Pasch"]="x"
            listboxbot.delete(7)
            listboxbot.insert(7, "")
        else:
            #sonst wird random gestrichen
            auswählen = random.randint(0, len(streichen_optionen)-1)
            computer_eintrag = streichen_optionen[auswählen]
            spielblockbot[computer_eintrag]="x"
            
            spielblockbotlist = list(spielblockbot.keys())
            listboxbot.delete(spielblockbotlist.index(computer_eintrag)+1)
            listboxbot.insert(spielblockbotlist.index(computer_eintrag)+1, "")

    
    #punkte des bot
    counter = Counter(botwuerfel)
    
    if eintragen == "1":
        x = 0
        for i in botwuerfel:
            if i == 1:
                x=x+1
        spielblockbot["1"]=x
        botpunkte = botpunkte + x
        listboxbot.delete(1)
        listboxbot.insert(1, "")
            
    elif eintragen == "2":
        x = 0
        for i in botwuerfel:
            if i == 2:
                x=x+2
        spielblockbot["2"]=x
        botpunkte = botpunkte + x
        listboxbot.delete(2)
        listboxbot.insert(2, "")

        
    elif eintragen == "3":
        x = 0
        for i in botwuerfel:
            if i == 3:
                x=x+3
        spielblockbot["3"]=x
        botpunkte = botpunkte + x
        listboxbot.delete(3)
        listboxbot.insert(3, "")
        
    elif eintragen == "4":
        x = 0
        for i in botwuerfel:
            if i == 4:
                x=x+4
        spielblockbot["4"]=x
        botpunkte = botpunkte + x    
        listboxbot.delete(4)
        listboxbot.insert(4, "")

    elif eintragen == "5":
        x = 0
        for i in botwuerfel:
            if i == 5:
                x=x+5
        spielblockbot["5"]=x
        botpunkte = botpunkte + x       
        listboxbot.delete(5)
        listboxbot.insert(5, "")
        
    elif eintragen == "6":
        x = 0
        for i in botwuerfel:
            if i == 6:
                x=x+6
        spielblockbot["6"]=x
        botpunkte = botpunkte + x
        listboxbot.delete(6)
        listboxbot.insert(6, "")

    elif eintragen == "3er Pasch":
        x=0
        for zahl, count in counter.items():
            if count == 3:
                x = zahl * 3
        spielblockbot["3er Pasch"] = x
        botpunkte = botpunkte + x
        listboxbot.delete(7)
        listboxbot.insert(7, "")

    
    elif eintragen == "4er Pasch":
        x=0
        for zahl, count in counter.items():
            if count == 4:
                x = zahl * 4
        spielblockbot["4er Pasch"] = x
        botpunkte = botpunkte + x
        listboxbot.delete(8)
        listboxbot.insert(8, "")

        
    elif eintragen == "Full House":
        spielblockbot["Full House"] = 25
        botpunkte = botpunkte + 25
        listboxbot.delete(9)
        listboxbot.insert(9, "")
        
    elif eintragen == "kleine Straße":
        spielblockbot["kleine Straße"] = 30
        botpunkte = botpunkte + 30
        listboxbot.delete(10)
        listboxbot.insert(10, "")

    elif eintragen == "große Straße":
        spielblockbot["große Straße"] = 40
        botpunkte = botpunkte + 40
        listboxbot.delete(11)
        listboxbot.insert(11, "")

    elif eintragen == "Kniffel":
        spielblockbot["Kniffel"] = 50
        botpunkte = botpunkte + 50
        listboxbot.delete(12)
        listboxbot.insert(12, "")

    elif eintragen == "Chance":
        x=0
        for i in botwuerfel:
            x = x+i
        spielblockbot["Chance"] = x
        botpunkte = botpunkte + x
        listboxbot.delete(13)
        listboxbot.insert(13, "")

    
    
    #Kniffel Bonus
    summeoben = 0
    for o in spielblockbot:
        if o == "1" or o =="2" or o =="3"or o =="4"or o =="5"or o =="6" and spielblockbot[o]!="x":
            summeOben = summeoben + int(spielblockbot[o])
    
    if int(summeOben) >= 63:
        botpunkte = botpunkte + 35
    
          
    botpunktelabel.config(text="Punkte: "+ str(botpunkte))
    print("Bot fertig")
    print("Spielblock Bot " + str(spielblockbot))

    if runde < 13:
        spielzug()
    
    else:
        #spieler gewonnen
        if punkte>botpunkte: 
            nochmal = messagebox.askyesno("ENDE", "Du hast gewonnen!! Lust auf ein Rematch?")
            if nochmal:
                restart()
            else:
                kniffelroot.destroy()
        #unentschieden
        elif punkte == botpunkte:
            nochmal = messagebox.askyesno("ENDE", "Unentschieden. Nochmal?")
            if nochmal:
                restart()
            else:
                kniffelroot.destroy()
        #bot gewonnen   
        else:
            nochmal = messagebox.askyesno("ENDE", "Verloren... Rematch!")
            if nochmal:
                restart()
            else:
                kniffelroot.destroy()

#das Spiel
def spiel():
    global runde
    global punkte
    global botpunkte
    global spielblockspieler
    global spielblockbot
    
    #Startspielblock Spieler
    spielblockspieler = {
             "1": 0,
             "2": 0,
             "3": 0,
             "4": 0,
             "5": 0,
             "6": 0,
             "3er Pasch": 0,
             "4er Pasch": 0,
             "Full House": 0,
             "kleine Straße": 0,
             "große Straße": 0,
             "Kniffel": 0,
             "Chance": 0}

    #Startspielblock Bot
    spielblockbot = {
             "1": 0,
             "2": 0,
             "3": 0,
             "4": 0,
             "5": 0,
             "6": 0,
             "3er Pasch": 0,
             "4er Pasch": 0,
             "Full House": 0,
             "kleine Straße": 0,
             "große Straße": 0,
             "Kniffel": 0,
             "Chance": 0}
 
    spielzug()    
    


# Startseite

def startseite():
    startroot = tk.Tk()
    startroot.geometry("1000x600")
    startroot.title("Kniffel")
    startroot.configure(bg="#3b526c")
            
    #Zeilen/Spalten von startroot
    startroot.columnconfigure(0, weight=1)
    startroot.rowconfigure(0, weight=1)
            
    #Zeilen/Spalten von grid
    grid = tk.Frame(startroot, bg="#3b526c")
    grid.grid(column=0, row=0, sticky="nsew")
            
    for i in range(6):
        grid.columnconfigure(i, weight = 1)
                
    for j in range(6):
        grid.rowconfigure(j, weight =1)
        
    #Spielregeln Fenster   
    def regeln(event):
        regelnroot = tk.Toplevel()
        regelnroot.title("Kniffel Spielregeln")
        regelnroot.geometry("600x500")
        regelnroot.configure(bg="#3b526c")
        spielablauf_text = """
        *Runde starten
        - Jeder Spieler würfelt der Reihe nach mit allen 5 Würfeln.
        - Bis zu drei Würfe pro Zug:
          Nach dem ersten Wurf kann der Spieler beliebig viele Würfel zurücklegen und die restlichen 
          erneut würfeln.
          Dies kann bis zu dreimal pro Zug wiederholt werden.
        - Eintrag im Spielblock:
          Am Ende des Zuges muss ein Ergebnis in eine Kategorie eingetragen werden.
          Falls kein passendes Ergebnis erzielt wurde, darf eine Kategorie gestrichen werden 
          (kein Punktewert).

        *Wertungsblöcke
        - Oberer Block:
          Einträge basieren auf der Augensumme der Zahlen 1 bis 6.
          Bonus von 35 Punkten, wenn die Summe der Einträge ≥ 63 beträgt.
        - Unterer Block:
          Kombinationen:
          Dreierpasch: Mindestens drei gleiche Würfel, Summe aller Würfel.
          Viererpasch: Mindestens vier gleiche Würfel, Summe aller Würfel.
          Full House: Drei gleiche und zwei gleiche Würfel, 25 Punkte.
          Kleine Straße: Vier aufeinanderfolgende Zahlen, 30 Punkte.
          Große Straße: Fünf aufeinanderfolgende Zahlen, 40 Punkte.
          Kniffel: Fünf gleiche Würfel, 50 Punkte.
          Chance: Summe aller Würfel, keine Bedingungen.

        *Spielende
        - Das Spiel endet, wenn alle Kategorien aller Spieler ausgefüllt sind.
        - Gewinner: Der Spieler mit der höchsten Gesamtpunktzahl gewinnt."""

        # Label hinzufügen
        label = tk.Label(regelnroot, text=spielablauf_text, font = ('Times New Roman',9),bg="#4d6b8d",justify="left", anchor="nw", wraplength=550)
        label.pack(padx=20, pady=20)
        
    #widgets für startseite
    fragezeichen = tk.Label(startroot, text = "\u2370", foreground="white",background="#3b526c", 
                                        font=('Times New Roman', 18))
    fragezeichen.bind("<Button-1>", regeln)
    fragezeichen.grid(column=5, columnspan=3,row=0,sticky="n")
            
    titel_label = tk.Label(grid, text="Kniffel", fg="#a51216", bg="#3b526c", font=("Cooper Black", 50))
    titel_label.grid(column=2, columnspan=2, row=0, sticky="n") 
            
    frage1 = tk.Label(grid, text="Schaffst du es, den Bot zu besiegen?", fg= "white", bg="#3b526c", font=("Times New Roman", 20))
    frage1.grid(column=2, columnspan=2, row=2, sticky="n")
            
    startbutton = tk.Button(grid, width=20, height=6, text="START", font=('Times New Roman', 15), fg = "white",bg="#386f13", 
                                        command=lambda: [startroot.destroy()], activebackground="#336113", activeforeground="white")
    startbutton.grid(column=2,columnspan=2,row=3, sticky="n")
            
    anmerkung = tk.Label(grid, text="Klicke auf \u2370 für die Spielregeln", fg= "white", bg="#3b526c", font=("Arial", 10))
    anmerkung.grid(column=1, columnspan=4, row=4, sticky="n")


    startroot.mainloop()

     
startseite()

#GUI vom Spiel
kniffelroot = tk.Tk()
kniffelroot.geometry("1000x600")
kniffelroot.title("Kniffel")
kniffelroot.configure(bg="#d6eaf8")

# grid zeilen, spalten
for i in range(13):
    kniffelroot.columnconfigure(i, weight=1)
for j in range(8):
    kniffelroot.rowconfigure(j, weight=1)

# listbox für spieler
listboxspieler = tk.Listbox(kniffelroot, width=12, height=14, bg="#d1f2eb", fg="black", font=("Arial", 12))
listboxspieler.grid(column=0, row=0, rowspan=6, sticky="nsew", padx=10, pady=10)
listboxspieler.insert(0, "Dir fehlt:")
listboxspieler.insert(1, "1")
listboxspieler.insert(2, "2")
listboxspieler.insert(3, "3")
listboxspieler.insert(4, "4")
listboxspieler.insert(5, "5")
listboxspieler.insert(6, "6")
listboxspieler.insert(7, "3er Pasch")
listboxspieler.insert(8, "4er Pasch")
listboxspieler.insert(9, "Full House")
listboxspieler.insert(10, "kleine Straße")
listboxspieler.insert(11, "große Straße")
listboxspieler.insert(12, "Kniffel")
listboxspieler.insert(13, "Chance")

# listbox bot 
listboxbot = tk.Listbox(kniffelroot, width=12, height=14, bg="#fadbd8", fg="black", font=("Arial", 12))
listboxbot.grid(column=12, row=0, rowspan=6, sticky="nsew", padx=10, pady=10)
listboxbot.insert(0, "Bot fehlt:")
listboxbot.insert(1, "1")
listboxbot.insert(2, "2")
listboxbot.insert(3, "3")
listboxbot.insert(4, "4")
listboxbot.insert(5, "5")
listboxbot.insert(6, "6")
listboxbot.insert(7, "3er Pasch")
listboxbot.insert(8, "4er Pasch")
listboxbot.insert(9, "Full House")
listboxbot.insert(10, "kleine Straße")
listboxbot.insert(11, "große Straße")
listboxbot.insert(12, "Kniffel")
listboxbot.insert(13, "Chance")

# Frames für würfel
wuerfel_frame = tk.Frame(kniffelroot, bg="#d6eaf8")
wuerfel_frame.grid(column=1, row=1, columnspan=11, rowspan=4, sticky="nsew")

# würfel layout
wuerfel_frame.columnconfigure((0, 1, 2, 3, 4), weight=1)
wuerfel_frame.rowconfigure((0, 1), weight=1)

# würfel buttons
wuerfel = []

wuerfel.append(tk.Button(wuerfel_frame, text="1", bg="#d6eaf8", fg="black", font=("Arial", 25), 
                       activebackground="#c0defe",command=lambda: auswahl_wuerfeln(wuerfel[0])))
wuerfel.append(tk.Button(wuerfel_frame, text="1", bg="#d6eaf8", fg="black", font=("Arial", 25), 
                       activebackground="#c0defe",command=lambda: auswahl_wuerfeln(wuerfel[1])))
wuerfel.append(tk.Button(wuerfel_frame, text="1", bg="#d6eaf8", fg="black", font=("Arial", 25), 
                       activebackground="#c0defe",command=lambda: auswahl_wuerfeln(wuerfel[2])))
wuerfel.append(tk.Button(wuerfel_frame, text="1", bg="#d6eaf8", fg="black", font=("Arial", 25), 
                       activebackground="#c0defe",command=lambda: auswahl_wuerfeln(wuerfel[3])))
wuerfel.append(tk.Button(wuerfel_frame, text="1", bg="#d6eaf8", fg="black", font=("Arial", 25), 
                       activebackground="#c0defe",command=lambda: auswahl_wuerfeln(wuerfel[4])))

# position würfel
wuerfel[0].grid(column=1, row=0, sticky="nsew", padx=5, pady=5)
wuerfel[1].grid(column=2, row=0, sticky="nsew", padx=5, pady=5)
wuerfel[2].grid(column=3, row=0, sticky="nsew", padx=5, pady=5)
wuerfel[3].grid(column=1, row=1, sticky="nsew", padx=5, pady=5)
wuerfel[4].grid(column=2, row=1, sticky="nsew", padx=5, pady=5)

# Buttons unter den würfeln
button_frame = tk.Frame(kniffelroot, bg="#d6eaf8")
button_frame.grid(column=4, row=5, columnspan=5, sticky="nsew")
button_frame.columnconfigure((0, 1, 2), weight=1)

Streichen = tk.Button(button_frame, text="Streichen", bg="#fadbd8", font=("Arial", 12), activebackground="#f5b7b1", command=streichen_zeigen)
Streichen.grid(column=0, row=0, sticky="nsew", padx=5, pady=5)

Eintragen = tk.Button(button_frame, text="Eintragen", bg="#d1f2eb", font=("Arial", 12), activebackground="#a9dfbf", command=optionen_zeigen)
Eintragen.grid(column=1, row=0, sticky="nsew", padx=5, pady=5)

Nochmalwürfeln = tk.Button(button_frame, text="Nochmal würfeln", bg="#fef9e7", font=("Arial", 12), activebackground="#f9e79f", command=spieler_wuerfelt)
Nochmalwürfeln.grid(column=2, row=0, sticky="nsew", padx=5, pady=5)

#runden anzeigen
global runde 
runde = 0
rundenanzeige = tk.Label(kniffelroot, text="Runde "+ str(runde)+ " von 13", font = ('Arial', 10), bg = "#d6eaf8")
rundenanzeige.grid(column=5, row = 8, sticky="nsew")


# spieler info links unten
spielerlabel = tk.Label(kniffelroot, text="Spieler", font=("Arial", 15), fg="green", bg="#d6eaf8")
spielerlabel.grid(column=0, row=6, sticky="nsew", padx=5, pady=5)

global punkte
punkte = 0
spielerpunkte = tk.Label(kniffelroot, text="Punkte: "+str(punkte), font=("Arial", 20), bg="#d6eaf8")
spielerpunkte.grid(column=0, row=7, sticky="nsew", padx=5, pady=5)

# Bot info rechts unten
botlabel = tk.Label(kniffelroot, text="Bot", font=("Arial", 15), fg="red", bg="#d6eaf8")
botlabel.grid(column=12, row=6, sticky="nsew", padx=5, pady=5)

global botpunkte 
botpunkte = 0
botpunktelabel = tk.Label(kniffelroot, text="Punkte: "+str(botpunkte), font=("Arial", 20), bg="#d6eaf8")
botpunktelabel.grid(column=12, row=7, sticky="nsew", padx=5, pady=5)

#spiel starten
spiel()

kniffelroot.mainloop()


    
    
  
  
   


