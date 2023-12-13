#conditional statements
#if-else
#checking age whether eligible for vote

age=int(input("enter age:"))
if age>=18:
    print("Eligible for voting")

else:
    print("Not eligible for voting")


#for loop
#table of a number
a=int(input("enter number:"))

for i in range(1,11):
    print(a,'*',i,'=',a*i)


#while loop
#find the sum of natural numbers
b=int(input("Enter number:"))
sum=0
i=1
while i<=b:
    sum+=i
    i+=1
print("sum:",sum)


