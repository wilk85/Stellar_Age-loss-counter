
Ships = [
    {'name' : 'Light Fighter', 'short' : 'LF', 'price' : 3_500, 'repair' : 1188},
    {'name' : 'Heavy Fighter', 'short' : 'HF', 'price' : 8_000, 'repair' : 2810},
    {'name' : 'Cruiser', 'short' : 'CR', 'price' : 32_000, 'repair' : 11078},
    {'name' : 'Battleship', 'short' : 'BA', 'price' : 90_000, 'repair' : 31789}
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


# Cena zakupu za sztukę
# Light = 3,5, Heavy = 8, Cruiser = 32, Battleship = 90, 

# Cena naprawy za sztukę
# Light = 1188, Heavy = 2810, Cruiser = 11078, Battleship = 31789

# obliczenia 32000 - 65,38% = 11078,4 - cruiser
# 64,68