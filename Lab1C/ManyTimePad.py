import sys

inFile = sys.argv[1]

with open(inFile, 'r') as f:
    lines = f.read()

messages = lines.split("\n\n")

binary_list = []
new_list = []
for line in messages:
    line = ''.join(line.split())

    new_list.append(line)
    
    # Source - https://stackoverflow.com/a/4859937
    # Posted by Onedinkenedi, modified by community. See post 'Timeline' for change history
    # Retrieved 2026-10-01, License - CC BY-SA 3.0
    scale = 16 ## equals to hexadecimal

    num_of_bits = 8

    binary_list.append(bin(int(line, scale))[2:].zfill(num_of_bits))

print(new_list)

# Source - https://stackoverflow.com/a/19414115
# Posted by Robᵩ, modified by community. See post 'Timeline' for change history
# Retrieved 2026-10-01, License - CC BY-SA 4.0

y = int(binary_list[0], 2) ^ int(binary_list[1], 2)

