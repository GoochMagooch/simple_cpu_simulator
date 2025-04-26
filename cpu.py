# list of instructions for validity checks
instruction_set = ["LOAD", "MUL", "DIV", "ADD", "SUB", "PRINT", "HALT", "STORE", "LOADVAR"]

# function that runs basic instructions
def run_cpu(instructions):
    reg_output = []
    register = 0

    # checks for empty instructions list
    if not instructions:
        return "Error: no instructions given, ending program..."
    
    # checks for valid instructions
    for i in instructions:
        if " " in i:
            if i[0:i.index(" ")] not in instruction_set:
                if reg_output:
                    return reg_output + [f"Error: invalid instruction - {i[:i.index(' ')]}"]
                else:
                    return f"Error: invalid instruction - {i[:i.index(' ')]}"
        else:
            if i not in instruction_set:
                if reg_output:
                    return reg_output + [f"Error: invalid instruction - {i[:i.index(' ')]}"]
                else:
                    return f"Error: invalid instruction - {i[:i.index(' ')]}"

    # checks for initial register
    if not instructions[0].startswith("LOAD"):
        return "Failed to load integer: Set 'LOAD x' as first instruction."
    else:
        register = int(instructions[0][instructions[0].index(" ")+1:])
    
    # checks for multiple registers
    for i in range(1, len(instructions)):
        if " " in instructions[i]:
            if instructions[i][0:instructions[i].index(" ")] == "LOAD":
                if reg_output:
                    return reg_output + ["Error: cannot load multiple registers - program was halted"]
                else:
                    return "Error: cannot load multiple registers - program was halted"
        else:
            if instructions[i] == "LOAD":
                if reg_output:
                    return reg_output + ["Error: cannot load multiple registers - program was halted"]
                else:
                    return "Error: cannot load multiple registers - program was halted"
            
    # runs instructions against loaded register
    stored = {}
    for i in instructions[1:]:
        if i == "HALT":
            return reg_output + ["Program was halted"]
        elif i == "PRINT":
            reg_output.append(register)
        elif i.startswith("MUL"):
            register *= int(i.split()[1])
        elif i.startswith("DIV"):
            try:
                register //= int(i.split()[1])
            except ZeroDivisionError:
                if reg_output:
                    return reg_output + ["Error: cannot divide register by 0 - program was halted"]
                else:
                    return "Error: cannot divide register by 0 - program was halted"
        elif i.startswith("ADD"):
            register += int(i.split()[1])
        elif i.startswith("SUB"):
            register -= int(i.split()[1])
        elif i.startswith("STORE"):
            stored[i.split()[1]] = register
        elif i.startswith("LOADVAR"):
            try:
                register = stored[i.split()[1]]
            except KeyError:
                if reg_output:
                    return reg_output + [f"Variable '{i.split()[1]}' not found, program was halted"]
                else:
                    return f"Variable '{i.split()[1]}' not found, program was halted"
    return reg_output
 
store_loadvar_test = ["LOAD 20", "PRINT", 
                      "STORE x", "ADD 5", "PRINT", 
                      "LOADVAR x", "PRINT", 
                      "ADD 10", "PRINT", 
                      "STORE y", "ADD 20", "PRINT", 
                      "LOADVAR x", "PRINT", 
                      "LOADVAR e", "PRINT", 
                      "HALT"] # should return [20, 25, 20, 30, 50, 20, "Variable 'e' not found", 20, "Program was halted"]
store_loadvar_emptylst_test = ["LOAD 20", 
                      "STORE x", "ADD 5", 
                      "LOADVAR x", 
                      "ADD 10", 
                      "STORE y", "ADD 20", 
                      "LOADVAR x", 
                      "LOADVAR e", "PRINT", "HALT"] # should return "Variable 'e' not found, program was halted"
 
print(run_cpu(store_loadvar_test))
print(run_cpu(store_loadvar_emptylst_test))