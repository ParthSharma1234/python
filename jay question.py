def reverse(n):
    a = 0 #a is use to store the digit
    r = 0 # rev is use to store the result
    while(n>0):
        d = n%10 #use to extract the last digit
        n = int(n/10) #use to find out questiont after the division
        r = r*10+d #shift the reverse into the 10th place and the digit will get added to the 1st place of the number.
    return r
x = int(input("Enter ur number:"))
r = reverse(x) #function call
print("Number : ",x)
print("Reverse : ",r)