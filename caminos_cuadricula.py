"""
Práctica 12 – Estrategias para la construcción de algoritmos II
Módulo  : Parte 2 – Contando caminos en una cuadrícula
"""

import time


def medir(funcion, *args, repeticiones: int = 5):

    tiempos = []
    resultado = None

    for _ in range(repeticiones):
        inicio = time.perf_counter()
        resultado = funcion(*args)
        fin = time.perf_counter()

        tiempos.append(fin - inicio)

    return resultado, sum(tiempos) / len(tiempos)


# ============================================================
# CAMINOS SIN OBSTÁCULOS
# ============================================================

def caminos_recursivo(m: int, n: int) -> int:

    if m == 1 or n == 1:
        return 1

    return caminos_recursivo(m - 1, n) + caminos_recursivo(m, n - 1)


def caminos_memo(m: int, n: int, memo: dict = None) -> int:

    if memo is None:
        memo = {}

    if m == 1 or n == 1:
        return 1

    if (m, n) in memo:
        return memo[(m, n)]

    memo[(m, n)] = caminos_memo(m - 1, n, memo) + caminos_memo(m, n - 1, memo)

    return memo[(m, n)]


def caminos_bottom_up(m: int, n: int) -> tuple:

    tabla = [[0] * n for _ in range(m)]

    for j in range(n):
        tabla[0][j] = 1

    for i in range(m):
        tabla[i][0] = 1

    for i in range(1, m):
        for j in range(1, n):

            tabla[i][j] = tabla[i - 1][j] + tabla[i][j - 1]

    return tabla[m - 1][n - 1], tabla


def imprimir_tabla(tabla: list, titulo: str = "Tabla DP") -> None:

    max_val = max(max(fila) for fila in tabla)

    ancho = len(str(max_val)) + 1

    print(titulo + ":")

    for fila in tabla:
        print(" ".join(str(val).rjust(ancho) for val in fila))


# ============================================================
# CAMINOS CON OBSTÁCULOS
# ============================================================

def caminos_con_obstaculos(grid: list) -> int:

    m = len(grid)
    n = len(grid[0])

    if grid[0][0] == 1 or grid[m - 1][n - 1] == 1:
        return 0

    tabla = [[0] * n for _ in range(m)]

    for j in range(n):

        if grid[0][j] == 1:
            break

        tabla[0][j] = 1

    for i in range(m):

        if grid[i][0] == 1:
            break

        tabla[i][0] = 1

    for i in range(1, m):
        for j in range(1, n):

            if grid[i][j] == 1:
                tabla[i][j] = 0
            else:
                tabla[i][j] = tabla[i - 1][j] + tabla[i][j - 1]

    return tabla[m - 1][n - 1]


# ============================================================
# EXPERIMENTOS
# ============================================================

if __name__ == "__main__":

    print("=== Verificación de correctitud ===")

    casos = [
        (1, 1, 1),
        (2, 2, 2),
        (3, 3, 6),
        (3, 7, 28),
        (4, 4, 20)
    ]

    for m, n, esperado in casos:

        r = caminos_recursivo(m, n)
        memo_r = caminos_memo(m, n)
        bu = caminos_bottom_up(m, n)[0]

        print(f"caminos({m}x{n}) = {esperado}")

    print("\n=== Tabla DP para cuadrícula 5x5 ===")

    total, tabla = caminos_bottom_up(5, 5)

    imprimir_tabla(tabla, "Caminos 5x5")

    print(f"Caminos totales: {total}")

    print("\n=== Comparación de tiempos ===")

    print(f"{'cuadrícula':>12}  {'recursivo (s)':>16}  {'memo (s)':>12}  {'bottom_up (s)':>14}")

    for dim in [5, 10, 12, 15]:

        _, t_r = medir(caminos_recursivo, dim, dim)
        _, t_m = medir(caminos_memo, dim, dim)

        bu_fn = lambda d=dim: caminos_bottom_up(d, d)

        _, t_b = medir(bu_fn)

        print(f"{dim:3d}x{dim:<3d}  {t_r:16.8f}  {t_m:12.8f}  {t_b:14.8f}")

    print("\n=== Cuadrícula con obstáculos ===")

    grid_ejemplo = [
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 0, 0],
    ]

    for fila in grid_ejemplo:
        print(fila)

    resultado_obs = caminos_con_obstaculos(grid_ejemplo)

    print(f"Caminos evitando obstáculos: {resultado_obs}")
