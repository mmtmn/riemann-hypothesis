#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define NUM_ZEROS 1000

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
void find_riemann_zeros(double* zeros, int num_zeros) {
    double t = 0.0;
    int found = 0;
    while (found < num_zeros) {
        double z = Z(t);
        if (fabs(z) < 1e-6) {
            zeros[found] = t;
            found++;
        }
        t += 0.001; // Increase t by a small value to search for next zero
    }
}

int main() {
    double zeros[NUM_ZEROS];
    find_riemann_zeros(zeros, NUM_ZEROS);

    // Print the zeros formatted as a numpy array
    printf("known_zeros = np.array([");
    for (int i = 0; i < NUM_ZEROS; i++) {
        if (i == NUM_ZEROS - 1) {
            printf("%f])\n", zeros[i]);
        } else {
            printf("%f, ", zeros[i]);
        }
    }

    return 0;
}
