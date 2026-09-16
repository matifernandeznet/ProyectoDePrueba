```python
def calculadora():
    while True:
        print("\n===== CALCULADORA =====")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Potencia")
        print("6. Módulo (resto)")
        print("7. Salir")

        opcion = input("\nElige una opción: ")

        if opcion == "7":
            print("\nCalculadora cerrada.")
            break

        if opcion not in ["1", "2", "3", "4", "5", "6"]:
            print("\n❌ Opción no válida.")
            continue

        try:
            numero1 = float(input("Ingresa el primer número: "))
            numero2 = float(input("Ingresa el segundo número: "))

            if opcion == "1":
                resultado = numero1 + numero2
                simbolo = "+"

            elif opcion == "2":
                resultado = numero1 - numero2
                simbolo = "-"

            elif opcion == "3":
                resultado = numero1 * numero2
                simbolo = "*"

            elif opcion == "4":
                if numero2 == 0:
                    print("\n❌ No se puede dividir por cero.")
                    continue

                resultado = numero1 / numero2
                simbolo = "/"

            elif opcion == "5":
                resultado = numero1 ** numero2
                simbolo = "**"

            elif opcion == "6":
                if numero2 == 0:
                    print("\n❌ No se puede calcular el módulo con cero.")
                    continue

                resultado = numero1 % numero2
                simbolo = "%"

            print(f"\nResultado: {numero1} {simbolo} {numero2} = {resultado}")

        except ValueError:
            print("\n❌ Error: debes ingresar números.")

        continuar = input("\nPresiona ENTER para continuar...")


calculadora()
```
