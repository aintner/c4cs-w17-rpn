#!/usr/bin/env python3
import operator


operators = {
    "+":operator.add,
    "-":operator.sub
}

def calculate(arg):
    stack = list()
    for operand in arg.split():
        try:
            operand = float(operand)
            stack.append(operand)
        except ValueError:
            arg2 = stack.pop()
            arg1 = stack.pop()
            stack.append(operators[operand](arg1, arg2))
    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> "))
        print("Result is :" + str(result))


if __name__ == '__main__': # Note: that's "underscore underscore n a m e ..."
    main()
