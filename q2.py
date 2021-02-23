#Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.
#Suppose the following input is supplied to the program: 8 Then, the output should be:40320

num = int(input("Enter number to find factorial: "))

fact = 1
if num<0:
    print("Factorial does not exist for negative numbers.")
elif num==0:
    print("Factorial is 1")
elif num==1:
    print("Factorial is 1")
else:
    for i in range(1,num+1):
        fact = fact*i
    print("Factorial of %d is %d"%(num,fact))    
