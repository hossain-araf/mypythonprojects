def primenumber():
    s=int(input("whats the number"))
    if s<1 and s%2==0:
        print("is not a prime number")
    elif s==2 or s==3 or s==5 or s==7:
        print("given number is a prime number")
    elif s%3==0:
        print("given number is not a prime number")
    elif s%5==0:
        print("given number is a prime number")
    elif s%7==0:
        print("given number is a prime number")
    else:
        print("given number is  a prime number")       


primenumber()