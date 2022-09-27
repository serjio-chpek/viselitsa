import random
 
slova = ["лебедь", "ива", "маршрутка", "поезд", "самолет"] #массив со словами
slovo=slova[random.randrange(5)] #рандомный выбор слова из массива
dlina=len(slovo) #число букв в слове
zdorovie = 10
proverka=False #проверка правильности буквы
uslet="" #буквы, которые уже писались
itogslovo=[] #итоговое слово
for i in range(len(slovo)): #шифровка букв в словах
    itogslovo+="_"
 
while dlina != 0 and zdorovie != 0:
    proverka = False
    while True:
        bukva = input("\nвведите букву ")
        if bukva in uslet or len(bukva)>1:
            print("\nмнога букаф")
            print("Уже были буквы: ",uslet)
        else:
            uslet+=bukva
            break
    count=0
    for i in slovo:
        if bukva in i:
            dlina -= 1
            proverka=True
            itogslovo[count]=bukva
        count+=1
 
 
 
    if proverka != True:
        zdorovie -= 1
        print("Неверно")
    else:
        print("Верно")
        print(itogslovo)
 
    print("Ваше здоровье = ", zdorovie)
 
if(dlina == 0):
    print("\nура победа, слово:", slovo)
else:
    print("\nура непобеда")
