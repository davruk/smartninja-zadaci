print("Hy, I am converter that convert km into miles")

while True:
    km = float(input("Please enter tha value in km: "))

# conversion factor = 0.621371
    miles = km * 0.621371

    print("{0} kilometers is {1} miles.".format(km, miles))

    choice = input("Would you like to do another conversion (y/n)")
    if choice != "y":
        print("By,By")
        break


