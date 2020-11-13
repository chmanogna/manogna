print('hi')

num1=10
num2=20

print("Before Swapping:",num1,num2)

#temp=num2
#num2=num1
#num1=temp

num1=num1+num2
num2=num1-num2
num1=num1-num2
num1,num2=num2,num1

print("After Swapping:",num1,num2)
