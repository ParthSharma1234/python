#WAP that take i/p from the user for driving licence
user = int(input())
if user>18:
    print("Of course you are eligible for driving licence.")
if user<18:
    print("You are not eligible for driving licence.")
if user==18:
    print("It is not decided that you are eligible for driving licence or not.")
