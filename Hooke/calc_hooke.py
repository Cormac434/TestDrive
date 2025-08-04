def calcular_fuerza(k, x):
    return k * x

def calcular_constante(F, x):
    return F / x

def calcular_elongacion(F, k):
    return F / k

def main():
    print("Calculadora de la Ley de Hooke")
    print("¿Qué parámetro deseas calcular? (fuerza, constante, elongacion)")
    opcion = input("Opción: ").lower()

    if opcion == "fuerza":
        k = float(input("Introduce la constante de elasticidad (N/m): "))
        x = float(input("Introduce la elongación (m): "))
        F = calcular_fuerza(k, x)
        print(f"La fuerza aplicada es: {F:.2f} N")
        
    elif opcion == "constante":
        F = float(input("Introduce la fuerza aplicada (N): "))
        x = float(input("Introduce la elongación (m): "))
        k = calcular_constante(F, x)
        print(f"La constante de elasticidad es: {k:.2f} N/m")
        
    elif opcion == "elongacion":
        F = float(input("Introduce la fuerza aplicada (N): "))
        k = float(input("Introduce la constante de elasticidad (N/m): "))
        x = calcular_elongacion(F, k)
        print(f"La elongación es: {x:.2f} m")
        
    else:
        print("Opción no válida. Intenta con 'fuerza', 'constante' o 'elongacion'.")

if __name__ == "__main__":
    main()
