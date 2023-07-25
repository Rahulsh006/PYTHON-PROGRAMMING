def fibo(i):
    if i <= 1:
        return i
    else:
        return (fibo(i - 1) + fibo(i - 2))

n=int(input("enter the count of fibo series "))

if n <=0:
    print("Please enter a Positive Number")
else:
    print("Fibonacci Series:", end=" ")

for i in range(n):
    print(fibo(i), end=" ")
