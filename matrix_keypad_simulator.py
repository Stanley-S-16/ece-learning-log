# matrix_keypad_simulator.py

print("Matrix Keypad Calculator Simulator")
print("Enter digits and operators like a keypad.")
print("Press '=' to calculate result. Press 'q' to quit.\n")

expression = ""

while True:
    key = input("Press key: ")

    if key == 'q':
        print("Exiting calculator.")
        break

    elif key == '=':
        try:
            result = eval(expression)
            print("Result =", result)
            expression = str(result)
        except:
            print("Invalid expression")
            expression = ""

    else:
        expression += key
        print("Current expression:", expression)
