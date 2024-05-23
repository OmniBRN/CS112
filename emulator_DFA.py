from header import load_file_content
from header import get_section_list
from header import get_section_content
from FAChecker import dfa_checker
# fa o functie de verificare a documentului

dfa_checker("input.txt")


dictionary = {}
content = load_file_content("input.txt")
for x in get_section_list(content):
    if x == "Delta":
        dictionary[x] = {}
        randuri = get_section_content(x, content)
        for rand in randuri:
            rand = rand.split(' ')
            dictionary[x][rand[0] + '_' + rand[1]] = rand[2]
    else:
        dictionary[x] = get_section_content(x, content)

print(dictionary)



currentState = dictionary["Init"][0]
print(f"Starea initiala este: {currentState}")
string = input()
for x in string:
    key = currentState + '_' + x
    formerState = currentState
    currentState = dictionary["Delta"][key]
    print(f"{formerState} --> {currentState}")
if currentState not in dictionary["Finals"]:
    print("Stringul nu este acceptat de DFA")
else:
    print("Stringul este acceptat de DFA")