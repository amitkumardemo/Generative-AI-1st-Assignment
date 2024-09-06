age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
    if 18 <= age <= 25:
        print("You are eligible for a youth discount.")
    else:
        print("You are not eligible for a youth discount.")
else:
    print("You are not eligible to vote.")
