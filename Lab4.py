def Zad1():
    moja_lista=[1, 17, 3, 5, 3, 4, 86, 90, 2, 21]
    print(moja_lista[0])
    print(moja_lista[-1])
    print(len(moja_lista))
    print(max(moja_lista))
    print(min(moja_lista))
    print(sum(moja_lista))
    print(sorted(moja_lista))
    print(moja_lista.append(6))
    print(moja_lista.insert(3,8))
    print(moja_lista.pop())
    print(moja_lista.reverse())
    print(moja_lista+moja_lista)
    lista=moja_lista*5
    print(lista)
    print(moja_lista[:3], moja_lista[3:], moja_lista[3:10:2], moja_lista[::-1])

def Zad2():
    imie=["Paweł", "Szymon", "Oskar", "Mateusz"]
    print(sorted(imie))
    imie.append("Adrian")
    imie.append("Maciek")
    print(imie.pop())
    imie.insert(3,"Anna")
    print(imie[::-1]*2)

def Zad3():
    imie=input("Imie: ")
    wiek=input("Wiek: ")
    nazwisko=input("Nazwisko: ")
    print(f"Witaj {imie}")
    print(f"Twój wiek to: {wiek}")
    print(imie[0],nazwisko[0])
    x=input("Podaj tekst: ")
    print(x*5)
    a=input("Podaj łańcuch: ")
    b=input("Podaj drugi łańcuch: ")
    c=a+b
    print(c)
    d=input("Podaj łańcuch: ")
    e=input("Podaj drugi łańcuch: ")
    pd=int(round((len(d)/2), 0))
    de=int(round((len(e)/2), 0))
    print(d[:pd], e[de:])

def Zad4():
    zdanie=str(input("Zdanie: "))
    print(sorted(zdanie.lower()))
    alfabet=["a", "ą" , "b", "c", "ć", "d", "e", "ę", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "ó", "p", "r", "s", "ś", "t", "u", "v", "w", "x", "y", "z", "ż", "ź"]
    print(sorted(str(alfabet)-zdanie))

def Zad5():
    dni=("Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela")
    print(dni)

def Zad6():
    owoce=("jabłko", "banan", "gruszka", "banan", "banan", "malina")
    print(owoce.count("banan"))

def Zad7():
    moja_krotka=(10,2,6,6,9,13,0,1)
    lista=moja_krotka
    print(sorted(lista))

def Zad8():
    stopnie=("Szeregowy", "Kapral", "Sierżancie", "Porucznik", "Kapitan", "Major", "Pułkownik")
    ilość_stopni=len(stopnie)
    print(ilość_stopni)
    s=str(stopnie)
    Major_index=stopnie.index("Major")
    print(Major_index)
    Pułkownik_wystepowanie=s.find("Pułkownik")
    if Pułkownik_wystepowanie>0:
        print("Pułkownik występuje w krotce")
    else:
        print("Pułkownik nie występuje w krotce")

def Zad9():
    lista_zakupów={"chleb":3, "Mleko":2, "Jajka":12, "Kawa":28, "Czekolada":9}
    suma=sum(lista_zakupów.values())
    print(lista_zakupów)
    print(f"Wydatki: {suma}")

#Zad1()
#Zad2()
#Zad3()
#Zad4()
#Zad5()
#Zad6()
#Zad7()
#Zad8()
#Zad9()






