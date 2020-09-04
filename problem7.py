
import timeit

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
    




def get_nth_prime(n):
    

    max_val = 1
    count = len(sieve(max_val))


    print('*')
    while(count < n):
        max_val += 1000
        count = len(sieve(max_val))

    print('**')
    while(count > n):
        max_val -= 100
        count = len(sieve(max_val))
    
    print('***')
    while(count < n):
        max_val += 10
        count = len(sieve(max_val))

    
    print('****')
    while(count > n):
        max_val -= 1
        count = len(sieve(max_val))

    #print('count = ', count) 
    nth_prime = sieve(max_val)[-1]
    
    return nth_prime




n = 10001    

start = timeit.default_timer()
nth_prime = get_nth_prime(n)
stop = timeit.default_timer()

print('%dth prime is : %d ' % (n, nth_prime))
print('Time : ', (stop-start) , 'secs' )




