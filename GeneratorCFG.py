from header import load_file_content
from header import get_section_list
from header import get_section_content
from FAChecker import cfg_checker
import random


#Functia returneaza stringul din dreapta nonterminalului dupa ce este aleasa aleatoriu
def randomRule(cfgPR, cfgS):
    listCompatiblePR = []
    for x in cfgPR:
        if cfgS == x[0]:
            listCompatiblePR.append(x)
    aleatoriu = random.randint(0, len(listCompatiblePR)-1)
    meme = "".join(listCompatiblePR[aleatoriu][1])
    return meme

#returneaza prima litera mare
def returnFirstUpper(string):
    for c in string:
        if c.isupper():
            return c
    

def main():
    content = load_file_content("./inputs/input_cfg.txt")
    sectionList = get_section_list(content)
    cfgNT = get_section_content(sectionList[0], content)
    cfgT = get_section_content(sectionList[1], content)
    cfgPR = get_section_content(sectionList[2], content)
    cfgS = get_section_content(sectionList[3], content)[0]
    for i, x in enumerate(cfgPR):
        x = x.split(" => ")
        cfgPR[i] = x;
    for x in cfgPR:
        x[1] = x[1].split('+')
    nr = 0
    solutie = ""
    while(nr < 100):
        meme = randomRule(cfgPR, cfgS)
        if(solutie == ""):
            if meme == 'e':
                print("Empty", end="")
                break
            else:
                solutie = meme
                cfgS = returnFirstUpper(solutie)    
        else:
            if meme == 'e':
                solutie = solutie.replace(cfgS, "")
                break
            solutie = solutie.replace(cfgS, meme)
            for c in solutie:
                cfgS = returnFirstUpper(solutie)
        nr += 1
    print(solutie)
    for c in solutie:
        if c.isupper(): 
            solutie = solutie.replace(c, "")





if(cfg_checker("./inputs/input_cfg.txt")):
    print("How many words do you want to generate?")
    nr = int(input())
    for i in range(nr):
        main()