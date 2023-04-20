#WAP that take i/p form user  and take i/p till the number is not greater then 100
while(True):
    n = int(input("Enter a number:-\n"))
    if n>100:
        print("Great u entered a no. greater than 100\n")
        break
    else:
        print("Try again!")
    continue