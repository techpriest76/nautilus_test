#Give the sum of all prime numbers below 1k

def check_prime(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

prime_sum=0
for i in range(1,1000):
    if check_prime(i):
        prime_sum+=i

print(prime_sum)
