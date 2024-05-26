num = int(input("List number you want divisors for: "))
list = []
for i in range(2, int(num/2)):
    if num % i == 0:
        list.append(i)

print(list)