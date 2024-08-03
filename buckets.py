def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def count_primes_and_non_primes_in_buckets(n_points, max_buckets=16):
    numbers = list(range(1, n_points + 1))

    for num_buckets in range(1, max_buckets + 1):
        # Reset counts for the current number of buckets
        prime_counts = [0] * num_buckets
        non_prime_counts = [0] * num_buckets

        for i, number in enumerate(numbers):
            bucket_index = i % num_buckets
            if is_prime(number):
                prime_counts[bucket_index] += 1
            else:
                non_prime_counts[bucket_index] += 1

        # Print results for the current number of buckets
        print(f"{num_buckets} bucket experiment")
        for j in range(num_buckets):
            print(f"bucket{j + 1}:")
            print(f"  primes: {prime_counts[j]}")
            print(f"  non-primes: {non_prime_counts[j]}")
        print("\n")

# Number of points to consider
n_points = 10000
count_primes_and_non_primes_in_buckets(n_points)
