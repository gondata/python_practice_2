

n=0
n
n += 1
n -= 1
n /= 2
n *= 2
n **= 2

1+1 == 3
1+1 == 2
c = 5
c
c >= 3
c >= 9
c <= 9
c <= 2

# Ingreso de datos (input)

decimal = float(input("Introduce un valor decimal:"))
decimal


valores = []
print("Introduce valores")
for x in range(3):
    valores.append(input("Introduce 3 valores: "))

print(valores)
valores

# Funciones

def tabla_del_5():
    for i in range(11):
        print("5 *", i, "=", i*5)
tabla_del_5()

def test():
    n = 5
    print(5)
test()

n = 10
test()
print(n)

# Funciones con parámetros (a, b)

def suma(a, b):
    return(a + b)

r = suma(7, 8)
r

# Funciones iterativas

def cuenta_atras(num):
    num -= 1
    if num > 0:
        print(num)
        cuenta_atras(num)  #Vuelvo atrás (recursión)
    else:
        print("Hasta aquí")

    print("Fin de función", num)

cuenta_atras(6)

# La función se cierra en orden inverso. ""Fin de función 0"" se cierra con "Hasta aquí" , ""Fin de función 1"" se cierra con "1" y así sucesivamente
# Es como un árbol que se va ramificando y se va cerrando en orden inverso en el cuál fue abierto