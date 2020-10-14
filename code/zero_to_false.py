from ast import literal_eval

with open('./rom_code/output.txt') as f:
    lines = f.read().splitlines()

output = open('./rom_code/compare.hack', 'w+')

for line in lines:
    line = [False if bit == '0' else True for bit in line]
    line = ' '.join(str(bit) for bit in line)
    output.write(line + '\n')

output.close()
