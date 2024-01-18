import sys

def prime_factorization(n):
    factors = []
    # Divide by 2 until n is odd
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    # Divide by odd numbers starting from 3
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    
    # If n is a prime number greater than 2
    if n > 2:
        factors.append(n)
    
    return factors

number_to_factorize = int(sys.argv[1])
result = prime_factorization(number_to_factorize)
print(f"The prime factors of {number_to_factorize} are: {result}")
