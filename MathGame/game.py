from random import choice,randint
son_oraliq = int(input("son oraligini kiriting (10/100..) >>> ")) 

javoblar_soni = 0
savollar_soni = 0
upg_uchun = 12

while True:
    a = randint(1,son_oraliq+1)
    b = randint(1,son_oraliq+1)
    ishora = choice(["+","-","*"])
    javob = 0
    savollar_soni+=1
    upg_uchun +=1

    if ishora == "+":
        javob = a+b
    elif ishora == "-":
        javob = a-b
    elif ishora == "*":
        javob = a*b
    
    res = int(input(f"{a} {ishora} {b} = ? "))

    if upg_uchun > 15:
        upg = input("Misollarni kuchaytiramiz? (ha/yoq)")
        if upg == "ha":
            upg_uchun = 0
            son_oraliq = son_oraliq * 10
            print(f"Misollar endi {son_oraliq}0 sonlari oraligida beriladi")
        else:
            upg_uchun = 0
            print(f"tushunarli, {son_oraliq} sonlari oraligida davom etamiz")

    if res == javob:
        print(f"{res} tog'ri javob!")
        javoblar_soni +=1
    else:
        print(f"{res} notog'ri javob! tog'ri javob: {javob}")
        print(f"siz {savollar_soni} ta savoldan {javoblar_soni} tasiga togri javob berdingiz {round(javoblar_soni*100/savollar_soni)}%")
        
        running = input("qaytadan boshlaymizmi? (ha/yoq)")
        if running == "ha":
            savollar_soni = 0
            javoblar_soni = 0
            print("Ishlashda davom etamiz, Omad!")
        else:
            print("Dastur toxtadi!")
            break