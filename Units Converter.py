print("Hy, I am converter that coverts km into miles")

while True:

    km = int(input("Enter the value in kilometers: "))

# 1 Kilometre = 0.621371 Mile
    ratio = 0.621371

    miles = km * 0.621371

    print("{0} kilometers is {1} miles.".format(km, miles))
    choice = input("Would you like to do another conversion (y/n)")
    if choice == "y":
        km = int(input("Enter the value in kilometers: "))
        print("{0} kilometers is {1} miles.".format(km, miles))
    elif choice == "y":
        km = int(input("Enter the value in kilometers: "))
        print("{0} kilometers is {1} miles.".format(km, miles))
    else:
        print("By,by")
    break



