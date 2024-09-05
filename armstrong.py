#n = int(input("armstrong numbers up to 1000 are:"))
for num in range(1,1001):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** len(str(num))
        temp //= 10
    if num == sum:
        print(num)

