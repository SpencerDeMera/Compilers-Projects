def process():
    # Processing function
    keywords = ["int", "float", "bool", "double", "char", "short", "cout<<", "if", "else", "break", "else if", "while", "do", "for", "try", "catch", "&&", "||", "<=", ">=", "==", "!=", "++", "--"]
    operators = ["=", "+", "-", "*", "/", "%","<", ">"]
    seperators = [":", ",", "(", ")", "{", "}", "[", "]","'",".","$"]
    semiColon = ";"
    angle = "<"
    mainLineArr = []
    minorLineArr = []
    tempLineBuffer = []
    strArr = []

    f = open("data.txt", "r")
    lines = f.readlines()
    
    for line1 in lines:
        # Strip newline char read in from file
        line1 = line1.rstrip("\n")

        # Strips off same-line comments && extra spaces
        line1 = line1.split("//", 1)
        newLine = line1[0]
        newLine = newLine.split(";")
        parsedToken = ""

        for line2 in newLine:
            # removes extra blank lines or comment lines
            if line2.strip():
                # Add semi colon to end of each line
                line2 = line2 + ';'

                for token in line2:
                    if token in keywords:
                        minorLineArr.append('{:^3}'.format(token))
                    else:
                        for char in token:
                            if char in seperators or char in operators and char != angle:
                                strArr.append('{:^3}'.format(char))
                            elif char == semiColon:
                                strArr.append('{:>3}'.format(char))
                            elif char == angle:
                                strArr.append('{:>1}'.format(char))
                            else:
                                strArr.append(char)

                        parsedToken = "".join(strArr)

                        # Remove dubplicate spaces
                        parsedToken = " ".join(parsedToken.split())
                    minorLineArr.append('{:^3}'.format(parsedToken))

    f.close()
    n = open("newdata.txt", "w")
    n.truncate()

    # Gets last index of processed data
        # Inefficient as hell but I don't have enough time to find a better solution 😕
    tempLineBuffer.append(minorLineArr[-1])
    newLine = tempLineBuffer[0].split(";")

    for line in newLine:
        if line.strip():
            line = " ".join(line.split())
            print(line + ' ;')
            n.write(line + ' ;' + '\n')
    n.close()

if __name__ == '__main__':
    # This program optimizes and reprints text input from data.txt file
    # All ambiguous code is removed (comments, extra spaces, newlines, etc) and 
        # rewritten into newdata.txt

    print("\nProcessing data.txt...\n")
    process()
    print("\nFinished Processing data.txt...\nCheck newdata.txt\n")