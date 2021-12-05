import random
a = open('log', 'w')
vertikal = 'ABCDEFGHIJ'
pole = [[' A ', ' B ', ' C ', ' D ', ' E ', ' F ', ' G ', ' H ', ' I ', ' J '],
        [' | ', ' | ', ' | ', ' | ', ' | ', ' | ', ' | ', ' | ', ' | ', ' | '],
        [' | ', ' | ', ' | ', ' | ', ' | ', ' | ', ' | ', ' | ', ' | ', ' | '],
        [' | ', ' | ', ' | ', ' | ', ' | ', ' | ', ' | ', ' | ', ' | ', ' | '],
        [' | ', ' | ', ' | ', ' | ', ' | ', ' | ', ' | ', ' | ', ' | ', ' | '],
        [' | ', ' | ', ' | ', ' | ', ' | ', ' | ', ' | ', ' | ', ' | ', ' | '],
        [' | ', ' | ', ' | ', ' | ', ' | ', ' | ', ' | ', ' | ', ' | ', ' | '],
        [' | ', ' | ', ' | ', ' | ', ' | ', ' | ', ' | ', ' | ', ' | ', ' | '],
        [' | ', ' | ', ' | ', ' | ', ' | ', ' | ', ' | ', ' | ', ' | ', ' | '],
        [' | ', ' | ', ' | ', ' | ', ' | ', ' | ', ' | ', ' | ', ' | ', ' | '],
        [' | ', ' | ', ' | ', ' | ', ' | ', ' | ', ' | ', ' | ', ' | ', ' | ']]


def Pole(pole):
    a = 0
    for i in pole:
        if a != 10:
            print(a, '', *i, end='\n')
        else:
            print(a, *i, end='\n')
        a += 1

pole_p1 = []
pole_p2 = []

def Rasstanovka(koordinaty, pole):
    if len(koordinaty) != 2:
        koor_vert_1 = int(koordinaty[1])
        koor_vert_2 = int(koordinaty[-1])
        koor_goriz_1 = vertikal.find(koordinaty[0])
        koor_goriz_2 = vertikal.find(koordinaty[-2])
    else:
        koor_vert_1 = int(koordinaty[1])
        koor_vert_2 = koor_vert_1
        koor_goriz_1 = vertikal.find(koordinaty[0])
        koor_goriz_2 = koor_goriz_1
    if koor_vert_1 == koor_vert_2:
        i = koor_goriz_2 - koor_goriz_1 + 1
        d = 0
        while i > 0:
            pole[koor_vert_1][koor_goriz_2 - d] = '*|'
            i -= 1
            d += 1
    elif koor_goriz_1 == koor_goriz_2:
        i = koor_vert_2 - koor_vert_1 + 1
        d = 0
        while i > 0:
            pole[koor_vert_2 - d] = abs(0 - koor_vert_1)*(' |') + '*|' + (12 - koor_vert_2)*(' |')
            i -= 1
            d += 1
    return pole

def choose():
    a.write('GAME:SEA_BATTLE\n')
    for i in range(1):
        r = int(input('Выбирите режим:1.ИИ против игрока,2.ИИ против ИИ,3.Игрок против игрока:'))
        if r == 1:
            a.write('GAME_MODE:II_P\n')
        elif r == 2:
            a.write('GAME_MODE:II_II\n')
        elif r == 3:
            a.write('GAME_MODE:P_P\n')
        else:
            print('Нужно выбрать из предложенного!')
            input('Выбирите режим:1.ИИ против игрока,2.ИИ против ИИ,3.Игрок против игрока')

        global name1
        name1 = input('Введите имя первого игрока:')
        global name2
        name2 = input('Введите имя второго игрока:')
        a.write('P1:' + name1 + '\n')
        a.write('P2:' + name2 + '\n')
        poz1()
        poz2()
        coin()
        igra()

def poz1():
    a.write('FIELD:' + '\n' + 'P1:\n')
    pole_p1 = pole.copy()
    for i in range(4):
        koordinaty = input('Player1, Введите расстановку однопалубника:')
        a.write('1: ' + koordinaty + '|' + '\n')
        Rasstanovka(koordinaty, pole_p1)

    for i in range(3):
        koordinaty = input('Player1, Введите расстановку двухпалубника:')
        a.write('2: ' + koordinaty + '|' + '\n')
        Rasstanovka(koordinaty, pole_p1)
    for i in range(2):
        koordinaty = input('Player1, Введите расстановку трехпалубника:')
        a.write('3: ' + koordinaty + '|' + '\n')
        Rasstanovka(koordinaty, pole_p1)
    for i in range(1):
        koordinaty = input('Player1, Введите расстановку четырехпалубника:')
        a.write('4: ' + koordinaty + '|' + '\n')
        a.write('\n')
        Rasstanovka(koordinaty, pole_p1)
        break
    Pole(pole_p1)

def coin():
    coin_p1 = int(input('Выбирите номер 1 или 2:'))
    if coin_p1 == random.randint(1, 2):
        print('Ход игрока', name1)
    else:
        print('Ход игрока', name2)

def poz2():
    a.write('FIELD:' + '\n' + 'P1:\n')
    pole_p2 = pole.copy()
    for i in range(4):
        koordinaty = input('Player2, Введите расстановку однопалубника:')
        a.write('1: ' + koordinaty + '|' + '\n')
        Rasstanovka(koordinaty, pole_p2)
    for i in range(3):
        koordinaty = input('Player2, Введите расстановку двухпалубника:')
        a.write('2: ' + koordinaty + '|' + '\n')
        Rasstanovka(koordinaty, pole_p2)
    for i in range(2):
        koordinaty = input('Player2, Введите расстановку трехпалубника:')
        a.write('3: ' + koordinaty + '|' + '\n')
        Rasstanovka(koordinaty, pole_p2)
    for i in range(1):
        koordinaty = input('Player2, Введите расстановку четырехпалубника:')
        a.write('4: ' + koordinaty + '|' + '\n')
        a.write('\n')
        Rasstanovka(koordinaty, pole_p2)
        break
    Pole(pole_p2)

def igra():
    counter_p1 = 0
    counter_p2 = 0
    while counter_p1 != 20 or counter_p2 != 20:
        hod = input('Ход первого игрока ')
        a = vertikal.index(hod[0])
        b = int(hod[1])
        if pole_p2[b][a] == '*|':
            pole_p2[b][a] = 'x'
            counter_p2 += 1
        elif pole_p2[b][a] == ' |':
            pole_p2[b][a] = 'o'
        Pole(pole_p2)
        hod = input('Ход  второго игрока ')
        a = vertikal.index(hod[0])
        b = int(hod[1])
        if pole_p1[b][a] == '*|':
            pole_p1[b][a] = 'x'
            counter_p1 += 1
        elif pole_p1[b][a] == ' |':
            pole_p1[b][a] = 'o'
        Pole(pole_p1)
    if counter_p1 == 20:
        print('Player_2 WON!!!')
    if counter_p2 == 20:
        print('Player_1 WON!!!')

choose()
