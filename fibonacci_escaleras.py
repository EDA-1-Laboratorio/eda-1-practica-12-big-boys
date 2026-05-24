"""
Práctica 12 – Estrategias para la construcción de algoritmos II
Módulo  : Parte 1 – Fibonacci y Escalando Peldaños

Instrucciones generales
    Implementa cada función en el orden en que aparece.
    Cada bloque de comentarios guiados te explica CÓMO pensar el problema,
    no solo qué hacer. Léelos con cuidado antes de escribir código.
    Elimina los 'pass' conforme vayas completando cada función.

Ejecuta este archivo directamente para ver los resultados:
    python3 fibonacci_escaleras.py
"""

import time


# ============================================================
# UTILIDAD DE MEDICIÓN (ya implementada — no modificar)
# ============================================================

def medir(funcion, *args, repeticiones: int = 5):
    """
    Ejecuta funcion(*args) 'repeticiones' veces.
    Retorna (resultado, tiempo_promedio_en_segundos).
    """
    tiempos = []
    resultado = None
    for _ in range(repeticiones):
        inicio = time.perf_counter()
        resultado = funcion(*args)
        fin = time.perf_counter()
        tiempos.append(fin - inicio)
    return resultado, sum(tiempos) / len(tiempos)


# ============================================================
# PARTE 1A – TRES VERSIONES DE FIBONACCI
# ============================================================

def fib_recursivo(n: int) -> int:
    """
    Calcula F(n) usando recursión directa.
    """

    # PASO 1 – Validación de entrada.
    if n < 0:
        raise ValueError("n debe ser >= 0")

    # PASO 2 – Casos base.
    if n == 0:
        return 0

    if n == 1:
        return 1

    # PASO 3 – Caso recursivo.
    return fib_recursivo(n - 1) + fib_recursivo(n - 2)


def fib_memo(n: int, memo: dict = None) -> int:
    """
    Calcula F(n) con recursión + memoización (top-down).
    """

    # PASO 1 – Inicialización del diccionario.
    if memo is None:
        memo = {}

    # PASO 2 – Validación de n.
    if n < 0:
        raise ValueError("n debe ser >= 0")

    # PASO 3 – Casos base.
    if n == 0:
        return 0

    if n == 1:
        return 1

    # PASO 4 – Revisión de caché.
    if n in memo:
        return memo[n]

    # PASO 5 – Caso recursivo con guardado.
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)

    return memo[n]


def fib_bottom_up(n: int) -> int:
    """
    Calcula F(n) con tabulación iterativa (bottom-up).
    """

    # PASO 1 – Validación de n.
    if n < 0:
        raise ValueError("n debe ser >= 0")

    # PASO 2 – Casos base especiales.
    if n == 0:
        return 0

    if n == 1:
        return 1

    # PASO 3 – Crea la tabla.
    tabla = [0] * (n + 1)

    # PASO 4 – Inicializa los casos base.
    tabla[0] = 0
    tabla[1] = 1

    # PASO 5 – Bucle de llenado.
    for i in range(2, n + 1):
        tabla[i] = tabla[i - 1] + tabla[i - 2]

    # PASO 6 – Devuelve tabla[n].
    return tabla[n]


# ============================================================
# PARTE 1B – ESCALANDO PELDAÑOS
# ============================================================

def escaleras_recursivo(n: int) -> int:
    """
    Cuenta las formas de subir n peldaños (1 o 2 a la vez) — versión recursiva.
    """

    # PASO 1 – Validación.
    if n < 0:
        raise ValueError("n debe ser >= 0")

    # PASO 2 – Casos base.
    if n == 0:
        return 1

    if n == 1:
        return 1

    if n == 2:
        return 2

    # PASO 3 – Caso recursivo.
    return escaleras_recursivo(n - 1) + escaleras_recursivo(n - 2)


def escaleras_memo(n: int, memo: dict = None) -> int:
    """
    Cuenta las formas de subir n peldaños — versión con memoización.
    """

    # Inicializa memo.
    if memo is None:
        memo = {}

    # Validación.
    if n < 0:
        raise ValueError("n debe ser >= 0")

    # Casos base.
    if n == 0:
        return 1

    if n == 1:
        return 1

    if n == 2:
        return 2

    # Revisión de caché.
    if n in memo:
        return memo[n]

    # Caso recursivo con guardado.
    memo[n] = escaleras_memo(n - 1, memo) + escaleras_memo(n - 2, memo)

    return memo[n]


def escaleras_bottom_up(n: int) -> int:
    """
    Cuenta las formas de subir n peldaños — versión tabulación iterativa.
    """

    # Validación.
    if n < 0:
        raise ValueError("n debe ser >= 0")

    # Casos base.
    if n == 0:
        return 1

    if n == 1:
        return 1

    if n == 2:
        return 2

    # Tabla.
    tabla = [0] * (n + 1)

    # Inicialización.
    tabla[0] = 1
    tabla[1] = 1
    tabla[2] = 2

    # Llenado.
    for i in range(3, n + 1):
        tabla[i] = tabla[i - 1] + tabla[i - 2]

    # Resultado.
    return tabla[n]


# ============================================================
# EXPERIMENTOS — ejecuta este bloque para ver resultados
# ============================================================

if __name__ == "__main__":

    # --- Verificación de correctitud ---
    esperados_fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    print("=== Verificación Fibonacci ===")
    for i, esperado in enumerate(esperados_fib):
        r = fib_recursivo(i)
        m = fib_memo(i)
        b = fib_bottom_up(i)
        ok_r = "✓" if r == esperado else f"✗(esperado {esperado}, obtuvo {r})"
        ok_m = "✓" if m == esperado else f"✗(esperado {esperado}, obtuvo {m})"
        ok_b = "✓" if b == esperado else f"✗(esperado {esperado}, obtuvo {b})"
        print(f"  F({i:2d}) = {esperado:4d}  recursivo:{ok_r}  memo:{ok_m}  bottom_up:{ok_b}")

    esperados_esc = [1, 1, 2, 3, 5, 8, 13, 21]
    print("\n=== Verificación Escaleras ===")
    for i, esperado in enumerate(esperados_esc):
        r = escaleras_recursivo(i)
        m = escaleras_memo(i)
        b = escaleras_bottom_up(i)
        ok_r = "✓" if r == esperado else f"✗(esperado {esperado}, obtuvo {r})"
        ok_m = "✓" if m == esperado else f"✗(esperado {esperado}, obtuvo {m})"
        ok_b = "✓" if b == esperado else f"✗(esperado {esperado}, obtuvo {b})"
        print(f"  esc({i}) = {esperado:4d}  recursivo:{ok_r}  memo:{ok_m}  bottom_up:{ok_b}")

    # --- Experimento de tiempo ---
    print("\n=== Comparación de tiempos: Fibonacci ===")
    print(f"{'n':>5}  {'recursivo (s)':>16}  {'memo (s)':>12}  {'bottom_up (s)':>14}")
    for n in [10, 20, 25, 30, 35]:
        _, t_r = medir(fib_recursivo, n)
        _, t_m = medir(fib_memo, n)
        _, t_b = medir(fib_bottom_up, n)
        print(f"  {n:3d}  {t_r:16.8f}  {t_m:12.8f}  {t_b:14.8f}")

    # --- Reflexión ---
    print("\n=== Escaleras vs Fibonacci ===")
    for n in range(1, 10):
        fib_n1 = fib_bottom_up(n + 1)
        esc_n  = escaleras_bottom_up(n)
        print(f"  escaleras({n}) = {esc_n:4d}   fib({n+1}) = {fib_n1:4d}  "
              f"{'¿iguales?' if esc_n == fib_n1 else 'DISTINTOS'}")
