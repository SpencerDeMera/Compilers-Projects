def process():
    reservedWords = ["cout<<", "for", "int", "while"]
    special = ["<", "=", "*", "-", "+", ";", "(", ")", "<=", "++", ","]
    flag = True

    while flag:
        userInput = input("Enter your statement: ")
        print()
        res = userInput.split()

        for token in res:
            if token.lower() in reservedWords:
                print(token + " reserved word")
            elif token in special:
                print(token + " special symbol")
            elif token.isnumeric():
                print(token + " number")
            elif token[0] == "-" and token[1].isnumeric():
                print(token + " number")
            elif token[0] == "_" or token[0].isalpha():
                print(token + " identifier")
            else:
                print(token + " not identifier")

        con = input("\nCONTINUE (y/n) ? ")
        if con == "n":
            flag = False

if __name__ == '__main__':
    # This program tokeninzes a given input string
        # seprates into numbers, letters, identifiers, reserved words, etc
        # separated list is printed to console

        # Example string: for ( int i = 0 ; i < 10 ; i ++ ) ;

    print("\nProcessing...\n")
    process()
    print("\nFinished Processing...\n")