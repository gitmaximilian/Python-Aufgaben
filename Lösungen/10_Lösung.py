try:
    a = float(input("a: "))
    b = float(input("b: "))
    op = input("Operator: ")
    if op == "/":
        print(a / b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        print(a / b)
    else:
        print("ungültig")
except ZeroDivisionError:
    print("Fehler: Division durch Null!")