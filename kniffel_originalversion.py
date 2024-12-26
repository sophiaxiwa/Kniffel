# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 12:20:42 2024

@author: demo
""" 
   
import random
from copy import deepcopy

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

def nochmal_würfeln(spieler, spielblock, wuerfel):
    if spieler == "Spieler": 
        neue_wuerfe = input("Welche Würfel sollen neu geworfen werden?")
        neue_wuerfe = neue_wuerfe.split(",")
        for i in range(len(neue_wuerfe)):
            neue_wuerfe[i] = int(neue_wuerfe[i]) 
                
        wuerfel_neu = neue_wuerfe
            
            
        
        for index in wuerfel_neu:
            wuerfel[index] = random.randint(1,6)
        wuerfel.sort()
        print(wuerfel)
    
    elif spieler == "Unser Bot":
        optionen = getOptionen(spielblock, wuerfel)
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
                            optionen = getOptionen(spielblock, wuerfel)
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
                            optionen = getOptionen(spielblock, wuerfel)
                            
        elif "kleine Straße" in optionen:
            wuerfel.sort()
            if len(set(wuerfel)) <5:
                # fall von duplikaten
                for i in range(0,5):
                    if wuerfel.count(wuerfel[i]) > 1:
                        # wuerfel den index neu
                        wuerfel[i] = random.randint(1,6)
                        break
            else:
                # am Anfang oder Ende ist das Problem
                if wuerfel[1] != wuerfel[0]+1:
                    # der erste muss neu gewürfelt werden
                    wuerfel[0] = random.randint(1,6)
                elif wuerfel[4] != wuerfel[3]+1:
                    # der letzte muss neu gewürfelt werden
                    wuerfel[4] = random.randint(1,6)
       
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
             
        elif "kleine Straße" not in optionen and not is2erPasch(wuerfel):
            wuerfel.sort()
            x = 0
            for i in wuerfel:
                if i > 0 and spielblock[str(i)] != "x" and spielblock[str(i)] !=0:
                    x = i
            for k in range(len(wuerfel)):
                if wuerfel[k] != x:
                    wuerfel[k] = random.randint(1,6)
                    
                    
                    
                
                            
    else:
        entscheidung_anzahl = random.randint(0,5)
        entscheidung_positionen = random.sample(range(0, 5), entscheidung_anzahl)
        
        
        for i in entscheidung_positionen:
            entscheidung_zahl = random.randint(1,6)
            wuerfel[i] = entscheidung_zahl
        

def getOptionen(spielblock, wuerfel):    
    optionen = []
    
    if 1 in wuerfel and spielblock["1"]==0:
        optionen.append("1")
    if 2 in wuerfel and spielblock["2"]==0:
        optionen.append("2")
    if 3 in wuerfel and spielblock["3"]==0:
        optionen.append("3")
    if 4 in wuerfel and spielblock["4"]==0:
        optionen.append("4")
    if 5 in wuerfel and spielblock["5"]==0:
        optionen.append("5")
    if 6 in wuerfel and spielblock["6"]==0:
        optionen.append("6")
        
        
    if is3erPasch(wuerfel) and spielblock["3er Pasch"]==0:
        optionen.append("3er Pasch")
    if is4erPasch(wuerfel) and spielblock["4er Pasch"]==0:
        optionen.append("4er Pasch")
    if isKniffel(wuerfel) and spielblock["Kniffel"]==0:
        optionen.append("Kniffel")
    if iskleineStraße(wuerfel) and spielblock["kleine Straße"]==0:
        optionen.append("kleine Straße")
    if isgroßeStraße(wuerfel) and spielblock["große Straße"]==0:
        optionen.append("große Straße")
    if isFullHouse(wuerfel) and spielblock["Full House"]==0:
        optionen.append("Full House")
    if spielblock["Chance"]==0:
        optionen.append("Chance")
    return optionen


def spielzug(spielblock, wuerfel, spieler="Spieler"):

    for i in range(5):
        wuerfel[i] = random.randint(1,6)
    wuerfel.sort()
    print(wuerfel)
    
    optionen = getOptionen(spielblock, wuerfel)

    if spieler == "Spieler": 
        nochmal = input("Willst du nochmal würfeln?")
        if nochmal == "ja":    
            nochmal_würfeln(spieler, spielblock, wuerfel)
            
            nochmal = input("Willst du nochmal würfeln?")
            if nochmal == "ja":    
                nochmal_würfeln(spieler, spielblock, wuerfel)
    
    elif spieler == "Unser Bot":
    # Wann nochmal gewürfelt werden soll  
        optionen = getOptionen(spielblock, wuerfel)
        if "Kniffel" in optionen or "Full House" in optionen or "große Straße" in optionen:
            pass
        
        elif "3er Pasch" in optionen or "4er Pasch" in optionen:
            nochmal_würfeln("Unser Bot",spielblock,wuerfel)
        
        
        else:
            optionen = getOptionen(spielblock, wuerfel)
            nochmal_würfeln("Unser Bot", spielblock, wuerfel)
            if i == "Kniffel" or i == "Full House" or i == "große Straße":
                pass
            else:
                nochmal_würfeln("Unser Bot", spielblock, wuerfel)
    
    else:
        decision = random.randint(0,1)
        if decision == 0:
            nochmal_würfeln(False, wuerfel)
            decision2 = random.randint(0,1)
            if decision2 == 0:
                nochmal_würfeln(False, wuerfel)

    
    
    computer_eintrag = ""
    
    optionen = getOptionen(spielblock, wuerfel)

    print("Deine Optionen sind ")
    for i in optionen:
        print(i)
        
    streichen_optionen = []
    
    if spielblock["1"]==0:
        streichen_optionen.append("1")
    if spielblock["2"]==0:
        streichen_optionen.append("2")
    if spielblock["3"]==0:
        streichen_optionen.append("3")
    if spielblock["4"]==0:
        streichen_optionen.append("4")
    if spielblock["5"]==0:
        streichen_optionen.append("5")
    if spielblock["6"]==0:
        streichen_optionen.append("6")
            
            
    if spielblock["3er Pasch"]==0:
        streichen_optionen.append("3er Pasch")
    if spielblock["4er Pasch"]==0:
        streichen_optionen.append("4er Pasch")
    if spielblock["Kniffel"]==0:
        streichen_optionen.append("Kniffel")
    if spielblock["kleine Straße"]==0:
        streichen_optionen.append("kleine Straße")
    if spielblock["große Straße"]==0:
        streichen_optionen.append("große Straße")
    if spielblock["Full House"]==0:
        streichen_optionen.append("Full House")
    if spielblock["Chance"]==0:
        streichen_optionen.append("Chance")
    
    if spieler == "Spieler":
        eintragen = input("Wo willst du das Ergebnis eintragen? Oder willst du etwas streichen?")  
        while True:  
            if eintragen == "streichen":
                print("Deine Optionen sind ")    
                for i in streichen_optionen:
                    print(i)
                streichen_ort = input("Was möchtest du streichen?")
                if streichen_ort in streichen_optionen:
                    spielblock[streichen_ort]="x"
                    break
                else:    
                    while True:
                        print("Dies ist keine Option")
                        streichen_ort = input("Was möchtest du stattdessen streichen?")
                        if streichen_ort in streichen_optionen:
                            spielblock[streichen_ort]="x"
                            break
                    break
            elif eintragen in optionen:
                break
            else:
                print("Dies ist keine Option")
                eintragen = input("Wo willst du das Ergebnis eintragen? Oder willst du etwas streichen?")
    
    elif spieler == "Unser Bot": 
        # Hier wird eingetragen!
        wuerfel.sort()
        eintragen = "nix"
        if len(optionen)> 0:
            if "Kniffel" in optionen:
                eintragen = "Kniffel"
            elif "große Straße" in optionen:
                eintragen = "große Straße"
            elif "Full House" in optionen:
                eintragen = "Full House"
            elif "kleine Straße" in optionen:
                eintragen = "kleine Straße"
            
            else:
                auswählen = random.randint(0, len(optionen)-1)
                computer_eintrag = optionen[auswählen]
                eintragen = computer_eintrag
                        
                if is4erPasch(wuerfel):
                    pasch_zahlen = get4erPasch(wuerfel)
                    pasch_zahlen.sort()
                    if "4er Pasch" in optionen and pasch_zahlen[0] >=4:
                        eintragen = "4er Pasch"
                    elif str(pasch_zahlen[0]) in optionen:
                        eintragen = str(pasch_zahlen[0]) 
                        
                elif is3erPasch(wuerfel):
                    pasch_zahlen = get3erPasch(wuerfel)
                    pasch_zahlen.sort()
                    if "3er Pasch" in optionen and pasch_zahlen[0] >=4:
                        eintragen = "3er Pasch"
                    elif str(pasch_zahlen[0]) in optionen:
                        eintragen = str(pasch_zahlen[0]) 
                        
                elif is2erPasch(wuerfel) and not is3erPasch(wuerfel):
                    pasch_zahlen = get2erPasch(wuerfel)
                    pasch_zahlen.sort()
                    for zahl in pasch_zahlen:
                        if str(zahl) in optionen:
                            eintragen = str(zahl)
                            break
                else:
                    wuerfel.sort()
                    for i in wuerfel:
                        if str(i) in optionen:
                            eintragen = str(i)
                            break
                        
                    #summiert ersten sechs Einträge
                    keys = ["1","2", "3", "4", "5","6"]
                    key_val = 0
                    for key in keys:
                        if type(spielblock[key]) == type(1):
                            key_val = key_val + spielblock[key]
                    
                    for i in wuerfel:
                        if i*wuerfel.count(i) + key_val >= 63:
                            if str(i) in optionen:
                                eintragen = str(i)
                        
                    
            
        else:
            if "Kniffel" in streichen_optionen:
                spielblock["Kniffel"]="x"
                
            elif "4er Pasch" in streichen_optionen:
                spielblock["4er Pasch"]="x"
                
            elif "große Straße" in streichen_optionen:
                spielblock["große Straße"]="x"
            
            elif "1" in streichen_optionen:
                spielblock["1"]="x"
            
            elif "Full House" in streichen_optionen:
                spielblock["Full House"]="x"
            
            elif "3er Pasch" in streichen_optionen:
                spielblock["3er Pasch"]="x"
            else:
               auswählen = random.randint(0, len(streichen_optionen)-1)
               print("Testprint", len(streichen_optionen)-1)
               computer_eintrag = streichen_optionen[auswählen]
               spielblock[computer_eintrag]="x"
    
    
    else:
        entscheidung = random.randint(0,1)
        
        eintragen = "nix"
        if entscheidung == 0 and len(optionen)> 0:
            auswählen = random.randint(0, len(optionen)-1)
            computer_eintrag = optionen[auswählen]
            eintragen = computer_eintrag
        else:
            auswählen = random.randint(0, len(streichen_optionen)-1)
            computer_eintrag = streichen_optionen[auswählen]
            spielblock[computer_eintrag]="x"
        
         
         
    
    if eintragen == "1":
        x = 0
        for i in wuerfel:
            if i == 1:
                x=x+1
        spielblock["1"]=x
       
    
          
    elif eintragen == "2":
        x = 0
        for i in wuerfel:
            if i == 2:
                x=x+2
        spielblock["2"]=x
       
    
    elif eintragen == "3":
        x = 0
        for i in wuerfel:
            if i == 3:
                x=x+3
        spielblock["3"]=x
       
    
    elif eintragen == "4":
        x = 0
        for i in wuerfel:
            if i == 4:
                x=x+4
        spielblock["4"]=x
       
    
    elif eintragen == "5":
        x = 0
        for i in wuerfel:
            if i == 5:
                x=x+5
        spielblock["5"]=x
       
    
    elif eintragen == "6":
        x = 0
        for i in wuerfel:
            if i == 6:
                x=x+6
        spielblock["6"]=x
        
    elif eintragen == "3er Pasch":
        x=0
        for i in wuerfel:
            x = x+i
        spielblock["3er Pasch"] = x
    
    elif eintragen == "4er Pasch":
        x=0
        for i in wuerfel:
            x = x+i
        spielblock["4er Pasch"] = x
    
    elif eintragen == "Full House":
        spielblock["Full House"] = 25
    
    elif eintragen == "kleine Straße":
        spielblock["kleine Straße"] = 30
        
    elif eintragen == "große Straße":
        spielblock["große Straße"] = 40
        
    elif eintragen == "Kniffel":
        spielblock["Kniffel"] = 50
    
    elif eintragen == "Chance":
        x=0
        for i in wuerfel:
            x = x+i
        spielblock["Chance"] = x
        
    print(spielblock)

def spiel(spieler):
    spielblock = {
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
    
    punkte = 0
    
    
    wuerfel = [0,0,0,0,0]
        
    for i in range(13):
        
        spielzug(spielblock, wuerfel, spieler)    
    
    keys = ["1","2", "3", "4", "5","6"]
    key_val = 0
    for key in keys:
        if type(spielblock[key]) == type(1):
            key_val = key_val + spielblock[key]
    if key_val >= 63:
        punkte = punkte + 35
            
    
    for i in spielblock:
        if type(spielblock[i]) == type(1):
            punkte = punkte + spielblock[i]
    
    print("Deine Gesamtpunktzahl beträgt " , punkte)
    return punkte
        
gesamt_punkte= 0   
n = 100
punkte_liste=[]
for i in range(0,n):
    #wenn Mensch spielt, dann spiel("Spieler")
    #wenn schlauer Bot spielt, dann spiel("Unser Bot")
    #bei allem anderen spielt dummer Bot
    #gesamt_punkte = gesamt_punkte + spiel("Unser Bot")   
    punkte_liste.append(spiel("Unser Bot"))
durchschnitt = sum(punkte_liste)/n 
größter_wert = max(punkte_liste)
kleinster_wert = min(punkte_liste)
#print(größter_wert)
#print(kleinster_wert)
        
        
    