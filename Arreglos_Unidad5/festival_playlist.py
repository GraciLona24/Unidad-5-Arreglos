def agregar_canciones(nombres, artistas, duraciones, popularidades):
    cantidad = int(input("¿Cuántas canciones deseas agregar? "))

    for _ in range(cantidad):
        nombre = input("Nombre de la canción: ")
        artista = input("Artista: ")
        duracion = float(input("Duración (minutos): "))
        popularidad = int(input("Popularidad (1-100): "))

        nombres.append(nombre)
        artistas.append(artista)
        duraciones.append(duracion)
        popularidades.append(popularidad)

    print("Canciones registradas correctamente \n")


def ver_reportes(nombres, duraciones, popularidades):
    if not nombres:
        print("No hay canciones registradas todavía \n")
        return

    total = len(nombres)
    duracion_total = sum(duraciones)
    pop_max = max(popularidades)
    pop_min = min(popularidades)
    prom_pop = sum(popularidades) / total

    idx_max = popularidades.index(pop_max)
    idx_min = popularidades.index(pop_min)

    print("--- REPORTES ---")
    print(f"Número total de canciones: {total}")
    print(f"Duración total de la playlist: {duracion_total:.2f} min")
    print(f"Canción más popular: {nombres[idx_max]} ({pop_max})")
    print(f"Canción menos popular: {nombres[idx_min]} ({pop_min})")
    print(f"Promedio de popularidad: {prom_pop:.2f}\n")


def buscar_canciones(nombres, artistas, popularidades):
    if not nombres:
        print("No hay canciones registradas \n")
        return

    print("1. Buscar por artista")
    print("2. Buscar por rango de popularidad")
    op = input("Elige una opción: ")

    if op == "1":
        art = input("Ingresa el nombre del artista: ")
        print(f"\nResultados para artista '{art}':")
        encontrados = False
        for i in range(len(nombres)):
            if artistas[i].lower() == art.lower():
                print(f"- {nombres[i]} (Popularidad: {popularidades[i]})")
                encontrados = True
        if not encontrados:
            print("No se encontraron canciones de ese artista \n")

    elif op == "2":
        minimo = int(input("Popularidad mínima: "))
        maximo = int(input("Popularidad máxima: "))
        print(f"\nCanciones con popularidad entre {minimo} y {maximo}:")
        encontrados = False
        for i in range(len(nombres)):
            if minimo <= popularidades[i] <= maximo:
                print(f"- {nombres[i]} ({popularidades[i]})")
                encontrados = True
        if not encontrados:
            print("No hay canciones en ese rango \n")

    else:
        print("Opción inválida \n")


def playlist_recomendada(nombres, duraciones, popularidades):
    if not nombres:
        print("No hay canciones registradas \n")
        return

    promedio = sum(popularidades) / len(popularidades)
    print(f"\n--- PLAYLIST RECOMENDADA (Popularidad > {promedio:.2f}) ---")

    recomendadas = False
    for i in range(len(nombres)):
        if popularidades[i] > promedio:
            print(f"- {nombres[i]} ({popularidades[i]}) - {duraciones[i]} min")
            recomendadas = True

    if not recomendadas:
        print("No hay canciones que superen el promedio de popularidad \n")


def main():
    nombres = []
    artistas = []
    duraciones = []
    popularidades = []

    while True:
        print("===== MENU PRINCIPAL =====")
        print("1. Agregar canciones")
        print("2. Ver reportes")
        print("3. Buscar canciones")
        print("4. Playlist recomendada")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            agregar_canciones(nombres, artistas, duraciones, popularidades)
        elif opcion == "2":
            ver_reportes(nombres, duraciones, popularidades)
        elif opcion == "3":
            buscar_canciones(nombres, artistas, popularidades)
        elif opcion == "4":
            playlist_recomendada(nombres, duraciones, popularidades)
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Inténtalo de nuevo \n")


if __name__ == "__main__":
    main()
