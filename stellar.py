#!/usr/bin/env python3
""" Loss and farm counter for stellar age, it's in early stage od building, v:1.1 """
__author__  = 'Sebastian Ostrowski'

import math

Ships = [
    {'name' : 'Light Fighter', 'short' : 'LF', 'price' : 3_500, 'repair' : 932, 'damage' : 215, 'armor' : 1105},
    {'name' : 'Heavy Fighter', 'short' : 'HF', 'price' : 8_000, 'repair' : 2203, 'damage' : 559, 'armor' : 2764},
    {'name' : 'Cruiser', 'short' : 'CR', 'price' : 32_000, 'repair' : 8687, 'damage' : 2034, 'armor' : 11_050},
    {'name' : 'Battleship', 'short' : 'BA', 'price' : 90_000, 'repair' : 24_928, 'damage' : 6164, 'armor' : 33_170},
    {'name' : 'Dreadnought', 'short' : 'DR', 'price' : 300_000, 'repair' : 78_844, 'damage' : 15_040, 'armor' : 82_930},
    {'name' : 'Bomber', 'short' : 'BO', 'price' : 320_000, 'repair' : 95_683, 'damage' : 20_750, 'armor' : 110_580 },
    # {'name' : 'Destroyer', 'short' : 'DE', 'price' : 90_000, 'repair' : 31789, 'damage' : }
]

def get_repair_price():
    ship = input('Podaj nazwę statku: ').upper()
    for s in Ships:
        if s['short'] == ship:
            return s['repair'], s['name']

def get_resources_from_farm(): # Funkcja ta konwertuje z liczby float np 3.5 na 3.500.00 czyli dodaje zera tak by wyszły z zwykłej dziesiętnej liczby miliony
    x = eval(input('\nPodaj wartość: '))
    if type(x) == int:
        if int(x):
            x = int(str(x)+'000000')
        return int(x) # zwraca integer
    elif type(x) == float: # funkcja obsługuje liczby float z zerem po przecinku np 4.02
        dec, prime = math.modf(x)
        prime = int(prime)
        if dec < 1 or dec > 10:
            dec = "%.2f" % dec + '0000'
            x = str(prime)+str(dec[2:])
        elif dec == 1 or dec < 10:
            dec = "%.2f" % dec + '00000'
            x = str(prime)+str(dec)
        return float(x)
    
def count_repair():
    resources = get_resources_from_farm() # wartość farmy 
    rep, ship_name = get_repair_price() # rozpakowanie zwróconych wartości
    loss_inp = int(input('Podaj straty w %: '))
    numbers_inp = int(input('Podaj liczbę statków: '))
    loss = int((loss_inp*numbers_inp)/100)
    costs = int((loss_inp*numbers_inp/100)*rep)
    total = int(resources - (loss_inp*numbers_inp)/100*rep)
    return loss, costs, total, ship_name

def print_results():
    loss, costs, total, ship_name = count_repair()
    print('\n\tStraty ' + ship_name +':',loss, '| Koszty:',"{:,}".format(costs), '| Zarobek:',"{:,}".format(total))

while True:
    print_results()