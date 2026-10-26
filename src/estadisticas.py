
# ==========================================
# ESTADÍSTICAS
# ==========================================

import unicodedata


def normalizar_continente(nombre):
    """
    Normaliza el nombre de un continente para
    evitar diferencias de tildes, mayúsculas
    y espacios durante el conteo.
    """
    nombre = " ".join(nombre.strip().split())

    nombre = "".join(
        caracter
        for caracter in unicodedata.normalize("NFD", nombre)
        if unicodedata.category(caracter) != "Mn"
    ).casefold()

    continentes_validos = {
        "america del sur": "América del Sur",
        "america del norte": "América del Norte",
        "america central": "América Central",
        "europa": "Europa",
        "asia": "Asia",
        "africa": "África",
        "oceania": "Oceanía",
        "antartida": "Antártida"
    }

    return continentes_validos.get(
        nombre,
        nombre.capitalize()
    )


def mostrar_estadisticas(paises):
    """
    Calcula y muestra estadísticas generales
    del dataset de países.

    Indicadores:
        - País con mayor y menor población.
        - Promedio de población y superficie.
        - Cantidad de países por continente.

    Parámetros:
        paises (list): Lista de diccionarios
        con los datos de cada país.

    Retorna:
        None. Muestra los resultados por consola.
    """

    if not paises:
        print("No hay datos cargados para calcular estadísticas.")
        return

    # Países con mayor y menor población
    mayor = max(paises, key=lambda p: p["poblacion"])
    menor = min(paises, key=lambda p: p["poblacion"])

    # Cálculo de promedios
    promedio_poblacion = (
        sum(p["poblacion"] for p in paises) / len(paises)
    )

    promedio_superficie = (
        sum(p["superficie"] for p in paises) / len(paises)
    )

    # Conteo de países por continente
    continentes = {}

    for pais in paises:
        continente = normalizar_continente(
            pais["continente"]
        )

        if continente in continentes:
            continentes[continente] += 1
        else:
            continentes[continente] = 1

    # Presentación de resultados
    print("\n========== ESTADÍSTICAS ==========")

    print(
        f"\nPaís con mayor población: "
        f"{mayor['nombre']} ({mayor['poblacion']:,} hab.)"
    )

    print(
        f"País con menor población: "
        f"{menor['nombre']} ({menor['poblacion']:,} hab.)"
    )

    print(
        f"\nPromedio de población:  "
        f"{promedio_poblacion:>15,.2f} hab."
    )

    print(
        f"Promedio de superficie: "
        f"{promedio_superficie:>15,.2f} km²"
    )

    print("\nCantidad de países por continente:")
    print("-" * 35)

    for continente, cantidad in sorted(continentes.items()):
        print(f"  {continente:<25} {cantidad} país/es")

    print("=" * 35)
