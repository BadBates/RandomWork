smaller = int(input("what is the smallest number:"))
larger = int(input("what is the largest number:"))

count = 0
for number in range(smaller, larger):
    if number % 2 == 0:
        count += 1
        print("the even numbers are: ", number)