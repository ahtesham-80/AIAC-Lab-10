def divide_numbers(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Error: Division by zero"
print(divide_numbers(10,0))





