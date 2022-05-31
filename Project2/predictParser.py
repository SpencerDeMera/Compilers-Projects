PT = [
    ['', 'a', '+', '-', '*', '/', '(', ')', '$'],
    ['E', 'TQ', '', '', '', '', 'TQ', '', ''],
    ['Q', '', '+TQ', '-TQ', '', '', '', 'ε', 'ε'],
    ['T', 'FR', '', '', '', '', 'FR', '', ''],
    ['R', '', 'ε', 'ε', '*FR', '/FR', '', 'ε', 'ε'],
    ['F', 'a', '', '', '', '', '(E)', '', ''],
]

rows = {'E': 1, 'Q': 2, 'T': 3, 'R': 4, 'F': 5}
cols = {'a': 1, '+': 2, '-': 3, '*': 4, '/': 5, '(': 6, ')': 7, '$': 8}

def trace(inputStr):
    accept = 'ACCEPTED'
    reject = 'FAILED'
    inputStr = inputStr.replace(' ', '')

    # Init buffers
    stackBuffer = '$'
    inBuffer = inputStr
    moveBuffer = ''

    first = True
    colNum = 0
    rowNum = 0

    while True:
        if first:
            for i in range(0, 8):
                if inBuffer[0] == PT[0][i]:
                    colNum = i
                    rowNum = 1

            moveBuffer = moveBuffer + PT[rowNum][colNum]
            stackRow('| ' + stackBuffer, '| ' + inBuffer, '| ' + moveBuffer)

            first = False
        else:
            if moveBuffer[0] == inBuffer[0]:
                stackBuffer = stackBuffer + inBuffer[0]
                inBuffer = inBuffer[1:]
                moveBuffer = moveBuffer[1:]
                stackRow('| ' + stackBuffer, '| ' + inBuffer, '| ' + moveBuffer)
            else:
                while moveBuffer[0] != inBuffer[0] and moveBuffer[0] != '':
                    if moveBuffer[0] == 'ε':
                        moveBuffer = moveBuffer[1:]
                        stackRow('| ' + stackBuffer, '| ' + inBuffer, '| ' + moveBuffer) 
                    else:
                        rowNum = rows[moveBuffer[0]] # Gets row number to be in
                        colNum = cols[inBuffer[0]] # Gets column number to be in
                        moveBuffer = moveBuffer[1:]
                        moveBuffer = PT[rowNum][colNum] + moveBuffer
                        stackRow('| ' + stackBuffer, '| ' + inBuffer, '| ' + moveBuffer)

                    if moveBuffer == '' and len(inBuffer) == 1: 
                        stackRow('| ' + accept, '| ' + accept, '| ' + accept)
                        return
                    elif moveBuffer == '' and len(inBuffer) > 1:
                        stackRow('| ' + reject, '| ' + reject, '| ' + reject)
                        return

def stackRow(stack, inputStr, move):
    print("{:15s} {:15s} {:15s}".format(stack, inputStr, move))

if __name__ == '__main__':
    # This program makes use of a predictive parser to trace a string
    # Program outputs full stack trace of the string with productions and actions
        # Input strings must end with $

        # a*a is accepted
        # a(a+a$ is not accepted

    flag = True

    while flag:
        userInput = input("\nEnter a string: ")
        print()

        # Checks for ending with $
        if userInput[-1] == "$":
            # Formatting for Stack table
            stackRow('| Stack', '| Input', '| Moves')
            print('|' + '-' * 15 + '|-' + '-' * 14 + '|-' + '-' * 15)

            # Call trace function
            trace(userInput)
        else:
            print("Your input must end with a \'$\'\n")
        print()

        con = input("\nCONTINUE (y/n) ? ")
        if con == "n":
            flag = False
    print()
