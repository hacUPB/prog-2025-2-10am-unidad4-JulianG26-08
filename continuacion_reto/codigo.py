

Te_inicial = float(input("Ingrese la temperatura inicial (°C): "))
tiempo_vuelo = float(input("Ingrese el tiempo de vuelo (minutos): "))
valores = {
    "Te_min": 30,
    "Te_max": 80,
    "intervalo_1": 10,
    "tiempo_estabilizacion": 5,
    "intervalo_2": 2
}

Te_actual = Te_inicial

print("1. Boeing 747-8 (k = 5)")
print("2. Airbus A380-800 (k = 8)")
print("3. Antonov An-225 (k = 10)")

opcion = int(input("Seleccione el avión: "))

match opcion:
    case 1:
        print("1. Boeing 747-8 (k = 5)")
        k = 5
    case 2:
        print("2. Airbus A380-800 (k = 8)")
        k = 8
    case 3:
        print("3. Antonov An-225 (k = 10)")
        k = 10
    case _:
        print("Opción no válida")


tiempo_inicio_estabilizacion = tiempo_vuelo - valores["tiempo_estabilizacion"]
tiempo_actual = 0
temp = []
while tiempo_actual < tiempo_vuelo:
    tiempo_actual += valores["intervalo_1"]

    dT_dt = -k * (Te_actual - Te_inicial)
    Te_nueva = Te_actual + (dT_dt * (valores["intervalo_1"] / 60))
    Te_actual = Te_nueva

    if tiempo_actual < tiempo_inicio_estabilizacion:
        if (int(tiempo_actual / valores["intervalo_1"])) % 2 == 0:
            Te_actual += 5
        else:
            Te_actual -= 5

    if Te_actual < valores["Te_max"]:
        print("La temperatura del LG es menor que la temperatura máxima, verificar si es menor que la mínima")
        if Te_actual < valores["Te_min"]:
            print("Cuidado: temperatura muy fría")
            Te_actual += (-k * (Te_actual - Te_inicial)) * (valores["intervalo_2"] / 60)
        else:
            print("Temperatura en rango ideal")
    else:
        print("temperatura muy caliente")
        Te_actual -= (-k * (Te_actual - Te_inicial)) * (valores["intervalo_2"] / 60)

    if tiempo_actual >= tiempo_inicio_estabilizacion:
        print("Fase de estabilización, asegurar para aterrizar")
    else:
        print("No iniciar fase de estabilización, seguir monitoreando.")
    
    temp.append(Te_actual)

    print(f"Temperatura actual: {Te_actual:.2f} °C")

print (temp)

valor_maximo = max(temp)
print(f"Temperatura Máxima: {valor_maximo:.2f} °C")
valor_minimo = min(temp)
print(f"Temperatura Mínima: {valor_minimo:.2f} °C")
promedio = sum(temp) / len(temp)
print(f"Temperatura Promedio: {promedio:.2f} °C")