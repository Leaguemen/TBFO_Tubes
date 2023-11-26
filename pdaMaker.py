from Tokenizer import *

start_input = ""  # input word to be found or not found
found = False  # stores found state
accepted_config = []  # here we will post the end configuration that was accepted

# production rules ("read input", "pop stack", "push stack", "next state")
arrProdRule =[]

# start state
current_state = ""

# start stack symbol
stack = []

# list of acceptable states
acceptable_states = []

# E - accept on empty stack or F - acceptable state (default is false)
accept_with = ""

def head(stack):
    return stack[len(stack)-1]
    
def find_index(first_three_elements):
    global arrProdRule
    for i, rule in enumerate(arrProdRule):
        if rule[:3] == first_three_elements:
            return i
    return -1 

def split_string_into_words(input_string):
    words = input_string.split(',')
    return words

#main

file = open("pda.txt", "r")
lines =[line.rstrip().split() for line in file]
current_state = lines[3][0]
pda_stack = [lines[4][0]]
acceptCondition = pda_stack
acceptable_states = lines[5] #sebuah array
accept_with = lines[6][0]

#tambah rule
for i in range(7,len(lines)):
    production = lines[i]
    arrProdRule.append(tuple((production[0], production[1], production[2], production[3], production[4])))



#input ada di sini
# print(arrProdRule)
tokens= createToken("html/inputAcc.txt")
print(tokens)
# tokens = [0,0,0,"e",1,1,1]
# generate(start_symbol, start_input, start_stack, (start_symbol, start_input, start_stack))

i = 0
length = len(tokens)

while i < length:
    print("\n\nSTACK\n", pda_stack, "\n")
    first_three_elements = (current_state,str(tokens[i]),head(pda_stack))
    rule_index = find_index(first_three_elements)
    print(first_three_elements)
    if  rule_index != -1:
        current_state = arrProdRule[rule_index][3]
        if ',' in arrProdRule[rule_index][4]:
            string_split = split_string_into_words(arrProdRule[rule_index][4])
            if head(pda_stack) != string_split[1]:
                pda_stack.pop()
                pda_stack.append(string_split[1])
                pda_stack.append(string_split[0])
            else:
                pda_stack.append(string_split[0])
        else:
            if arrProdRule[rule_index][4] == "e":
                pda_stack.pop()
            else:
                pda_stack.pop()
                pda_stack.append(arrProdRule[rule_index][4])
        i +=1
    else:
        #########################################################
        first_three_elements = (current_state,"e",head(pda_stack))
        rule_index = find_index(first_three_elements)
        if  rule_index != -1:
            current_state = arrProdRule[rule_index][3]
            if ',' in arrProdRule[rule_index][4]:
                string_split = split_string_into_words(arrProdRule[rule_index][4])
                if head(pda_stack) != string_split[1]:
                    pda_stack.pop()
                    pda_stack.append(string_split[1])
                    pda_stack.append(string_split[0])
                else:
                    pda_stack.append(string_split[0])
            else:
                if arrProdRule[rule_index][4] == "e":
                    pda_stack.pop()
                else:
                    pda_stack.pop()
                    pda_stack.append(arrProdRule[rule_index][4])
            print("KENA EPSILON")
        ############################################
        else:
            pda_stack =[]
            break

print(pda_stack)
if pda_stack == acceptCondition:
    print("Accepted")
else:
    print("Not accepted")




