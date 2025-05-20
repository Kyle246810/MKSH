nuber=int(input("請輸入一個要轉乘的二進位數:"))
binary=list()
while number>1:
    binary.append(str(number %2))
    nuber //=2
binary.append(str(nuber))
print("".join(reversed(binary)))