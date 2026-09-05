# i=1 
# while i<=100 :
#     print(i)
#     i += 1

# i=100
# while i>=1 :
#     print(i)
#     i -= 1

# n=int(input("enter the number :"))
# i=1
# while i<=10 :
#     print(n," * ",i," = ",n*i)
#     i +=1
    
# nums=[]
# i=1
# while i <= 10 :
#     nums.append(i*i)
#     i += 1
# print(nums)

# tip=(1,4,9,16,25,36,49,64,81,100)
# idx=0
# x=int(input("enter the number  :"))
# while idx < len(tip) :
#     if x == tip[idx]:
#         print("find it")
#         break
#     else :
#         idx +=1
# else :
#     print("Not found")    

# nums=[1,2,3,4,5,6,7,8,9]
# for num in nums :
#     print(num)

# nums1=(1,4,9,16,25,36,49)
# x=4
# for num1 in nums1 :
#     if(num1 == 4 ) :
#         print("found it") 


# n=int(input("Enter the number :"))
# i=1
# sum =0
# while i<=n :
#     sum=sum+i
#     i += 1
# print(sum)    

n=int(input("Enter the number :"))
i=1
fact =1
while i<=n :
    fact=fact*i
    i += 1
print(fact)    
