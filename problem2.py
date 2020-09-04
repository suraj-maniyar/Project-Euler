

def fib(n):

    if n<1:
        return 0

    f0, f1 = 0, 1
    f2 = 0
    while(n):
        f2 = f0+f1
        f0 = f1
        f1 = f2
        n-=1
    return f2



# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
# Note terms at index of the form 3n+2 are even

val = 0

for i in range(11):
    val += fib(3*i+2)

print('val = %d', val)


