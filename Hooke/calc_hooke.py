def calcular_fuerza(k, x):
    return k * x

def calcular_constante(F, x):
    return F / x

def calcular_elongacion(F, k):
    return F / k

def display_menu():
    print("\n" + "="*50)
    print("Bienvenido a la calculadora de Ley de Hooke")
    print("="*50)
    print("Eliga que quiere clcular")
    print("1.Fuerza")
    print("2.Elasticidad")
    print("3.Elongación")
    print("4.Exit")

def main():
    while True:
        display_menu()

        opcion = input("Opción: ").lower()

        if opcion == "1":
            k = float(input("Introduce la constante de elasticidad (N/m): "))
            x = float(input("Introduce la elongación (m): "))
            F = calcular_fuerza(k, x)
            print(f"La fuerza aplicada es: {F:.2f} N")
            
        elif opcion == "2":
            F = float(input("Introduce la fuerza aplicada (N): "))
            x = float(input("Introduce la elongación (m): "))
            k = calcular_constante(F, x)
            print(f"La constante de elasticidad es: {k:.2f} N/m")
            
        elif opcion == "3":
            F = float(input("Introduce la fuerza aplicada (N): "))
            k = float(input("Introduce la constante de elasticidad (N/m): "))
            x = calcular_elongacion(F, k)
            print(f"La elongación es: {x:.2f} m")
        
        elif opcion =="4":
          print("¡Muchas gracias por usar la calculadora de Ley de Hooke!")
          break

        
        continue_hooke = input("¿Desea continuar calculando?")
        if continue_hooke != 'y' and continue_hooke != 'yes':
            print("¡Muchas gracias por usar la calculadora de Ley de Hooke!")
            break       
    
        else:
            print("Opción no válida. Intenta con 'fuerza', 'constante' o 'elongacion'.")


if __name__ == "__main__":
    main()
