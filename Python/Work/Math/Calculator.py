def calculation(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b
    # return multiple values separated by comma
    return addition, subtraction, multiplication, division

# get result in tuple format
res = calculation(int(input("A")),int(input("B")))
print(res)