# myapp/utils/prime_numbers.py
class PrimeNumberGenerator:
    @staticmethod
    def generate_primes(lower_limit, upper_limit):
        primes = []
        for num in range(lower_limit, upper_limit + 1):
            if PrimeNumberGenerator.is_prime(num):
                primes.append(num)
        return primes

    @staticmethod
    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True
        for i in range(2, n // 2 + 1):
            if n % i == 0 and i != n:
                return False
        return True






# def prime(lower_limit, upper_limit):
#     for i in range(lower_limit, upper_limit + 1):
#         if is_prime(i):
#             print(i, end=' ')

# def is_prime(n):
#     if n == 1:
#         return False
#     if n == 2:
#         return True
#     for i in range(2, n // 2 + 1):
#         if n % i == 0 and i != n:
#             return False
#     return True

# try:
#     lower_limit = int(input("Enter the lower limit: "))
#     upper_limit = int(input("Enter the upper limit: "))
    
#     if lower_limit < 1 or upper_limit < lower_limit:
#         raise ValueError("Invalid input. Please ensure the lower limit is at least 1, and the upper limit is greater than or equal to the lower limit.")

#     print("The prime numbers in this range are:")
#     prime(lower_limit, upper_limit)

# except ValueError as ve:
#     print(f"Error: {ve}")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")
