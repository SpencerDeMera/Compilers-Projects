LRTable = [
    ['', 'i', '+', '-', '*', '/', '(', ')', '$', 'E', 'T', 'F'],
    ['0', 'S5', '', '', '', '', 'S4', '', '', '1', '2', '3'],
    ['1', '', 'S6', 'S7', '', '', '', '', 'ACC', '', '', ''],
    ['2', '', 'R3', 'R3', 'S8', 'S9', '', 'R3', 'R3', '', '', ''],
    ['3', '', 'R6', 'R6', 'R6', 'R6', '', 'R6', 'R6', '', '', ''],
    ['4', 'S5', '', '', '', 'S4', '', '', '', '10', '2', '3'],
    ['5', '', 'R8', 'R8', 'R8', 'R8', '', 'R8', 'R8', '', '', ''],
    ['6', 'S5', '', '', '', '', 'S4', '', '', '', '11', '3'],
    ['7', 'S5', '', '', '', '', 'S4', '', '', '', '12', '3'],
    ['8', 'S5', '', '', '', '', 'S4', '', '', '', '', '13'],
    ['9', 'S5', '', '', '', '', 'S4', '', '', '', '', '14'],
    ['10', '', 'S6', 'S7', '', '', '', 'S15', '', '', '', ''],
    ['11', '', 'R1', 'R1', 'S8', 'S9', '', 'R1', 'R1', '', '', ''],
    ['12', '', 'R2', 'R2', 'S8', 'S9', '', 'R2', 'R2', '', '', ''],
    ['13', '', 'R4', 'R4', 'R4', 'R4', '', 'R4', 'R4', '', '', ''],
    ['14', '', 'R5', 'R5', 'R5', 'R5', '', 'R5', 'R5', '', '', ''],
    ['15', '', 'R7', 'R7', 'R7', 'R7', '', 'R7', 'R7', '', '', ''],
]

CFG = {
    'E+T': 'E -> E + T', 'E-T': 'E -> E - T', 'T': 'E -> T',
    'T*F': 'T -> T * F', 'T/F': 'T -> T / F', 'F': 'T -> F',  
    '(E)': 'F -> (E)', 'i': 'F -> i',
}

inputs = ['i', 'S', 'E', 'T', 'F']
operators = ['+', '-', '*', '/', '(', ')']
prods = {
    1: ['E', 'E+T'],
    2: ['E', 'E-T'],
    3: ['E', 'T'],
    4: ['T', 'T*F'],
    5: ['T', 'T/F'],
    6: ['T', 'F'],
    7: ['F', '(E)'],
    8: ['F', 'i']
}

rows = {'0': 1, '1': 2, '2': 3, '3': 4, '4': 5, '5': 6, '6': 7, '7': 8, '8': 9, '9': 10, '10': 11, '11': 12, '12': 13, '13': 14, '14': 15, '15': 16}
cols = {'i': 1, '+': 2, '-': 3, '*': 4, '/': 5, '(': 6, ')': 7, '$': 8, 'E': 9, 'T': 10, 'F': 11}

def trace(inputStr):
    accept = 'ACCEPTED'
    inputStr = inputStr.replace(' ', '')

    # Init buffers
    OPStackBuffer = [0]
    inBuffer = inputStr
    actionsBuffer = []
    productBuffer = ''

    # Matrix Manipulators
    colNum = 0
    rowNum = 0
    index = 0

    # Runs while error flag != False
    while True:
        # Generates stack information
        top = OPStackBuffer[len(OPStackBuffer) - 1]
        nextInput = inputStr[index]
        rowNum = rows[str(top)]
        colNum = cols[nextInput]
        actionsBuffer = LRTable[rowNum][colNum]

        # Readjusts buffer arrays to strings
        currStackBuffer = ''.join(str(a) for a in OPStackBuffer)
        currActionsBuffer = ''.join(str(c) for c in actionsBuffer)

        # If not excepted / invalid state
            # Provides error message for production at index rowNum, colNum
        if actionsBuffer == '':
            stackRow('| ' + currStackBuffer, '| ' + inBuffer, '| ERROR', '| No Production for [' + currStackBuffer[-1] + ', ' + inBuffer[0] + ']')
            return False
        # Shifts
        elif actionsBuffer[0] == 'S':
            OPStackBuffer.append(nextInput)
            OPStackBuffer.append(actionsBuffer[1:])
            index += 1
            productBuffer = '' # reset product buffer

            stackRow('| ' + currStackBuffer, '| ' + inBuffer, '| ' + currActionsBuffer, '| ' + productBuffer)

            # Decrements the input buffer
            inBuffer = inBuffer[1:]
        # Reductions
        elif  actionsBuffer[0] == 'R':
            # Finds the productions 
            idents = prods[int(actionsBuffer[1:])][0]
            product = prods[int(actionsBuffer[1:])][1]

            productBuffer = CFG[product]

            stackRow('| ' + currStackBuffer, '| ' + inBuffer, '| ' + currActionsBuffer, '| ' + productBuffer)

            # Incrementing for poping values off the stack
            for i in range(0, (len(product) * 2)):
                OPStackBuffer.pop()

            # Realigns tops of the stack
            topNew = OPStackBuffer[len(OPStackBuffer) - 1]
            OPStackBuffer.append(idents)
            rowNum = rows[str(topNew)]
            colNum = cols[str(idents)]
            OPStackBuffer.append(LRTable[rowNum][colNum])
        # If accepted state
        elif actionsBuffer == 'ACC':
            stackRow('| ' + currStackBuffer, '| ' + inBuffer, '| ' + currActionsBuffer, '| ' + accept)
            return True

def stackRow(stack, inputStr, action, production):
    print("{:25s} {:15s} {:15s} {:15s}".format(stack, inputStr, action, production))

if __name__ == '__main__':
    # This program traces the input of an input string using an SLR Parser
    # This program displays the full trace of a strings processing using 
        # the stack, input, actions, and productions

        # i*(i/i)$ is accepted
        # i(i/i)$ is not accepted

    flag = True

    while flag:
        userInput = input("\nEnter a string: ")
        print()

        # Checks for ending with $
        if userInput[-1] == "$":
            # Formatting for Stack table
            stackRow('| Stack', '| Input', '| Action', '| Production')
            print('|' + '-' * 25 + '|-' + '-' * 14 + '|-' + '-' * 14 + '|-' + '-' * 15)

            # Call trace function
            acceptFlag = trace(userInput)

            if acceptFlag:
                print("\nString " + userInput + " Was Accepted")
            else:
                print("\nString " + userInput + " Was Not Accepted")
        else:
            print("Your input must end with a \'$\'\n")
        print()

        con = input("CONTINUE (y/n) ? ")
        if con == "n":
            flag = False
    print()