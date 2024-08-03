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

def find_bucket_with_all_primes(n_points, max_buckets=100000):
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

        # Check if any bucket contains all the primes and no non-primes
        for j in range(num_buckets):
            if prime_counts[j] > 0 and non_prime_counts[j] == 0:
                print(f"Found a bucket with all primes in {num_buckets} bucket experiment.")
                print(f"Bucket{j + 1} has all the primes.")
                return

    print("No single bucket with all primes found.")

# Number of points to consider
n_points = 100000
find_bucket_with_all_primes(n_points)
