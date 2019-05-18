import math

Ships = [
    {'name' : 'Light Fighter', 'short' : 'LF', 'price' : 3_500, 'repair' : 1079, 'damage' : 188, 'armor' : 966},
    {'name' : 'Heavy Fighter', 'short' : 'HF', 'price' : 8_000, 'repair' : 2810, 'damage' : 490, 'armor' : 2415},
    {'name' : 'Cruiser', 'short' : 'CR', 'price' : 32_000, 'repair' : 11078, 'damage' : 1903, 'armor' : 9660},
    {'name' : 'Battleship', 'short' : 'BA', 'price' : 90_000, 'repair' : 28875, 'damage' : 5765, 'armor' : 28_980},
    {'name' : 'Dreadnought', 'short' : 'DR', 'price' : 300_000, 'repair' : 88382, 'damage' : 13_620, 'armor' : 72_450},
    {'name' : 'Bomber', 'short' : 'BO', 'price' : 320_000, 'repair' : 107_000, 'damage' : 18_790, 'armor' : 96_590 },
    # {'name' : 'Destroyer', 'short' : 'DE', 'price' : 90_000, 'repair' : 31789, 'damage' : }
]

def get_repair_price():
    ship = input('Podaj nazwę statku: ').upper()
    for s in Ships:
        if s['short'] == ship:
            return s['repair'], s['name']

def get_resources_from_farm(): # Funkcja ta konwertuje z liczby float np 3.5 na 3.500.00 czyli dodaje zera tak by wyszły z zwykłej dziesiętnej liczby miliony
    x = eval(input('Podaj wartość: '))
    if type(x) == int:
        if int(x):
            x = int(str(x)+'000000')
        return x # zwraca integer
    # elif type(x) == float:
    #     x = str(x).split('.')
    #     if int(x[1]) < 10 and int(x[1]) > 1:
    #         x = int(str(x[0]) + str(x[1])+'00000')
    #     elif int(x[1]) > 10:    
    #         x = int(str(x[0])+str(x[1])+'0000') 
    #     return x
    elif type(x) == float:
        dec, prime = math.modf(x)
        prime = int(prime)
        # print(dec)
        # print(int(dec))
        # print(type(dec))
        # print(int(prime), 'dec', dec)
        if dec < 1:
            dec = "%.2f" % dec + '0000'
            x = str(prime)+str(dec[2:])
            print("{:,}".format(x))
            # print(type(dec))
        # return x


# z = get_resources_from_farm()
    
def count_repair():
    resources = get_resources_from_farm() # wartość farmy 
    rep, s_name = get_repair_price() # rozpakowanie zwróconych wartości
    loss_inp = int(input('Podaj straty w %: '))
    numbers_inp = int(input('Podaj liczbę statków: '))
    loss = int((loss_inp*numbers_inp)/100)
    costs = int((loss_inp*numbers_inp/100)*rep)
    total = int(resources - (loss_inp*numbers_inp)/100*rep)
    print('\nStraty: ',loss, 'Koszty: ', "{:,}".format(costs), 'Zarobek: ', "{:,}".format(total,'\n'))
   
while True:
    count_repair()

### rozbić funkcję count_repair() na moduły
