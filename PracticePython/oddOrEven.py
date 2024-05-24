num = int(input("Enter main number:\n"))
divisor = int(input("Enter divisor:\n"))

if num % divisor == 0: 
    print(f"{num} gets divided by {divisor}")
else:
    print(f"{num} does not get divided by {divisor}")