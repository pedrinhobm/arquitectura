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
