import timeit
import math

# Sieve of Eratosthenes : returns list of all primes less than max_val
def sieve(max_val=1000):
    visited = set()
    count = 0
    prime = []

    for num in range(2, max_val):
        if num not in visited:
            prime.append(num)
            temp = num
            while(temp<max_val):
                visited.add(temp)
                temp += num

    return prime




def get_largest_prime(n):

    upper_limit = math.sqrt(n)
    print('upper_limit : ', upper_limit)
    primes = sieve(int(upper_limit)+1)
    

    for p in primes[::-1]:
        if n % p == 0:
            return p

    return -1


start = timeit.default_timer()
largest = get_largest_prime(600851475143)
stop = timeit.default_timer()

print('Largest = ', largest)
print('Time = ', stop-start, ' secs')
