word = input("Enter input: ")
flag = True 
for i in range (0, int(len(word)/2)):
    if word[i] != word[-i-1]:
        flag = False
        break
if flag:
    print("palindrome")
else:
    print("not palindrome")