try:
    numero1 = float(input("Ingrese el primer numero: "))
    numero2 = float(input("Ingrese el segundo numero: "))
    resultado = numero1 / numero2
    print(f"Resultado: {resultado}")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")