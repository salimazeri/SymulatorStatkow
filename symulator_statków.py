#-*- coding: utf-8 -*-

from random import randint
from random import choice
class DaneStatków:

    def __init__(self,plik):

        self.main_list = []
        self.big = []
        try:
            plik = open('dane_statkow.txt', "r")
        except IOError:
            print ('Problem z plikiem ', plik)

        for line in plik.readlines()[1:]:
            line = line.rstrip()
            if line:
                self.main_list.append(line)

        for lista in self.main_list:
            for el in lista.split(" "):
                self.big.append(el)

        self.mt = self.big[:5]
        self.dt = self.big[5:10]
        self.lm = self.big[10:15]
        self.mc = self.big[15:20]
        self.kr = self.big[20:25]
        self.ow = self.big[25:30]
        self.sk = self.big[30:35]
        self.re = self.big[35:40]
        self.ss = self.big[40:45]
        self.b = self.big[45:50]
        self.n = self.big[50:55]
        self.gs = self.big[55:60]
        self.p = self.big[60:65]

    def mt(self): return self.mt
    def dt(self): return self.dt
    def lm(self): return self.lm
    def mc(self): return self.mc
    def kr(self): return self.kr
    def ow(self): return self.ow
    def sk(self): return self.sk
    def re(self): return self.re
    def ss(self): return self.ss
    def b(self): return self.b
    def n(self): return self.n
    def gs(self): return self.gs
    def p(self): return self.p
    
    




class Statek:

    def __init__(self, statek):

        self.skrót = statek[0]
        self.nazwa = statek[1]
        self.hp = eval(statek[2])
        self.maxhp = eval(statek[2])
        self.armor = eval(statek[3])
        self.maxarmor = eval(statek[3])
        self.atak = eval(statek[4])

        self.szybkie_dziala_list = []
        try:
            plik = open('szybkie_dziala.txt', "r")
            for line in plik.readlines()[1:]:
                line = line.rstrip()[2:].split()
                if line:
                    self.szybkie_dziala_list.append(line)
        except IOError:
            print ('Problem z plikiem ')
            
    def szybkie_dziala(self, statek):
        def check(statek):
            if (statek.skrót == 'mt'):
                return 0
            if (statek.skrót == 'dt'):
                return 1
            if (statek.skrót == 'lm'):
                return 2
            if (statek.skrót == 'cm'):
                return 3
            if (statek.skrót == 'kr'):
                return 4
            if (statek.skrót =='ow'):
                return 5
            if (statek.skrót == 'sj'):
                return 6
            if (statek.skrót == 're'):
                return 7
            if (statek.skrót == 'ss'):
                return 8
            if (statek.skrót == 'b'):
                return 9
            if (statek.skrót == 'n'):
                return 10
            if (statek.skrót == 'gs'):
                return 11
            if (statek.skrót == 'p'):
                return 12
        if (self.skrót == 'mt'):
            return self.szybkie_dziala_list[0][check(statek)]
        if (self.skrót == 'dt'):
            return self.szybkie_dziala_list[1][check(statek)]
        if (self.skrót == 'lm'):
            return self.szybkie_dziala_list[2][check(statek)]
        if (self.skrót == 'cm'):
            return self.szybkie_dziala_list[3][check(statek)]
        if (self.skrót == 'kr'):
            return self.szybkie_dziala_list[4][check(statek)]
        if (self.skrót == 'ow'):
            return self.szybkie_dziala_list[5][check(statek)]
        if (self.skrót == 'sj'):
            return self.szybkie_dziala_list[6][check(statek)]
        if (self.skrót == 're'):
            return self.szybkie_dziala_list[7][check(statek)]
        if (self.skrót == 'ss'):
            return self.szybkie_dziala_list[8][check(statek)]
        if (self.skrót == 'b'):
            return self.szybkie_dziala_list[9][check(statek)]
        if (self.skrót =='n'):
            return self.szybkie_dziala_list[10][check(statek)]
        if (self.skrót == 'gs'):
            return self.szybkie_dziala_list[11][check(statek)]
        if (self.skrót == 'p'):
            return self.szybkie_dziala_list[12][check(statek)]
        
    def isDestroyed(self):
        if (self.hp <= 0):
            return True
        return False

    def shoot(self,statek):
        self.shoot_(statek)
        chance = 1-1/eval(self.szybkie_dziala(statek))
        random_chance = randint(1,100)
        if (random_chance < chance):
            print('strzelam ponownie')
            return True
        return False
    
    def shoot_(self,statek):
        #Osłona odnawia się (jej ilość wraca do maksymalnej wartości) na początku każdej rundy walki.
        #print (self.skrót,' atakuje ', statek.skrót)
        #print('stan ',statek.skrót,' przed atakiem: ',statek.statekInfo())

        if (self.atak < 0.01*statek.armor):
            #print('statek atakujący posiada zbyt mało ataku by zaatakować statek')
            return
        if (self.hp < 0.7*self.maxhp):
            chance = (1 - (self.hp / self.maxhp))*100
            random_chance = randint(1,100)
            if random_chance < chance:
                statek.hp = 0
                #print ('Trafiony zatopiony :)')
                return
        if (statek.armor > 0):
            if (self.atak > statek.armor):
                statek.armor = 0
                statek.hp = statek.hp - (self.atak - statek.maxarmor)
            else:
                statek.armor = statek.armor - self.atak
        else:
            statek.hp = statek.hp - self.atak
        #print('stan ',statek.skrót,' po ataku: ',statek.statekInfo())
    def statekInfo(self):
        return {'hp':self.hp, 'armor':self.armor,'atak':self.atak}

class Flota:


    def __init__(self, plik):
        self.flota = []
        self.lista = []
        self.nazwy = ['mt','dt','lm',
                      'mc','kr','ow',
                      'sk','re','ss',
                      'b','n','p',
                      'gs']
        try:
            plik = open(plik, "r")
        except IOError:
            print ('Problem z plikiem ', plik)
        i = 0
        for line in plik.readlines()[1:]:
            line = line.rstrip()
            if line:
                self.lista.append(line.split(" ")[1])
                i = i + 1
        #print (self.lista)
        self.mt = self.lista[0]
        self.dt = self.lista[1]
        self.lm = self.lista[2]
        self.mc = self.lista[3]
        self.kr = self.lista[4]
        self.ow = self.lista[5]
        self.sk = self.lista[6]
        self.re = self.lista[7]
        self.ss = self.lista[8]
        self.b = self.lista[9]
        self.n = self.lista[10]
        self.p = self.lista[11]
        self.gs = self.lista[12]
        dane_statkow = DaneStatków("dane_statkow.txt")
        print ('Tworzę obiekty floty')
        for i in range(len(self.lista)):
            for j in range(eval(self.lista[i])):
                if (self.nazwy[i] == 'mt'):
                    self.flota.append(Statek(dane_statkow.mt))
                    
                if (self.nazwy[i] == 'dt'):
                    self.flota.append(Statek(dane_statkow.dt))
                    
                if (self.nazwy[i] == 'lm'):
                    self.flota.append(Statek(dane_statkow.lm))
                    
                if (self.nazwy[i] == 'mc'):
                    self.flota.append(Statek(dane_statkow.mc))
                    
                if (self.nazwy[i] == 'kr'):
                    self.flota.append(Statek(dane_statkow.kr))
                    
                if (self.nazwy[i] == 'ow'):
                    self.flota.append(Statek(dane_statkow.ow))
                    
                if (self.nazwy[i] == 'sk'):
                    self.flota.append(Statek(dane_statkow.sk))
                    
                if (self.nazwy[i] == 're'):
                    self.flota.append(Statek(dane_statkow.re))
                    
                if (self.nazwy[i] == 'ss'):
                    self.flota.append(Statek(dane_statkow.ss))
                    
                if (self.nazwy[i] == 'b'):
                    self.flota.append(Statek(dane_statkow.b))
                    
                if (self.nazwy[i] == 'n'):
                    self.flota.append(Statek(dane_statkow.n))
                    
                if (self.nazwy[i] == 'p'):
                    self.flota.append(Statek(dane_statkow.p))
                    
                if (self.nazwy[i] == 'gs'):
                    self.flota.append(Statek(dane_statkow.gs))
                    
        print ('Obiekty floty zostały stworzone')
                
    def show(self):
        for i in range(len(self.lista)):
            print(self.nazwy[i],':',self.lista[i])
        return

    def start_shooting(self, flota):
        for i in range(len(self.flota)):
            target = choice(flota.flota)
            shoot = self.flota[i].shoot(target)
            while (shoot is True):
                self.flota[i].shoot(target)
            
    def remove_destroyed(self):
        print ('liczebność floty przed usunięciem zniszczonych statków: ', len(self.flota))
        temp_flota = self.flota
        try:
            for i in range(len(temp_flota)):
                #print ('hp statku: ', temp_flota[i].hp)
                if (temp_flota[i].hp <= 0):
                    #print ('usuwam')
                    self.flota.remove(self.flota[i])
        except IndexError:
            pass
        print ('liczebność floty po usunięciu zniszczonych statków: ', len(self.flota))

    
def start_game(flota1,flota2):
    f1 = Flota(flota1)
    f2 = Flota(flota2)
    print ("START GRY")
    for runda in range(6):
        print ('\n\n\n\nrunda ',runda+1)
        f1.start_shooting(f2)
        f2.start_shooting(f1)
        print ('flota1')
        f1.remove_destroyed()
        print ('flota2')
        f2.remove_destroyed()
    if (len(f1.flota) == 0):
        print ('flota2 wygrała')
    elif (len(f2.flota) == 0):
        print ('flota1 wygrała')
    else:
        print ('remis')
    print ('\n\n\nKONIEC GRY')
start_game("flota_1.txt","flota_1.txt")
start_game("flota_1.txt","flota_2.txt")
