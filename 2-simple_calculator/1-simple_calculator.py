while True:
    print('Welcome to the Simple Calculator 🧮')
    print('Write the first number')
    try:
        num1 = (float(input('>> ')))
    except ValueError:
        print('You can only write numbers\n')
        continue
    print('Write the second number')
    try:
        num2 = (float(input('>> ')))
    except ValueError:
        print('You can only write numbers\n')
        continue

    print('Pick a number from 1 to 4 to choose the operator')
    print('1 - "Addition (+)"')
    print('2 - "Subtraction (-)"')
    print('3 - "Multiplication (*)"')
    print('4 - "Division (/)"')
    
    try:
        operator = int(input('>> '))
        match operator:
            case 1:
                op = '+'
                result = num1 + num2
            case 2:
                op = '-'
                result = num1 - num2
            case 3:
                op = '*'
                result = num1 * num2
            case 4:
                op = '/'
                result = num1 / num2
        print(f'\n{num1} {op} {num2} = {result}\n')

    except ZeroDivisionError:
        print('You cannot divide a number by 0\n')
        continue

    except ValueError:
        print('You can only write numbers\n')
        continue