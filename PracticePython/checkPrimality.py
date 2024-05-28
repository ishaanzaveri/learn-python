def check_primality(num):
    for i in range(2,int(num/2)):
        if (num % i == 0):
            return False
    return True

num = int(input("Input a number "))
result = "Is Prime" if check_primality(num) else "is not prime" 
print(result)