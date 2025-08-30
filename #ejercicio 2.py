#Desarrolle una calculadora básica usando funciones, en la cual ingresen 2 números enteros y el
#tipo de operación a realizar en string. Como resultado la calculadora debe arrojar la operación
#deseada entre los 2 números.
def suma (x,y):
    return x + y
def resta (x,y):
    return x - y
def multiplicacion (x,y):
    return x * y
def division (x,y):
    if y == 0:
        return "Error matemático, no se puede dividir por 0"
    return x / y
def modulo (x,y):
    return x % y
def calculadora (x, y, Op):
    if Op == "Suma":
        return suma (x,y)
    elif Op == "Resta":
        return resta (x,y)
    elif Op == "Multiplicacion":
        return multiplicacion (x,y)
    elif Op == "Division":
        return division (x,y)
    elif Op == "Modulo":
        return modulo (x,y)
    else:
        return "Operacion no valida"
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
Op = input("Ingrese la operación a realizar (Suma, Resta, Multiplicacion, Division, Modulo): ").lower().capitalize()
result = calculadora (num1, num2, Op)
print("El resultado de su operación es = ", result)