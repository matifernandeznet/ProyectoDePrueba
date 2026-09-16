print("=== CALCULADORA BÁSICA ===")

numero1 = float(input("Ingresa el primer número: "))
operacion = input("Ingresa la operación (+, -, *, /): ")
numero2 = float(input("Ingresa el segundo número: "))

if operacion == "+":
    resultado = numero1 + numero2

elif operacion == "-":
    resultado = numero1 - numero2

elif operacion == "*":
    resultado = numero1 * numero2

elif operacion == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        resultado = "Error: no se puede dividir por cero"

else:
    resultado = "Error: operación no válida"

print("Resultado:", resultado)