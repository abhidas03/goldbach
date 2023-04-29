import time
#dictionary of primes
primes = {}


f = open("goldbach.txt", "w")

def SieveOfAtkin(limit):
    # 2 and 3 are known
    # to be prime
    if limit > 2:
        primes.update({2: 2})
    if limit > 3:
        primes.update({3: 3})

    # Initialise the sieve
    # array with False values
    sieve = [False] * (limit + 1)
    for i in range(0, limit + 1):
        sieve[i] = False

    '''Mark sieve[n] is True if
    one of the following is True:
    a) n = (4*x*x)+(y*y) has odd
    number of solutions, i.e.,
    there exist odd number of
    distinct pairs (x, y) that
    satisfy the equation and
    n % 12 = 1 or n % 12 = 5.
    b) n = (3*x*x)+(y*y) has
    odd number of solutions
    and n % 12 = 7
    c) n = (3*x*x)-(y*y) has
    odd number of solutions,
    x > y and n % 12 = 11 '''
    x = 1
    while x * x <= limit:
        y = 1
        while y * y <= limit:

            # Main part of
            # Sieve of Atkin
            n = (4 * x * x) + (y * y)
            if (n <= limit and (n % 12 == 1 or
                                n % 12 == 5)):
                sieve[n] ^= True

            n = (3 * x * x) + (y * y)
            if n <= limit and n % 12 == 7:
                sieve[n] ^= True

            n = (3 * x * x) - (y * y)
            if (x > y and n <= limit and
                    n % 12 == 11):
                sieve[n] ^= True
            y += 1
        x += 1

    # Mark all multiples of
    # squares as non-prime
    r = 5
    while r * r <= limit:
        if sieve[r]:
            for i in range(r * r, limit+1, r * r):
                sieve[i] = False

        r += 1

        # Print primes
    # using sieve[]
    for a in range(5, limit+1):
        if sieve[a]:
            primes.update({a: a})
            
# Driver Code
start = time.time()
limit = 1000000000
SieveOfAtkin(limit)
end = time.time()
print()
print (end - start)

#goldbach part:
#for every even number up to a billion 
#iterate through dictionary
#if there is a X - Y = Z in dictionary
#continue 
#else
#print impossible; break
goldbach = True
for x in range(4, limit, 2):
    sumExists = False
    for y in primes:
        if (x - y) in primes:
            f.write(str(x) + ' = '+ str(y) + ' + ' + str((x-y)) + "\n")
            sumExists = True
            break
    if (not sumExists):
        print(x)
        print("goldbach's conjecture is false")
        goldbach = False
        break
            
if (goldbach):
    print("We proved goldbach up to a billion")
else:
    print("We proved goldbach is wrong")