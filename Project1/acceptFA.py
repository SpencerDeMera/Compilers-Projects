def dfa(s):
    state = 1

    for i in range(len(s)):
        if state == 1:
            if s[i] == 'a':
                state = 2
            elif s[i] == 'b':
                state = 3
            else: 
                state = 0
        elif state == 2:
            if s[i] == 'a':
                state = 2
            elif s[i] == 'b':
                state = 4
            else: 
                state = 0
        elif state == 3:
            if s[i] == 'a':
                state = 0
            elif s[i] == 'b':
                state = 5
            else: 
                state = 0
        elif state == 4:
            if s[i] == 'a':
                state = 6
            elif s[i] == 'b':
                state = 7
            else: 
                state = 0
        elif state == 5:
            if s[i] == 'a':
                state = 6
            elif s[i] == 'b':
                state = 5
            else: 
                state = 0
        elif state == 6:
            if s[i] == 'a':
                state = 0
            elif s[i] == 'b':
                state = 0
            else: 
                state = 0
        elif state == 7:
            if s[i] == 'a':
                state = 6
            elif s[i] == 'b':
                state = 7
            else: 
                state = 0

    if state == 6:
        return "YES"
    return "NO"

if __name__ == '__main__':
    # This program takes in an input string ending with $ and prints whether or not
        # its accepted by the DFA in Project.docx

        # aabba$ is accepted
        # aaababba$ is not accepted

    userInput = input("\nEnter a string: ")

    # Checks for ending with $
    if userInput[-1] == "$":
        userInput = userInput[:-1]
        passed = dfa(userInput)
        print(passed + "\n")
    else:
        print("Your input must end with a \'$\'\n")