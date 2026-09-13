print("JENCUR6918  09/12/26")

numbers = [60,33,88,3,7,9,22]

print(f"The list of integers: {numbers}")

# This variable n represents each number in the list in my search for the largest integer
largest = numbers[0]
for n in numbers:
    if n > largest:
        largest = n

print(f"The largest number is: {largest}")

# This n represents each number in the list in my search for the smallest integer
smallest = numbers[0]
for n in numbers:
    if n < smallest:
        smallest = n

print(f"The smallest number is: {smallest}")
