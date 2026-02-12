def calc(a, b, c):
    if str(c) == '+':
        result = a + b
    elif str(c) == '-':
        result = a - b
    elif str(c) == '*':
        result = a * b
    elif str(c) == '/':
        result = a / b
    else:
        print("invalid")
        return
    return result
p = int(input("2-digit number:"))
q = int(input("2-digit number:"))
print("use / for division", "use + for addition", "use - for subtraction")
r = input("operator:")

addition = calc(p, q, r)
print(addition)