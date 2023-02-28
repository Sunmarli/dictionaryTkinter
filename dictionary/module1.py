

def loe_failist(file:str)->list:
    fail=open(file,'r',encoding="utf-8-sig")
    mas=[]
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas

def lisamine(mas:list,file:str):
    f=open(file,'w',encoding="utf-8-sig")
    for item in mas:
        f.write(item+"\n")
    f.close()

def element_listisse(eng:list,rus:list):
    en=input("English: ")
    eng.append(en)
    ru=input("Russian: ")
    rus.append(ru)
    return eng,rus

def kustuta(nimi:str,p:list,i:list):
    n=i.count(nimi)
    pos=0
    for j in range(n):
        ind=i.index(nimi,pos)
        pos=ind
        i.remove(nimi)
        p.pop(ind)
    return p,i
def connect(eng:list,rus:list):
    zipped=zip(eng,rus)
    print(list(zipped))

def eng_to_rus(eng:list,rus:list):
    n=str(input("Write the word:-- ")) 
    if n in eng:
        ind=eng.index(n) 
        print(f"{n}-- {rus[ind]}") 
        print("If you feel its wrong to make shanges print 1") 
        v=int(input())
        if v==1:
            ch=input("If wrong write right---") 
            rus[ind]=ch
            print(eng) 
            print(rus) 
            lisamine(rus,"rus.txt") 
        else:
            print("Bye")
    else:
        print("No such word, please add...")
        eng,rus=element_listisse(eng,rus) 
        print(eng) 
        print(rus)
        lisamine(eng,"eng.txt") 
        lisamine(rus,"rus.txt")


def rus_to_eng(eng:list,rus:list):
    n=str(input("Ваше слово:-- ")) 
    if n in rus:
        ind=rus.index(n) 
        print(f"{n}-- {eng[ind]}") 
        print("Если хотите исправить напишите  1") 
        v=int(input())
        if v==1:
            ch=input("Напишите правильно ---") 
            eng[ind]=ch
            print(eng) 
            print(rus) 
            lisamine(eng,"eng.txt") 
        else:
            print("Пока")
    else:
        print("Нет такого слова, добавить...")
        eng,rus=element_listisse(eng,rus) 
        print(eng) 
        print(rus)
        lisamine(eng,"eng.txt") 
        lisamine(rus,"rus.txt") 

def kontroll(eng,rus):
    import random 
    oige=0
    for i in range (5):
        n=random.choice(eng) 
        print(n) 
        ind=eng.index(n)
        v=input("ответ:") 
        if v in rus and v==rus[ind]:
            print("Правильно!") 
            print(f"Правильное слово -- {rus[ind]}\n") 
            oige=oige+1
        else:
            
            print("не Правильно!\n") 
            
    print("Teie tulemus ", oige /5)

     