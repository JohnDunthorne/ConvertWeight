# main attributes
weight = float(input("What is your weight?: "))
unit = input("(L)bs or (K)g?: ")
# use .upper module to covert any lower case "l" or "k" typed by the user
# else statement for when user enters something unusable by program

if unit.upper() == "L":
    print(weight * 0.45)
elif unit.upper() == "K":
    print(weight / 0.45)
else:
    print("Please Enter L or K")


