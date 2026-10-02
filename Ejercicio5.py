try:
    numero1 = float(input("Ingresá el primer numero: "))
    numero2 = float(input("Ingresá el segundo numero: "))
    resultado = numero1 / numero2
    print(f"El resultado es: {resultado}")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
except ValueError:
    print("Error: Tenes que ingresar un numero valido.")



