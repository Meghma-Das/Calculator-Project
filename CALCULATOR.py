def factorial(n):
    fact=1
    if n<0:
        print("Factorial of a negative number is not possible")
    elif(n==0):
        return 1
    else:
        for i in range(1,n+1,1): 
            fact=fact*i
        return(fact)     

def gcd(a,b):
    if a==0:
        return b
    elif b==0:
        return a
    elif a>b:
        return gcd(a%b,b)
    else:
        return gcd(a,b%a)

def combination(n,r):
    if r>n:
        print("r cannot be greater than n")
        return
    else:
        combination=factorial(n)/(factorial(r)*factorial(n-r))
        return combination

def permutation(n,r):
    if r>n:
        print("r cannot be greater than n")
        return
    else:
        permutation=factorial(n)/factorial(n-r)
        return permutation
print("MENU")
print("1.ADDITION\n2.SUBTRUCTION\n3.MULTIPLICATION\n4.DIVITION\n5.MODULO\n6.TO THE POWER\n7.GCD\n8.FACTORIAL\n9.LOGARITHM\n10.COMBINATION\n11.PERMUTATION\n12.Exit")
while(1):    
    ch=int(input("Enter your choice:")) 
    if ch==1:
        print("ADDITION")
        a=int(input("Enter first number:"))
        b=int(input("Enter second number:"))         
        print("{0} + {1} = {2}".format(a,b,a+b))
    elif ch==2:
        print("SUBTRUCTION")
        a=int(input("Enter first number:"))
        b=int(input("Enter second number:"))         
        print("{0} - {1} = {2}".format(a,b,a-b))
    elif ch==3:
        print("MULTIPLICATION")
        a=int(input("Enter first number:"))
        b=int(input("Enter second number:"))         
        print("{0} * {1} = {2}".format(a,b,a*b)) 
    elif ch==4:
        print("DIVITION")
        a=int(input("Enter first number:"))
        b=int(input("Enter second number:"))
        if b!=0:
            print("{0} / {1} = {2}".format(a,b,a/b)) 
        else:
            print("Error! Division by zero is not allowed") 
    elif ch==5:
        print("MODULO")
        a=int(input("Enter first number:"))
        b=int(input("Enter second number:"))
        if b!=0:
            print("{0} % {1} = {2}".format(a,b,a%b)) 
        else:
            print("Error! Division by zero is not allowed")          
    elif ch==6:
        print("TO THE POWER")
        a=int(input("Enter the number:"))    
        b=int(input("Enter the power:"))
        print("{0}^{1} = {2}".format(a,b,a**b))  
    elif ch==7:
        print("GCD")
        a=int(input("Enter first number:"))
        b=int(input("Enter second number:"))
        print("GCD of {0} and {1} is {2}".format(a,b,gcd(a,b)))
    elif ch==8:
        print("FACTORIAL")
        n=int(input("Enter the number:"))
        print("Factorial of {0} is {1}".format(n,factorial(n)))
    elif ch==9:
        print("LOGARITHM")
        import math
        n=int(input("Enter the number:"))
        base=int(input("Enter the base:"))
        print("logarithm base {0} of {1} is {2}".format(base,n,math.log(n,base)))
    elif ch==10:
        print("COMBINATION")
        n = int(input("Enter the total number of items:"))
        r = int(input("Enter the number of items to choose:"))
        print("{0}C{1}={2}".format(n,r,combination(n,r)))
    elif ch==11:
        print("PERMUTATION")
        n = int(input("Enter the total number of items:"))
        r = int(input("Enter the number of items to choose:"))
        print("{0}P{1}={2}".format(n,r,permutation(n,r)))   
    elif ch==12:
        print("Thank you")
        break             
    else:
        print("Invalid Choice")                   