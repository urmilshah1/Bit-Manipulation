def CountDifferentBits(num1, num2):
    x =num1 ^ num2
    count=0
    while(x):
        x=(x)&(x-1)
        count += 1
    return count

print(CountDifferentBits(132, 15))