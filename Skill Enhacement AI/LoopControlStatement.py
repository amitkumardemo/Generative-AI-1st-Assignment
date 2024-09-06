largest = None
for i in range(5):
    num = int(input("Enter a number: "))
    if largest is None or num > largest:
        largest = num
print(f"The largest number is: {largest}")
