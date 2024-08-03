#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define NUM_ZEROS 1000000000000LL  // Use long long for large constants
#define BATCH_SIZE 1000000         // Write to file in batches

// Function to compute the Riemann-Siegel Z function (approximation)
double Z(double t) {
    double sum1 = 0.0;
    double sum2 = 0.0;
    int N = (int)sqrt(t / (2 * M_PI));
    for (int n = 1; n <= N; n++) {
        sum1 += cos(t * log(n) - t / 2 - M_PI / 8);
    }
    for (int n = 1; n <= N; n++) {
        sum2 += cos(t * log(n / M_PI) - t / 2 - M_PI / 8);
    }
    return 2 * sum1 + sum2;
}

// Function to find zeros of the Z function (approximation to zeta zeros)
void find_riemann_zeros(const char* filename, long long num_zeros) {
    FILE *file = fopen(filename, "w");
    if (!file) {
        perror("Error opening file");
        exit(EXIT_FAILURE);
    }

    double t = 0.0;
    long long found = 0;
    double* zeros = (double*)malloc(BATCH_SIZE * sizeof(double));
    if (!zeros) {
        perror("Memory allocation failed");
        exit(EXIT_FAILURE);
    }

    while (found < num_zeros) {
        int batch_count = 0;
        while (batch_count < BATCH_SIZE && found < num_zeros) {
            double z = Z(t);
            if (fabs(z) < 1e-6) {
                zeros[batch_count++] = t;
                found++;
            }
            t += 0.001; // Increase t by a small value to search for next zero
        }

        // Write the current batch to the file
        for (int i = 0; i < batch_count; i++) {
            fprintf(file, "%f\n", zeros[i]);
        }
    }

    free(zeros);
    fclose(file);
}

int main() {
    find_riemann_zeros("riemann_zeros.txt", NUM_ZEROS);
    return 0;
}
