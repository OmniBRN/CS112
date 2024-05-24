from header import load_file_content
from header import get_section_list
from header import get_section_content
from FAChecker import pda_checker

class stack:
    def __init__(self):
        self.list = []
    def pop(self):
        if(self.isEmpty()):
            return -1
        x = self.list[-1]
        self.list.pop()
        return x
    def push(self, nr):
        self.list.append(nr)
    def top(self):
        if(self.isEmpty()):
            print("Stack is empty")
            return -1
        return self.list[-1]
    def isEmpty(self):
        if len(self.list) == 0:
            return 1

def copyStack(stiva, copieStiva):
    copieStiva.list = []
    for x in stiva.list:
        copieStiva.list.append(x)

def checkStack(stack, variable):
    if stack.isEmpty() and variable == 'e':
        return True
    if stack.top() == variable:
        return True
    return False

def functie(string, currentState, stiva, dictionar, tranzitii, pdaEnd):

    for i, c in enumerate(string):
        for x in tranzitii:
            stivaCopie = stack()
            copyStack(stiva, stivaCopie)
            if x[0] == currentState and x[1] == 'e':
                if x[3] != 'e':
                    if stiva.isEmpty() or stiva.top()!=x[3]:
                        continue
                    else:
                        stivaCopie.pop()
                if x[4] != 'e':
                    stivaCopie.push(x[4])
                if functie(string[i::], x[2], stivaCopie, dictionar, tranzitii, pdaEnd) == 1:
                    return 1
        cheie = currentState + '_' + c
        if cheie in dictionar:
            if dictionar[cheie][1] == 'e':
                currentState = dictionar[cheie][0]
                if dictionar[cheie][2] != 'e':
                    stiva.push(dictionar[cheie][2])
            else:
                if stiva.isEmpty():
                    return 0
                else:
                    if stiva.top() != dictionar[cheie][1]:
                        return 0
                    else:
                        stiva.pop()
                        if dictionar[cheie][2] != 'e':
                            stiva.push(dictionar[cheie][2])
                        currentState = dictionar[cheie][0]
        else:
            return 0
    
    for x in tranzitii:
        if currentState == x[0] and x[1] == 'e':
            if stiva.top() == x[3]:
                stiva.pop()
                currentState = x[2]
    
    if currentState in pdaEnd:
        print("String is valid")
        return 1
    return 0
    



    

def main():
    stiva = stack()
    dictionar = {}
    pdaContent = load_file_content("./inputs/input_PDA2.txt")
    pdaSectionList = get_section_list(pdaContent)
    pdaEnd = get_section_content(pdaSectionList[5], pdaContent)
    pdaTransition = get_section_content(pdaSectionList[3], pdaContent)
    currentState = get_section_content(pdaSectionList[4],pdaContent)[0]

    
    for i, x in enumerate(pdaTransition):
        x = x.split()
        pdaTransition[i] = x
    for x in pdaTransition:
        if x[1]!='e':
            cheie = x[0] +'_'+ x[1]
            element = [x[2], x[3], x[4]]
            dictionar[cheie] = element
    print(dictionar)
    print("Enter string to validate:", end="")
    userInput = input()
    if functie(userInput, currentState, stiva, dictionar, pdaTransition, pdaEnd) == 0:
        print("String is not valid")
    
        
    

if(pda_checker("./inputs/input_PDA2.txt")):
    main()