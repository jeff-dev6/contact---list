def get_digits():
    while True:
        num = input("Enter an operation formatted as x, operator, y: ")
        formatted_num = num.split()
        if len(formatted_num) != 3:
            print("Incorrect operation format")
            continue
        try:
            x = int(formatted_num[0])
            operator = formatted_num[1]
            y = int(formatted_num[2])

            if operator not in {"+", "-", "/", "*"}:
                print("Invalid operator. Use any of these, +, -, *, /")
                continue
            return x, operator, y
        except ValueError:
            print("Invalid Number. Insert an interger. \n")
            continue

def digit_cal(x, operator, y):
    if operator == "+":
        return x + y
    elif operator == "-":
        return x - y
    elif operator == "/":
        if y > x:
            print("Denominator can't be greater than numerator")
            return None
        if y == 0:
            print("Numerator can't be divided by 0")
            return None
        return x / y
    elif operator == "*":
        return x * y
    else:
        print("Invalid operator: Try again")


def main_cal():
    while True:
        x, operator, y = get_digits()
        result = digit_cal(x, operator, y)
        if result is not None:
            print(f"Result: {x} {operator} {y} = {result}")
            break
        continue
        

    
   

if __name__ == "__main__":
    main_cal()



    