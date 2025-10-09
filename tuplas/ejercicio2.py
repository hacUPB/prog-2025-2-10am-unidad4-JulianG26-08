# Representando una flota de aeronaves con tuplas
# (modelo, envergadura (m), longitud (m), mtow (kg), velocidad_max (km/h))
fleet_data = [
    ("Airbus A320", 35.80, 37.57, 78000, 871),
    ("Boeing 737-800", 35.79, 39.47, 79010, 853),
    ("Embraer E190", 28.72, 36.24, 51800, 871),
    ("Bombardier CRJ-900", 24.85, 36.40, 38330, 870)
]

# Encontrar el avión con mayor envergadura (paso a paso)
print("=== Buscando el avión con mayor envergadura ===")

# Inicializamos variables para el seguimiento
avion_mayor_envergadura = None
mayor_envergadura_valor = 0

# Recorremos cada avión en la flota
for avion in fleet_data:
    # Extraemos los datos del avión actual
    modelo = avion[0]
    envergadura = avion[1]
    longitud = avion[2]
    mtow = avion[3]
    velocidad_max = avion[4]
    
    print(f"Revisando: {modelo} - Envergadura: {envergadura} m")
    
    # Comparamos si esta envergadura es mayor que la que teníamos guardada
    if envergadura > mayor_envergadura_valor:
        # Si es mayor, actualizamos nuestros valores
        mayor_envergadura_valor = envergadura
        avion_mayor_envergadura = avion
        print(f"  → Nuevo récord encontrado: {modelo}")
    else:
        print(f"  → No supera el récord actual")

# Mostramos el resultado
print(f"\nResultado: Avión con mayor envergadura: {avion_mayor_envergadura[0]} ({avion_mayor_envergadura[1]} m)")

print("\n" + "="*50)

# Calcular velocidad promedio de la flota (paso a paso)
print("=== Calculando velocidad promedio de la flota ===")

# Inicializamos variables para el cálculo
suma_velocidades = 0
contador_aviones = 0

# Recorremos cada avión para sumar las velocidades
for avion in fleet_data:
    # Extraemos el modelo y la velocidad del avión actual
    modelo = avion[0]
    velocidad = avion[4]
    
    print(f"Procesando: {modelo} - Velocidad: {velocidad} km/h")
    
    # Sumamos la velocidad al total
    suma_velocidades = suma_velocidades + velocidad
    contador_aviones = contador_aviones + 1
    
    print(f"  → Suma acumulada: {suma_velocidades} km/h")
    print(f"  → Aviones procesados: {contador_aviones}")

# Calculamos el promedio
velocidad_promedio = suma_velocidades / contador_aviones

# Mostramos el resultado
print(f"\nCálculo final:")
print(f"Suma total de velocidades: {suma_velocidades} km/h")
print(f"Número de aviones: {contador_aviones}")
print(f"Velocidad promedio de la flota: {velocidad_promedio:.2f} km/h")
