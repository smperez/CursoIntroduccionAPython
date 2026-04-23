def multiplo_7(num) :

    for i in range(0, num+1, 7) :
        if i > 0 :
            print(i)

multiplo_7(int(input("Ingrese un numero: ")))