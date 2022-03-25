import csv      #importy modułów używanych w programie

from datetime import datetime

import random

print("\nDostępne gry:\n\n1. Lotto\n\n2. Multi Multi\n\n3. Eurojackpot\n")

lotteries_description = '''\n1. Lotto - Lotto jest grą kumulacyjną. Jeśli w losowaniu nie padnie „szóstka”, 
pula na tę wygraną przechodzi na kolejne losowanie. Każda rozbita kumulacja to nie 
tylko miliony trafione za szóstkę, ale i setki tysięcy w pozostałych wygranych.  
Im więcej osób zagra, tym większa będzie pula na wygrane, ponieważ zależy ona od liczby 
zawartych zakładów. Po losowaniu pieniądze z puli przeznaczonej na wygrane dzielimy między 
zwycięzców, którzy trafnie wytypowali wylosowane liczby. Wyjątek stanowi „trójka”, w przypadku 
której zawsze wypłacamy 24 zł.\n
2. Multi multi - W Multi Multi to Ty decydujesz, o ile grasz, a możesz wygrać nawet 25 000 000 zł! Twoja 
wygrana zależy od tego, ile liczb wytypujesz, z jaką stawką zagrasz i czy dodasz opcję gry z Plusem. 
Jeśli grasz z Plusem i go trafisz, przysługuje Ci wyższa wygrana z tabeli Multi Multi Plus. 
Jeśli grasz z wyższą stawką, wygraną odczytaną z tabeli mnożysz przez wysokość stawki.\n
3. Eurojackpot - O takiej wygranej Ci się nie śniło. Takich pieniędzy jeszcze nie widziałeś. 
Wielomilionowe wygrane w Eurojackpot przyspieszają bicie serca milionów ludzi. W grze bierze udział 
18 państw europejskich, w tym Polska. Typujesz 5 z 50 liczb oraz 2 z 12 liczb i grasz o niewyobrażalne 
pieniądze - nawet ponad pół miliarda złotych! W grze występuje aż 12 stopni wygranych.\n'''

description_validation = None   #konstrukcja obsługująca wywołanie legendy na prośbę użytkownika
while description_validation == None:
    description_validation_input = input("Czy chcesz zobaczyć krótki opis loterii?(T/N): ")
    if description_validation_input == 'T':
        description_validation = True
        print(lotteries_description)
    elif description_validation_input == "N":
        description_validation = False
    else:
        description_validation = None
        print("\nWprowadzona wartość jest nieprawdiłowa. Spróbuj ponownie.\n")  #obsługa nieprawidłowej wartości wprowadzonej przez użytkownika

lotto_numbers = []  #listy mające zawierać wyniki losowanie dla każdej z gier
multi_numbers = []
jackpot_numbers = []

lotto_validation = None
while lotto_validation == None: #ponowne korzystanie z pętli w celu obsługi nieprawidłowych wartości wprowadzanych przez użytkownika
    lotto_validation_input = input("\nCzy chcesz uruchomić generowanie liczb dla Lotto?(T/N): ")
    if lotto_validation_input == 'T':
        lotto_validation = True
        while len(lotto_numbers) < 6:
            n = random.randint(1,49)
            if n not in lotto_numbers:  #uniknięcie listy zawierającej dwie takie same liczby
                lotto_numbers.append(n)
            else:
                pass
        now = datetime.now()
        current_date = now.strftime("%d/%m/%Y %H:%M:%S")    #formatowanie daty i godziny
        data = [[current_date,"Lotto",lotto_numbers]]   #przypisanie zmiennej "data" ostatecznych informacji mających znależć się w pliku csv
        filename = 'totalizator_sportowy.csv'   #proces dodawania rekordu do pliku csv
        with open(filename, 'a', newline="") as file:
            csvwriter = csv.writer(file)
            csvwriter.writerows(data)
    elif lotto_validation_input == "N":
        lotto_validation = False
    else:
        lotto_validation = None
        print("\nWprowadzona wartość jest nieprawdiłowa. Spróbuj ponownie.\n")

multi_validation = None
while multi_validation == None:
    multi_validation_input = input("\nCzy chcesz uruchomić generowanie liczb dla Multi Multi?(T/N): ")   
    if multi_validation_input == 'T':
        multi_validation = True
        while len(multi_numbers) < 20:
            n = random.randint(1,80)
            if n not in multi_numbers:
                multi_numbers.append(n)
            else:
                pass
        now = datetime.now()
        current_date = now.strftime("%d/%m/%Y %H:%M:%S")
        data = [[current_date,"Multi Multi",multi_numbers]]
        filename = 'totalizator_sportowy.csv'
        with open(filename, 'a', newline="") as file:
            csvwriter = csv.writer(file)
            csvwriter.writerows(data)
    elif multi_validation_input == "N":
        multi_validation = False
    else:
        multi_validation = None
        print("\nWprowadzona wartość jest nieprawdiłowa. Spróbuj ponownie.\n")

jackpot_validation = None
while jackpot_validation == None:
    jackpot_validation_input = input("\nCzy chcesz uruchomić generowanie liczb dla Euro Jackpot?(T/N): ")
    if jackpot_validation_input == 'T':
        jackpot_validation = True
        while len(jackpot_numbers) < 7:
            n = random.randint(1,50)
            if n not in jackpot_numbers:
                jackpot_numbers.append(n)
            else:
                pass
        now = datetime.now()
        current_date = now.strftime("%d/%m/%Y %H:%M:%S")
        data = [[current_date,"Euro Jackpot",jackpot_numbers]]
        filename = 'totalizator_sportowy.csv'
        with open(filename, 'a', newline="") as file:
            csvwriter = csv.writer(file)
            csvwriter.writerows(data)
    elif jackpot_validation_input == "N":
        jackpot_validation = False
    else:
        jackpot_validation = None
        print("\nWprowadzona wartość jest nieprawdiłowa. Spróbuj ponownie.\n")

if lotto_numbers != []: #instrukcja warunkowa mająca określić które loterie zostały uruchomione przez użytkownika
    print(f"\nWylosowane liczby dla Lotto: {lotto_numbers}")
else:
    pass

if multi_numbers != []:
    print(f"\nWylosowane liczby dla Multi Multi: {multi_numbers}")
else:
    pass

if jackpot_numbers != []:
    print(f"\nWylosowane liczby dla Euro Jackpot: {jackpot_numbers}\n")
else:
    pass