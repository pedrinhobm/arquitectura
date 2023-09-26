# item 1
// functions.c
#include <stdio.h>

void accumulate_elementwise(float *matrix, int n, float *result) {
    float sum = 0.0;
    for (int i = 0; i < n * n; i++) {
        sum += matrix[i];
    }
    *result = sum;
}

void accumulate_in_blocks2(float *matrix, int n, float *result) {
    float sum = 0.0;
    for (int i = 0; i < n * n; i += 2) {
        sum += matrix[i] + matrix[i + 1];
    }
    *result = sum;
}

void accumulate_in_blocks4(float *matrix, int n, float *result) {
    float sum = 0.0;
    for (int i = 0; i < n * n; i += 4) {
        sum += matrix[i] + matrix[i + 1] + matrix[i + 2] + matrix[i + 3];
    }
    *result = sum;
}

void accumulate_in_blocks8(float *matrix, int n, float *result) {
    float sum = 0.0;
    for (int i = 0; i < n * n; i += 8) {
        sum += matrix[i] + matrix[i + 1] + matrix[i + 2] + matrix[i + 3] +
               matrix[i + 4] + matrix[i + 5] + matrix[i + 6] + matrix[i + 7];
    }
    *result = sum;
}

# item 2
gcc -shared -o mylibrary.so functions.c

# item 3
import ctypes

# Cargar la biblioteca dinámica
mylibrary = ctypes.CDLL('./mylibrary.so')

# Definir tipos de argumentos y valores de retorno para las funciones de C
mylibrary.accumulate_elementwise.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.c_int, ctypes.POINTER(ctypes.c_float)]
mylibrary.accumulate_elementwise.restype = None

mylibrary.accumulate_in_blocks2.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.c_int, ctypes.POINTER(ctypes.c_float)]
mylibrary.accumulate_in_blocks2.restype = None

mylibrary.accumulate_in_blocks4.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.c_int, ctypes.POINTER(ctypes.c_float)]
mylibrary.accumulate_in_blocks4.restype = None

mylibrary.accumulate_in_blocks8.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.c_int, ctypes.POINTER(ctypes.c_float)]
mylibrary.accumulate_in_blocks8.restype = None

# Implementar la función que devuelve las cuatro funciones configuradas
def get_accumulation_functions():
    return (
        mylibrary.accumulate_elementwise,
        mylibrary.accumulate_in_blocks2,
        mylibrary.accumulate_in_blocks4,
        mylibrary.accumulate_in_blocks8,
    )

# Haz una instancia de las funciones
accumulation_functions = get_accumulation_functions()

# item 4
#: Prueba las funciones para el menor valor de ns
#Puedes probar las funciones con el menor valor de ns y la variable Y utilizando el siguiente código:
import numpy as np

n = ns[0]
A = np.random.rand(n, n)
Y = A.flatten()

# Prueba las funciones para el menor valor de ns
for func in accumulation_functions:
    result = ctypes.c_float()
    func(Y.ctypes.data_as(ctypes.POINTER(ctypes.c_float)), n, ctypes.byref(result))
    print(f"Resultado: {result.value}")

# item 5 : Prueba las funciones para el mayor valor de ns
# Ahora, realiza la misma prueba pero con el mayor valor de ns utilizando el siguiente código:
n = ns[-1]
A = np.random.rand(n, n)
Y = A.flatten()

# Prueba las funciones para el mayor valor de ns
for func in accumulation_functions:
    result = ctypes.c_float()
    func(Y.ctypes.data_as(ctypes.POINTER(ctypes.c_float)), n, ctypes.byref(result))
    print(f"Resultado: {result.value}")


# item 6
# Realiza 50 mediciones de tiempo
Para medir el tiempo de ejecución, puedes utilizar el módulo time de Python.
#A continuación, se muestra un ejemplo de cómo puedes hacerlo para 50 mediciones y calcular la mediana:

import time

# Función para medir el tiempo de ejecución de una función
def measure_time(func, Y, n):
    times = []
    for _ in range(50):
        start_time = time.time()
        result = ctypes.c_float()
        func(Y.ctypes.data_as(ctypes.POINTER(ctypes.c_float)), n, ctypes.byref(result))
        end_time = time.time()
        elapsed_time = end_time - start_time
        times.append(elapsed_time)
    return sorted(times)[25]  # Mediana de las 50 mediciones

# Medir el tiempo de ejecución para todas las funciones y todos los valores de ns
times = []
for n in ns:
    A = np.random.rand(n, n)
    Y = A.flatten()
    ns_time = []
    for func in accumulation_functions:
        execution_time = measure_time(func, Y, n)
        ns_time.append(execution_time)
    times.append(ns_time)

# 'times' contiene los tiempos de ejecución para cada función y valor de ns


# Paso 7: Presentar una gráfica del tiempo de ejecución respecto al valor de ns para los cinco primeros valores de ns
Para presentar una gráfica de los tiempos de ejecución
#para los cinco primeros valores de ns, puedes usar bibliotecas como Matplotlib. A continuación, se muestra un ejemplo:

import matplotlib.pyplot as plt

# Tomar los tiempos de ejecución para los cinco primeros valores de ns
ns_values = ns[:5]
times_values = times[:5]

# Crear una gráfica
plt.figure(figsize=(10, 6))
for i, func_name in enumerate(["Elementwise", "Blocks2", "Blocks4", "Blocks8"]):
    plt.plot(ns_values, [t[i] for t in times_values], label=func_name)

plt.xlabel('Valor de ns')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Tiempo de ejecución para los cinco primeros valores de ns')
plt.legend()
plt.grid(True)
plt.show()

# item 8 Presentar una gráfica del tiempo de ejecución respecto al valor de ns para los cinco últimos valores de ns
# Para presentar una gráfica de los tiempos de ejecución para los cinco últimos valores de ns, puedes usar el siguiente código similar al paso anterior
import matplotlib.pyplot as plt

# Tomar los tiempos de ejecución para los cinco últimos valores de ns
ns_values = ns[-5:]
times_values = times[-5:]

# Crear una gráfica
plt.figure(figsize=(10, 6))
for i, func_name in enumerate(["Elementwise", "Blocks2", "Blocks4", "Blocks8"]):
    plt.plot(ns_values, [t[i] for t in times_values], label=func_name)

plt.xlabel('Valor de ns')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Tiempo de ejecución para los cinco últimos valores de ns')
plt.legend()
plt.grid(True)
plt.show()

# Paso 9: Presentar una gráfica del speedup respecto al valor de ns para los cinco primeros valores de ns
Para calcular el speedup, primero debes determinar cuál de las funciones es la más lenta y usarla como referencia.
# Luego, puedes calcular el speedup para cada función en comparación con la función más lenta y graficarlo.

# Determinar la función más lenta
slowest_function_index = np.argmax(np.max(times, axis=0))

# Calcular el speedup para cada función en comparación con la función más lenta
speedup_values = []
for i, func_times in enumerate(times):
    speedup = times[slowest_function_index][i] / func_times[i]
    speedup_values.append(speedup)

# Crear una gráfica
plt.figure(figsize=(10, 6))
plt.plot(ns, speedup_values, label="Speedup en comparación con la función más lenta")
plt.xlabel('Valor de ns')
plt.ylabel('Speedup')
plt.title('Speedup respecto al valor de ns (comparación con la función más lenta)')
plt.legend()
plt.grid(True)
plt.show()
#Paso 10: Presentar una gráfica del speedup respecto al valor de ns para los cinco últimos valores de ns
Puedes utilizar el mismo código que en el paso anterior para generar una gráfica del speedup respecto al valor de ns para los cinco últimos valores de ns.

#Paso 11: Comparar las implementaciones de un solo bucle for con las implementaciones de dos bucles for
#Para comparar las implementaciones con un solo bucle for con las implementaciones de dos bucles for, 
#primero debes tener las implementaciones de dos bucles for. Luego, puedes calcular y graficar el tiempo de ejecución para ambas versiones. Aquí hay un ejemplo de cómo hacerlo:python

  # Tomar los tiempos de ejecución para todas las funciones
times_single_loop = times[:4]  # Los tiempos de ejecución de las funciones de un solo bucle for
times_double_loop = []  # Aquí debes calcular los tiempos de ejecución de las funciones de dos bucles for

# Crear una gráfica comparativa
plt.figure(figsize=(10, 6))
for i, func_name in enumerate(["Elementwise", "Blocks2", "Blocks4", "Blocks8"]):
    plt.plot(ns, [t[i] for t in times_single_loop], label=f"{func_name} (1 bucle)")
    plt.plot(ns, [t[i] for t in times_double_loop], label=f"{func_name} (2 bucles)")

plt.xlabel('Valor de ns')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Comparación de tiempo de ejecución entre 1 bucle y 2 bucles')
plt.legend()
plt.grid(True)
plt.show()

# Paso 12: Presentar dos gráficas de speedup
# Para calcular el speedup entre las implementaciones con un solo bucle for y las implementaciones con dos bucles for, puedes usar el siguiente código
# Calcular el speedup entre las implementaciones con un solo bucle for y dos bucles for
speedup_single_loop = []
speedup_double_loop = []

for i in range(4):  # Itera sobre las cuatro funciones
    speedup_single = times_single_loop[i] / times_double_loop[i]
    speedup_double = times_double_loop[i] / times_double_loop[i]  # Aquí debes calcular los tiempos de ejecución de las funciones de dos bucles for
    speedup_single_loop.append(speedup_single)
    speedup_double_loop.append(speedup_double)

# Crear las gráficas de speedup
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
for i, func_name in enumerate(["Elementwise", "Blocks2", "Blocks4", "Blocks8"]):
    plt.plot(ns, [t[i] for t in speedup_single_loop], label=f"{func_name} (1 bucle)")
plt.xlabel('Valor de ns')
plt.ylabel('Speedup')
plt.title('Speedup entre 1 bucle y 2 bucles (últimos 5 valores de ns)')
plt.legend()
plt.grid(True)

plt.subplot(1, 2, 2)
for i, func_name in enumerate(["Elementwise", "Blocks2", "Blocks4", "Blocks8"]):
    plt.plot(ns, [t[i] for t in speedup_double_loop], label=f"{func_name} (2 bucles)")
plt.xlabel('Valor de ns')
plt.ylabel('Speedup')
plt.title('Speedup entre 1 bucle y 2 bucles (últimos 5 valores de ns)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

