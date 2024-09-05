num1=int(input("Enter lower digit:"))
num2=int(input("enter upper digit:"))
for num in range (num1,num2+1):
    flag=False
    if num < 2 : flag=True
    for i in range (2,(num//2)+1):
        if num/i == num//i:
            flag = True
    if flag:
        print(num)




