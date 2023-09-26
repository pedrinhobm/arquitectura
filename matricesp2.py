#13 // functions2.c
#3: Implementar funciones en C con dos bucles for
# Ahora, vamos a implementar las funciones en C que acumulan elementos de una matriz cuadrada de números
# reales utilizando dos bucles for. Aquí tienes un ejemplo de cómo podrían verse estas implementaciones en un archivo C llamado functions2.c:

#include <stdio.h>

void accumulate_by_rows(float *matrix, int n, float *result) {
    float sum = 0.0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            sum += matrix[i * n + j];
        }
    }
    *result = sum;
}

void accumulate_by_columns(float *matrix, int n, float *result) {
    float sum = 0.0;
    for (int j = 0; j < n; j++) {
        for (int i = 0; i < n; i++) {
            sum += matrix[i * n + j];
        }
    }
    *result = sum;
}


#14 gcc -shared -o mylibrary2.so functions2.c

# 15

import ctypes

# Cargar la segunda biblioteca dinámica
mylibrary2 = ctypes.CDLL('./mylibrary2.so')

# Definir tipos de argumentos y valores de retorno para las nuevas funciones de C
mylibrary2.accumulate_by_rows.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.c_int, ctypes.POINTER(ctypes.c_float)]
mylibrary2.accumulate_by_rows.restype = None

mylibrary2.accumulate_by_columns.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.c_int, ctypes.POINTER(ctypes.c_float)]
mylibrary2.accumulate_by_columns.restype = None

# Implementar la función que devuelve las dos nuevas funciones configuradas
def get_accumulation_functions2():
    return mylibrary2.accumulate_by_rows, mylibrary2.accumulate_by_columns

# Hacer una instancia de las nuevas funciones
accumulation_functions2 = get_accumulation_functions2()

# 16
Prueba las nuevas funciones para el menor valor de ns
Puedes probar las nuevas funciones con el menor valor de ns y la variable Y utilizando el siguiente código en un nuevo script Python:
import numpy as np

n = ns[0]
A = np.random.rand(n, n)
Y = A.flatten()

# Prueba las nuevas funciones para el menor valor de ns
for func in accumulation_functions2:
    result = ctypes.c_float()
    func(Y.ctypes.data_as(ctypes.POINTER(ctypes.c_float)), n, ctypes.byref(result))
    print(f"Resultado: {result.value}")

#17   Prueba las nuevas funciones para el mayor valor de ns
# Realiza la misma prueba pero con el mayor valor de ns en el mismo script Python:
n = ns[-1]
A = np.random.rand(n, n)
Y = A.flatten()

# Prueba las nuevas funciones para el mayor valor de ns
for func in accumulation_functions2:
    result = ctypes.c_float()
    func(Y.ctypes.data_as(ctypes.POINTER(ctypes.c_float)), n, ctypes.byref(result))
    print(f"Resultado: {result.value}")

# 18
