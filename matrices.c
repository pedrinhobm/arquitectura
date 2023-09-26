#include <stdio.h>

// Función para acumular los elementos de la matriz elemento a elemento
double acumularElementoAElemento(double matriz[], int n) {
    double suma = 0.0;
    for (int i = 0; i < n * n; i++) {
        suma += matriz[i];
    }
    return suma;
}

// Función para acumular los elementos de la matriz en bloques de 2 elementos
double acumularEnBloques2(double matriz[], int n) {
    double suma = 0.0;
    for (int i = 0; i < n * n; i += 2) {
        suma += matriz[i] + matriz[i + 1];
    }
    return suma;
}

// Función para acumular los elementos de la matriz en bloques de 4 elementos
double acumularEnBloques4(double matriz[], int n) {
    double suma = 0.0;
    for (int i = 0; i < n * n; i += 4) {
        suma += matriz[i] + matriz[i + 1] + matriz[i + 2] + matriz[i + 3];
    }
    return suma;
}

// Función para acumular los elementos de la matriz en bloques de 8 elementos
double acumularEnBloques8(double matriz[], int n) {
    double suma = 0.0;
    for (int i = 0; i < n * n; i += 8) {
        suma += matriz[i] + matriz[i + 1] + matriz[i + 2] + matriz[i + 3] +
                matriz[i + 4] + matriz[i + 5] + matriz[i + 6] + matriz[i + 7];
    }
    return suma;
}

int main() {
    // Tamaño de la matriz cuadrada
    int n = 4;
    
    // Declarar y llenar una matriz cuadrada de ejemplo
    double matriz[] = {1.0, 2.0, 3.0, 4.0,
                       5.0, 6.0, 7.0, 8.0,
                       9.0, 10.0, 11.0, 12.0,
                       13.0, 14.0, 15.0, 16.0};

    // Llamar a las funciones de acumulación
    double resultado1 = acumularElementoAElemento(matriz, n);
    double resultado2 = acumularEnBloques2(matriz, n);
    double resultado3 = acumularEnBloques4(matriz, n);
    double resultado4 = acumularEnBloques8(matriz, n);

    // Imprimir los resultados
    printf("Acumulación elemento a elemento: %lf\n", resultado1);
    printf("Acumulación en bloques de 2 elementos: %lf\n", resultado2);
    printf("Acumulación en bloques de 4 elementos: %lf\n", resultado3);
    printf("Acumulación en bloques de 8 elementos: %lf\n", resultado4);

    return 0;
}
