
#Write a function that receives an array of type integer,
#and the function returns the prime numbers in that array.

def is_prime(n):
    # any number less thane or = 1 is not prime
    if (n <= 1):
        return False

    # Check from 2 to n
    for i in range(2, int(n)):
        if (n % i == 0):
            return False

    return True

def primes_nums(array):
    array2 = [i for i in array if is_prime(i)]
    return array2

s = [33, 4, 44, 89, 33, 7]
print(primes_nums(s))
