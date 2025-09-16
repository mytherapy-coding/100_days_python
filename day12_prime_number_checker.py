def is_prime(num):
    if num <= 1:
        return False  # 1 or less is not prime
    if num == 2:
        return True  # 2 is prime
    if num % 2 == 0:
        return False  # even numbers > 2 are not prime

    # Loop over possible odd divisors from 3 up to sqrt(num)
    # Why sqrt(num)? Any factor larger than sqrt(num) has a corresponding
    # factor smaller than sqrt(num), so no need to check beyond sqrt(num)
    # int(num ** 0.5) converts float to integer for range()
    # +1 because range stops before the end value

    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:  # if divisible by i → not prime
            return False  # immediately return False if a divisor is found

    return True  # no divisors found → prime
