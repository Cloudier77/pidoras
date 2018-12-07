import time
import random
import sys

pidarasi = ["Олег", "Рома","Эмиль","Колян","Радик","Саня","Матвей","Димас"]
pidarasi_ch=[] #не трогать нахуй!!!

def vibori():
    print("Команды:\nubr-убрать\ndob-добавить\nchn-подкрутить шанс\nspk-список\next-выход")
    print("ext - универсальная команда,\nработает везде")
    print("vih-досрочный выход")
    ch = input()
    if ch=="ubr":
        ubrat()
    elif ch=="dob":
        dobavit()
    elif ch=="chn":
        chance()
    elif ch=="spk":
        print("Список:\n"+str(pidarasi)+"\n")
        vibori()
    elif ch=="ext":
        print("OK")
        pass
    elif ch=="vih":
        print("OK")
        sys.exit()
    else:
        print("Не понял "+ch+"\n")
        vibori()
        
def dobavit():
    print("Кого добавить?")
    print(pidarasi)
    ch=input()
    if ch=="ext":
        print("ОК")
        vibori()
        return
    try:
        pidarasi.append(ch)
        print("Добавлен "+ch)
    except:
        print("Неа епта")
        dobavit()
        return
    print("Новый список:\n"+str(pidarasi)+"\n")
    ch=""
    dobavit()

def ubrat():
    print("Кого убрать?\n")
    print(pidarasi)
    ch=input()
    if ch=="ext":
        print("ОК")
        vibori()
        return
    try:
        pidarasi.remove(ch)
        print("Убран "+ch)
    except:
        print("Неа епта")
        ubrat()
        return
    print("Новый список:\n"+str(pidarasi)+"\n")
    ch=""
    ubrat()
        
def chance():
    print("Подкручивание шанса")
    print("Кому подкрутить шанс выпадения?")
    print(str(pidarasi))
    ch=input()
    if ch=="ext":
        print("ОК")
        vibori()
        return
    kol=pidarasi.count(ch)
    if kol>=1:
        pass
    else:
        print("Такого нет епта!")
        chance()
        return
    print("Во сколько раз подкрутить? Введите число:")
    try:
        kol = int(input())
    except:
        print("Яж просил...")
        chance()
    if kol=="ext":
        print("ОК")
        vibori()
        return
    print("Подкручен шанс "+ch+" в "+str(kol)+" раз.")
    while kol!=0:
        pidarasi_ch.append(ch)
        kol-=1
    vibori()
#----------


while True:
    print("Стандарт:\n"+str(pidarasi)+"\nХотите изменить?")
    print("Y/N")
    ch = input()
    if ch == "Y":
        vibori()       
        break
    elif ch == "N":
        print("OK")
        break
    print("Не понял "+ch+"\n")

pidarasi.extend(pidarasi_ch)
print("Система выбора пидораса на рандом.")
time.sleep(1)
i=0
while(i!=105):
    try:
        pidar = random.choice(pidarasi)
    except:
        print("ТЫ СЛОМАЛ ВСЕ НАХУЙ!!")
        time.sleep(1)
        sys.exit()
    print(pidar)
    if (i<40):
        time.sleep(0.05)
        i+=1
    elif (i<80):
        time.sleep(0.1)
        i+=1
    elif (i<100):
        time.sleep(0.2)
        i+=1
    elif (i<106):
        time.sleep(0.5)
        i+=1


time.sleep(1)
print("Пидарас: "+pidar)
