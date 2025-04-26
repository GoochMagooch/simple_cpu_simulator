# list of instructions for validity checks
instruction_set = ["LOAD", "MUL", "DIV", "ADD", "SUB", "PRINT", "END", "STORE", "LOADVAR"]

# function that runs basic instructions
def run_cpu(instructions):
    reg_output = []
    register = 0

    # checks for empty instructions list
    if not instructions:
        return "Error: no instructions given"
    
    # checks for valid LOAD placement, valid register or missing register
    first_ins = instructions[0]
    if not first_ins.startswith("LOAD"):
        return "Failed to load register: Set 'LOAD x' as first instruction."
    else:
        if " " in first_ins:
            if len(first_ins.split()) == 1:
                return "Error: missing register value - Set register with 'LOAD x'"
            else:
                if not first_ins[first_ins.index(" ")+1:].isdigit():
                    return f"Error: load int as register value"
                else:
                    register = int(instructions[0][instructions[0].index(" ")+1:])
        else:
            return "Format error: Set LOAD instruction as 'LOAD x'"
    
    # checks for valid instructions
    for i in instructions[1:]:
        if " " in i:
            if i[:i.index(" ")] not in instruction_set:
                return f"Error: invalid instruction - {i[:i.index(' ')]}"
            elif i[-1] == " ":
                return "Error: Remove space from end of instruction - {i}"
        else:
            if i not in instruction_set:
                return f"Error: invalid instruction - {i[:i.index(' ')]}"
    
    # checks for multiple registers
    for i in instructions[1:]:
        if " " in instructions:
            if i.split()[0] == "LOAD":
                return "Error: cannot load multiple registers - program was halted"
        else:
            if i == "LOAD":
                return "Error: cannot load multiple registers - program was halted"
            
    # runs instructions against loaded register
    stored = {}
    for i in instructions[1:]:
        if i == "END":
            return reg_output + ["Program successfully ended"]
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

# Instructions for testing
testing = ["LOAD 20", "STORE x", "ADD 5", "LOADVAR x", 
           "ADD 10", "STORE y", "ADD 20", 
           "LOADVAR x", "PRINT", "END"]
 
print(run_cpu(testing))