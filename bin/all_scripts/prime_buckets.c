#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>

bool is_prime(int n) {
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;
    for (int i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) return false;
    }
    return true;
}

void find_exclusive_prime_bucket(int n_points, int max_buckets) {
    int *numbers = (int *)malloc(n_points * sizeof(int));
    for (int i = 0; i < n_points; ++i) {
        numbers[i] = i + 1;
    }

    for (int num_buckets = 1; num_buckets <= max_buckets; ++num_buckets) {
        int *prime_counts = (int *)calloc(num_buckets, sizeof(int));
        int *non_prime_counts = (int *)calloc(num_buckets, sizeof(int));

        for (int i = 0; i < n_points; ++i) {
            int bucket_index = i % num_buckets;
            if (is_prime(numbers[i])) {
                prime_counts[bucket_index]++;
            } else {
                non_prime_counts[bucket_index]++;
            }
        }

        int prime_only_buckets = 0;
        int prime_only_bucket_index = -1;
        for (int j = 0; j < num_buckets; ++j) {
            if (prime_counts[j] > 0 && non_prime_counts[j] == 0) {
                prime_only_buckets++;
                prime_only_bucket_index = j;
            }
        }

        if (prime_only_buckets == 1) {
            bool other_buckets_have_no_primes = true;
            for (int k = 0; k < num_buckets; ++k) {
                if (k != prime_only_bucket_index && prime_counts[k] != 0) {
                    other_buckets_have_no_primes = false;
                    break;
                }
            }

            if (other_buckets_have_no_primes) {
                printf("Found an experiment with one exclusive prime bucket in %d bucket experiment.\n", num_buckets);
                printf("Bucket %d has all the primes and no non-primes.\n", prime_only_bucket_index + 1);
                for (int k = 0; k < num_buckets; ++k) {
                    printf("Bucket %d:\n", k + 1);
                    printf("  primes: %d\n", prime_counts[k]);
                    printf("  non-primes: %d\n", non_prime_counts[k]);
                }
                free(numbers);
                free(prime_counts);
                free(non_prime_counts);
                return;
            }
        }

        free(prime_counts);
        free(non_prime_counts);
    }

    printf("No experiment found where only one bucket contains all primes and no non-primes.\n");
    free(numbers);
}

int main() {
    int n_points = 100000;
    int max_buckets = 100000;
    find_exclusive_prime_bucket(n_points, max_buckets);
    return 0;
}
