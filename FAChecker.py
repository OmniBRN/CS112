from header import load_file_content
from header import get_section_list
from header import get_section_content

def dfa_checker(filename):
    #trebuie sa verifici daca sunt mai mult decat 5 sectiuni
    #trebuie sa verifici ca toate starile din [Finals] se afla in sectiunea [States]
    #trebuie sa numeri ca sunt 3 elemente pe un rand in sectiunea [Delta]
    #trebuie sa verifica sunt nrStari*nrLitereAlfabet linii in sectiunea [Delta]
    #trebuie sa verifici ca nu se repeta
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
    if init not in stari:
        print(init + " not in States section")
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
    

def nfa_checker(filename):
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
    
    # Verifica daca variabilele din dreapta sagetii sunt terminali daca sunt cu litera mic sau nonterminali daca sunt cu litera mare
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




    
   
        
    
