
def problem4():
    maxAns = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            n = i * j
            if n > maxAns and str(n) == str(n)[::-1]:
                print(n)
                maxAns = n


def problem5():
    def gcd(a, b):
        if a > b:
            return gcd(b, a)
        if a == 0:
            return b
        return gcd(b % a, a)

    def lcm(a, b):
        return int(a * b / gcd(a, b))

    n = 1
    for i in range(1, 20):
        n = lcm(n, i)
    print(n)


def problem6():

    print(sum([i for i in range(1, 101)])**2 -
          sum([i**2 for i in range(1, 101)]))


def problem7():
    primes = [2]
    n = 2
    while len(primes) < 10002:
        n += 1
        # check if n is prime
        isDivisible = False
        for p in primes:
            if n % p == 0:
                isDivisible = True
                break
        if not isDivisible:
            primes.append(n)
    print(primes[10000])


def problem8():
    inp = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
    res = 1
    for i in range(len(inp) - 12):
        newRes = 1
        for j in range(i, i + 13):
            newRes *= int(inp[j])
        if newRes > res:
            res = newRes
    print(res)


def problem9():
    def isSquare(n):
        return n**0.5 == int(n * 0.5)
    elsum = 1000

    for a in range(1, elsum):
        for b in range(a, elsum):
            if(a**2 + b**2 == (elsum - a - b)**2):
                print(a, b, elsum - a - b, a * b * (elsum - a - b))


def problem10():
    M = int(2000000**0.5) + 3
    isPrime = [True for i in range(2000000)]
    primes = []
    isPrime[0] = False
    isPrime[1] = False

    for p in range(2, M):
        if isPrime[p]:
            primes.append(p)
            for i in range(p*p, M, p):
                isPrime[i] = False
    sumOfPrimes = 0
    for i in range(2,2000000):
        if isPrime[i]:
            sumOfPrimes += i 
    print(sumOfPrimes)

problem10()