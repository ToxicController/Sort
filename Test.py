print("Type the numbers you want to be sorted least to greatest")
print("When you are done type 'done'")
print("Enter your first digit")


userInt = input()
while not (userInt.isdigit()):
    print("Please enter a digit!")
    userInt = input()

digits = [int(userInt)]

#Gets the user inputted numbers
while not (userInt == "done"):
    print("Enter next digit")
    userInt = input()
    if (userInt.isdigit()):
        userInt
        digits.append(userInt)
    else:
        if not (userInt == "done"):
            print("Please enter a digit!")
        
        
print(digits)