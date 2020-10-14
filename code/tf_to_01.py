from ast import literal_eval

with open('./rom_code/output.txt') as f:
    lines = f.read().splitlines()

output = open('./rom_code/compare.hack', 'w+')

for line in lines:
    line = line.split(' ')
    line = [0 if bit == 'False' else 1 for bit in line]
    line = ''.join(str(bit) for bit in line)
    output.write(line + '\n')

output.close()
