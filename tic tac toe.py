import random
a00 = a01 = a02 = a10 = a11 = a12 = a20 = a21 = a22 = "-"
print(f" 012\n0"+a00+a01+a02+"\n1"+a10+a11+a12+"\n2"+a20+a21+a22)
d=0
s2=0
while d==0:
    while s2==0:
        a=int(input("Введите номер строки для крестика: "))
        b=int(input("Введите номер столбца для крестика: "))
        if a == 0:
            if b == 0:
                if a00 == "x" or a00 == "o":
                    print("Клетка уже занята")
                else:
                    a00 = "x"
                    s2 = 1
            elif b == 1:
                if a01 == "x" or a01 == "o":
                    print("Клетка уже занята")
                else:
                    a01 = "x"
                    s2 = 1
            elif b == 2:
                if a02 == "x" or a02 == "o":
                    print("Клетка уже занята")
                else:
                    a02 = "x"
                    s2 = 1
        elif a == 1:
            if b == 0:
                if a10 == "x" or a10 == "o":
                    print("Клетка уже занята")
                else:
                    a10 = "x"
                    s2 = 1
            elif b == 1:
                if a11 == "x" or a11 == "o":
                    print("Клетка уже занята")
                else:
                    a11 = "x"
                    s2 = 1
            elif b == 2:
                if a12 == "x" or a12 == "o":
                    print("Клетка уже занята")
                else:
                    a12 = "x"
                    s2 = 1
        elif a == 2:
            if b == 0:
                if a20 == "x" or a20 == "o":
                    print("Клетка уже занята")
                else:
                    a20 = "x"
                    s2 = 1
            elif b == 1:
                if a21 == "x" or a21 == "o":
                    print("Клетка уже занята")
                else:
                    a21 = "x"
                    s2 = 1
            elif b == 2:
                if a22 == "x" or a22 == "o":
                    print("Клетка уже занята")
                else:
                    a22 = "x"
                    s2 = 1
    print(f" 012\n0" + a00 + a01 + a02 + "\n1" + a10 + a11 + a12 + "\n2" + a20 + a21 + a22)
    if a00==a01==a02=="x"or a10==a11==a12=="x" or a20==a21==a22=="x":
        d=1
    if a00==a10==a20=="x"or a01==a11==a21=="x" or a02==a12==a22=="x":
        d=1
    if a00==a11==a22=="x" or a02==a11==a20=="x":
        d=1
    if d==1:
        print ("Крестики выиграли")
        exit()
    s1 = 0
    while s1 ==0:
        i=random.randrange(0,3,1)
        j = random.randrange(0, 3, 1)
        if a00 != "-" and a01 != "-" and a02 != "-" and a10 != "-" and a11 != "-" and a12 != "-" and a20 != "-" and a21 != "-" and a22 != "-":
            print("Ничья")
            exit()
        if i == 0:
            if j == 0:
                if a00 == "o" or a00 == "x":
                    print("Клетка уже занята")
                else:
                    a00 = "o"
                    s1 = 1
            elif j == 1:
                if a01 == "o" or a01 == "x":
                    print("Клетка уже занята")
                else:
                    a01 = "o"
                    s1 = 1
            elif j == 2:
                if a02 == "o" or a02 == "x":
                    print("Клетка уже занята")
                else:
                    a02 = "o"
                    s1 = 1
        elif i == 1:
            if j == 0:
                if a10 == "o" or a10 == "x":
                    print("Клетка уже занята")
                else:
                    a10 = "o"
                    s1 = 1
            elif j == 1:
                if a11 == "o" or a11 == "x":
                    print("Клетка уже занята")
                else:
                    a11 = "o"
                    s1 = 1
            elif j == 2:
                if a12 == "o" or a12 == "x":
                    print("Клетка уже занята")
                else:
                    a12 = "o"
                    s1 = 1
        elif i == 2:
            if j == 0:
                if a20 == "o" or a20 == "x":
                    print("Клетка уже занята")
                else:
                    a20 = "o"
                    s1 = 1
            elif j == 1:
                if a21 == "o" or a21 == "x":
                    print("Клетка уже занята")
                else:
                    a21 = "o"
                    s1 = 1
            elif j == 2:
                if a22 == "o" or a22 == "x":
                    print("Клетка уже занята")
                else:
                    a22 = "o"
                    s1 = 1
    print(f" 012\n0" + a00 + a01 + a02 + "\n1" + a10 + a11 + a12 + "\n2" + a20 + a21 + a22)
    if a00==a01==a02=="o"or a10==a11==a12=="o" or a20==a21==a22=="o":
        d=-1
    if a00==a10==a20=="o"or a01==a11==a21=="o" or a02==a12==a22=="o":
        d=-1
    if a00==a11==a22=="o" or a02==a11==a20=="o":
        d=-1
    if d==-1:
        print("Нолики выиграли")
        exit()
    s2 = 0