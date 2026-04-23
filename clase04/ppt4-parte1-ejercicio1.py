

def numero_triangular(num) :

    triangulo = 0
    for i in range(1, num+1) :
        triangulo += i
        print(f"{i} - {triangulo}")

numero_triangular(5)