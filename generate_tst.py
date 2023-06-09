import itertools, sys

def generate_tst(chip_name: str, num_inputs: int) -> None:

    tst = open(chip_name + ".tst", "w")
    tst.writelines("load " + chip_name + ".hdl;\n\n")

    # Generate a list of all input names
    chip_inputs: list = [];
    for i in range(num_inputs):
        new_input: chr = chr(97 + i) # 97 ASCII val for "a"
        chip_inputs.append(new_input)

    # Generate a list of all permutations for all inputs
    permutations: list = list(itertools.product([0, 1], repeat=num_inputs))

    # Smash them together
    result: list = []
    for perm in range(len(permutations)):
            current_perm: list = []
            for input in range(num_inputs):
                current_perm.append("set " + chip_inputs[input] + " " + str(permutations[perm][input])+ ", ")
            current_perm.append("eval;\n")
            result.append(current_perm)
    
    # Write lines to file
    for line in result:
         tst.writelines(line)
    tst.close()

_chip_name = sys.argv[1]
_num_inputs = int(sys.argv[2])

generate_tst(_chip_name, _num_inputs)
print("Generating tst file for %s.hdl using %i inputs ..."%(_chip_name, _num_inputs))
print("Done!")