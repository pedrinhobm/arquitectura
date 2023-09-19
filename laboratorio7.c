#include <stdio.h>
#include <time.h>

int programa1(int N) {
  int sum = 0;
  int array[N];

  // Inicializar el array
  for (int i = 0; i < N; i++) {
    array[i] = i;
  }

  // Calcular la suma del array
  for (int i = 0; i < N; i++) {
    sum += array[i];
  }

  // Imprimir la suma
  printf("Sum: %d\n", sum);

  return 0;
}

int programa2(int N) {
  int sum = 0;

  // Calcular la suma del array
  for (int i = 0; i < N; i++) {
    sum += i;
  }

  // Imprimir la suma
  printf("Sum: %d\n", sum);

  return 0;
}

int main() {
  struct timespec ti, tf;
  double elapsed;
  int rpta1, rpta2;
  int N = 1000000; // Cambiado 1e6 a 1000000 para evitar problemas con el tipo de dato

  clock_gettime(CLOCK_REALTIME, &ti);
  rpta1 = programa1(N);
  clock_gettime(CLOCK_REALTIME, &tf);
  elapsed = (tf.tv_sec - ti.tv_sec) * 1e9 + (tf.tv_nsec - ti.tv_nsec);
  printf("El tiempo en nanosegundos que toma el programa 1 es %.2lf ns\n", elapsed);

  clock_gettime(CLOCK_REALTIME, &ti);
  rpta2 = programa2(N);
  clock_gettime(CLOCK_REALTIME, &tf);
  elapsed = (tf.tv_sec - ti.tv_sec) * 1e9 + (tf.tv_nsec - ti.tv_nsec);
  printf("El tiempo en nanosegundos que toma el programa 2 es %.2lf ns\n", elapsed);

  return 0;
}
