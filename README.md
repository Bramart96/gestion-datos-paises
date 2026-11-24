# Gestión y análisis de países | Python

Desarrollé una aplicación de consola para administrar un conjunto de países almacenado en CSV. Organicé las operaciones en módulos específicos para facilitar la lectura, las validaciones y la persistencia de datos.

## Funcionalidades implementadas

- Alta y actualización de países en `data/paises.csv`.
- Búsqueda por nombre y filtros por continente, población y superficie.
- Ordenamiento por nombre, población y superficie.
- Estadísticas calculadas a partir de los registros.
- Validaciones para evitar nombres numéricos y valores de población o superficie no positivos.
- Normalización de entradas de texto con distintas mayúsculas, tildes y separadores numéricos.

El menú permite navegar entre estas funciones sin modificar manualmente el CSV.

## Estructura

```text
src/main.py            Menú principal y navegación
src/datos.py           Lectura, escritura y visualización CSV
src/validaciones.py    Alta, actualización y validaciones
src/busqueda.py        Consultas por nombre
src/filtros.py         Filtros por continente, población y superficie
src/ordenamiento.py    Ordenamientos
src/estadisticas.py    Cálculos estadísticos
data/paises.csv        Dataset utilizado
INFORME_TPI.pdf        Informe técnico del integrador
```

## Ejecución

Utilicé **Python 3** y una estructura de módulos con importaciones desde `src`. Para ejecutarlo desde la raíz:

```bash
python -m src.main
```

## Ejemplo de uso

Registré países desde el menú usando entradas como `Peru`, `america del sur` y `34.000.000` habitantes. El sistema interpreta el formato numérico, normaliza el texto y guarda los datos en el archivo CSV.

## Autoría y contexto

Realicé este trabajo integrador de Programación I (UTN) junto con **Mateo Peralta**. Mi participación incluyó desarrollo principal, edición de código y revisión; Mateo colaboró con la documentación técnica, correcciones y optimización. Mantengo esa atribución porque el proyecto fue colaborativo.

[Video de explicación y demostración](https://youtu.be/qe8kJ0Rlx-E)
