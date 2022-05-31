def parse(inputStr):
    finalVal = 0
    userStr = []
    identifiers = []
    numStr = userStr
    stack = [] # stack for pushing and popping postfix

    userStr[:] = inputStr

    # Replaces identifiers with values
    for token in userStr:
        if token.isalpha() and not (token in identifiers):
            identifiers.append(token)

    for ident in identifiers:
        val = input("   Enter the value of " + ident + " : ")
        # replace every identifier with its respective value
        numStr[:] = [x if x != ident else val for x in numStr]

    # Swicth cases for operators
    for i in range(len(inputStr)):
        if numStr[i].isdigit(): # push until get to an operator
            stack.append(int(numStr[i]))
        elif numStr[i] == '+':
            temp1 = stack.pop()
            temp2 = stack.pop()
            stack.append(int(temp1) + int(temp2))
        elif numStr[i] == '-':
            temp1 = stack.pop()
            temp2 = stack.pop()
            stack.append(int(temp1) - int(temp2))
        elif numStr[i] == '*':
            temp1 = stack.pop()
            temp2 = stack.pop()
            stack.append(int(temp1) * int(temp2))
        elif numStr[i] == '/':
            temp1 = stack.pop()
            temp2 = stack.pop()
            stack.append(int(temp1) / int(temp2))
    
    finalVal = stack.pop()
    print("\tFinal value = " + str(finalVal))

if __name__ == '__main__':
    # This program processes and solves psotfix notation equations
    # When a postfix equation is entered, you will be asked to fill
        # in the values of the variables in the equation
    # The input string must end with $

        # Example: ab*a+$ will equal 15
            # 34*3+=15 OR (3*4)+3 = 15


    flag = True

    while flag:
        userInput = input("\nEnter a postfix expression with a $ at the end : ")
        userInput = userInput.replace(' ', '')

        # Checks for ending with $
        if userInput[-1] == "$":
            # Call parse function
            parse(userInput)
        else:
            print("Your input must end with a \'$\'\n")

        con = input("\nCONTINUE (y/n) ? ")
        if con == "n":
            flag = False
    print()