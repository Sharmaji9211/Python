nums= [1,2,3,4,5,6,7,8,9]
num= [1,2,3,4,8,9]
num1= [1,4,5,6,7,8,9]

def lenght(list):
    print(len(list))

lenght(nums)
lenght(num)
lenght(num1)

def usd_to_Inr(num):
    inr=num*90
    print(num," USD = ",inr,"INR")

usd_to_Inr(4)    

def fact(n):
   factorial=1
   for i in range(1,n+1):
    factorial *= i

print(factorial)

fact(3)    


def add(a, b):
    return a + b

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

result = add(x, y)

print("Sum =", result)