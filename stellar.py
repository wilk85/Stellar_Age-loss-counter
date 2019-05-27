#!/usr/bin/env python3
""" Loss and farm counter for stellar age, it's in early stage od building, v:1.0"
__author__  = 'Sebastian Ostrowski'

Ships = [
    {'name' : 'Light Fighter', 'short' : 'LF', 'price' : 3_500, 'repair' : 1188},
    {'name' : 'Heavy Fighter', 'short' : 'HF', 'price' : 8_000, 'repair' : 2810},
    {'name' : 'Cruiser', 'short' : 'CR', 'price' : 32_000, 'repair' : 8814},
    {'name' : 'Battleship', 'short' : 'BA', 'price' : 90_000, 'repair' : 25292},
    {'name' : 'Dreadnought', 'short' : 'DR', 'price' : 300_000, 'repair' : 79995}
    {'name' : 'Bomber', 'short' : 'BO', 'price' : 330_000, 'repair' : 97080}
]

def get_repair_price():
    ship = input('Podaj nazwę statku: ').upper()
    for s in Ships:
        if s['short'] == ship:
            return s['repair'], s['name']

def count_repair():
    rep, s_name = get_repair_price() # rozpakowanie zwróconych wartości
    loss = int(input('Podaj straty w %: '))
    numbers = int(input('Podaj liczbę statków: '))
    print('Strata statków:', s_name, ':', int((loss*numbers)/100))
    print('\t', int((loss*numbers)/100)*rep, '\n')

while True:
    count_repair()

    # Vacuum polarization I = lv 20 / 10.5% reduction BA: 31500 / 65%, CR: 10977
