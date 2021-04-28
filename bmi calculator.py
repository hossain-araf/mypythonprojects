a=float(input("what is your weight in kilograms"))
b=float(input("What is your height in metre"))
h=a/b**2
if h <24.9 and h>18.5:
    print('you are in the limit')
elif h<18.5:
    print('you have a low bmi')
elif h>24.9:
    print("you have a high bmi")
