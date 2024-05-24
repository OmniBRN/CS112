from header import load_file_content
from header import get_section_list
from header import get_section_content

def dfa_checker(filename):
    trip = 0
    section_name = {"Sigma", "States", "Init", "Finals", "Delta"}
    try:
        
            f = open(filename)
            f.close()
        
    except:
        
            print("FILE IS MISSING")
            return -1
        
    content = load_file_content(filename)
    sections = get_section_list(content)
    for x in section_name:
        if x not in sections:
            print(x + " section is missing")
            trip = 1
        elif len(get_section_content(x, content)) == 0:
            print(x + " section is empty")
            trip = 1
    if trip == 1:
        return -1
    stari = get_section_content("States", content)
    alfabet = get_section_content("Sigma", content)
    init = get_section_content("Init", content)
    if len(init) > 1:
        print("Trebuie sa fie exact o stare initial")
        trip = 1
    if str(init[0]) not in stari:
        print(str(init[0]) + " not in States section")
        return -1
    
    for x in get_section_content("Delta", content):
        x = x.split(' ')
        if x[0] not in stari:
            print(x[0] + " not in States section")
            trip = 1
        if x[2] not in stari:
            print(x[0] + " not in States section")
            trip = 1
        if x[1] not in alfabet:
            print(x[1] + " not in Sigma section")
            trip = 1
    if trip == 1:
        return -1;   
    
    return 1

# def nfa_checker(filename):
#     trip = 0
#     section_name = {"Sigma", "States", "Init", "Finals", "Delta"}
#     try:
        
#             f = open(filename)
#             f.close()
        
#     except:
        
#             print("FILE IS MISSING")
#             return -1
        
#     content = load_file_content(filename)
#     sections = get_section_list(content)
#     for x in section_name:
#         if x not in sections:
#             print(x + " section is missing")
#             trip = 1
#         elif len(get_section_content(x, content)) == 0:
#             print(x + " section is empty")
#             trip = 1
#     if trip == 1:
#         return -1
    
def cfg_checker(filename):
    cfgContent = load_file_content(filename)
    cfgList = get_section_list(cfgContent)
    cfgNT = get_section_content(cfgList[0], cfgContent)
    cfgT= get_section_content(cfgList[1], cfgContent)
    cfgPR = get_section_content(cfgList[2], cfgContent)
    cfgS = get_section_content(cfgList[3], cfgContent)

    # Modifica lista de production rules ca sa fie mai usor de verificat
    for i , x in enumerate(cfgPR):
        x = x.split(" ")
        cfgPR[i] = x
    
    for i, x in enumerate(cfgPR):
        x[2] = x[2].split('+')
        cfgPR[i][2] = x[2]



    # Verifica daca variabila din stanga sagetii este nonterminal sau daca nu apartine multimii de terminali
    for x in cfgPR:
        if x[0] not in cfgNT:
            print("elementul " + x[0] + " nu apartine multumii nonterminalilor")
            return 0

    # Verifica daca prima regula il are la stanga pe starter
    if cfgPR[0][0] not in cfgS:
        print("elementul " + cfgPR[0][0] + " nu este starter")
        return 0
    
    # Verifica daca variabilele din dreapta sagetii sunt terminali daca sunt cu litera mica sau nonterminali daca sunt cu litera mare
    for x in cfgPR:
        for y in x[2]:
            if(y.isupper()):
                if y not in cfgNT:
                    print("elementul \"" + y + "\" nu este in lista de nonterminali")
                    return 0
            else:
                if y not in cfgT:
                    if y != 'e':
                        print("elementul \"" + y + "\" nu este in lista de terminali")
                        return 0

    # Verifica daca toate variabilele folosite in dreapta sunt declarate
    listaNTfolositi = []
    for i in enumerate(cfgPR):
        listaNTfolositi.append(cfgPR[i[0]][0])
    
    listaNTfolositi = list(set(listaNTfolositi))
    for x in cfgPR:
        for y in x[2]:
            if(y.isupper()):
                if y not in listaNTfolositi:
                    print("elementul \"" + y + "\" nu are o regula de productie")

    # Verifica daca sunt mai multe puncte de start
    if(len(cfgS) != 1):
        print("Prea multe variabilele de start")
        return 0

    return 1

def pda_checker(filename):
    pdaContent = load_file_content(filename)
    pdaList = get_section_list(pdaContent)
    pdaStates = get_section_content(pdaList[0], pdaContent)
    pdaInput = get_section_content(pdaList[1], pdaContent)
    pdaStack = get_section_content(pdaList[2], pdaContent)
    pdaS = get_section_content(pdaList[4], pdaContent)
    pdaEnd = get_section_content(pdaList[5], pdaContent)
    pdaTransitions = get_section_content(pdaList[3], pdaContent)
    for i, x in enumerate(pdaTransitions):
        x = x.split(" ")
        pdaTransitions[i] = x
    #Verific daca elementele din tranzitie apar in multimea de stari
    for x in pdaTransitions:
        if x[0] not in pdaStates:
            print(f"{x[0]} not in States section")
            return 0
        if x[2] not in pdaStates:
            print(f"{x[2]} not in States section")
            return 0
    
    #Verific daca elementele puse/scoase din Stiva apartin sectiunii stack
    for x in pdaTransitions:
        if x[3] not in pdaStack:
            if x[3] != 'e':
                print(f"{x[3]} not in Stack section")
                return 0
        if x[4] not in pdaStack:
            if x[4] != 'e':
                print(f"{x[4]} not in Stack section")
                return 0
            
    #Verific daca elementele de tranzitie apartin sectiunii input
    for x in pdaTransitions:
        if x[1] not in pdaInput:
            if x[1] != 'e':
                print(f"{x[1]} not in input section")
                return 0
        
    #Verifica daca elementul de start este doar unul
    if len(pdaS) > 1:
        print("Too many elements in the start section")
        return 0
    