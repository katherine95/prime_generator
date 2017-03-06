def prime():
    for i in range(1, n):
        if n % i == 0:
            return False
    return True
print(prime(7))            
