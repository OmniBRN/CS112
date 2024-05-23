import os
def load_file_content(file_name):
    try:
        f = open(file_name)
        f.close()
    except:
        print("file not found")
        return "file not found" 
    solutie = []
    with open(file_name, "r") as file:
        for line in file.readlines():
            if '#' not in line and line != "": 
                solutie.append(line.removesuffix('\n').rstrip())
        return list(filter(None, solutie))
def get_section_list(content):
    # baga inline comment
    solutie = []
    for x in content:
        x = x.rstrip()
        if x[0] == "[" and x[-1] == "]":
            x = x.removeprefix("[")
            x = x.removesuffix("]")
            solutie.append(x)
    if len(solutie) == 0:
        print("There are no sections in content")
        return 
    return solutie           
def get_section_content(name, content):
    
    solutie = []
    inceput = content.index("[" + name + "]")
    final = content[inceput::].index("END") + len(content) - len(content[inceput::])
    for i in range(inceput+1, final):
        solutie.append(content[i])
    return solutie


