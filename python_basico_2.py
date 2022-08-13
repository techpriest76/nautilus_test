#make a program that says the biggest prime divider of a given number

def check_prime(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True


numb=int(input("give me a number to find its biggest prime divider: "))
numbers=[]
prime_numbers=[]

for i in range(1,numb+1):
    if numb%i==0:
        numbers.append(i)

for i in numbers:
    if check_prime(i):
        prime_numbers.append(i)

print("its bigger prime divider is:",max(prime_numbers))
