file_name = r"Sample compilation -portuguese_char_frequency.txt"
with open(file_name, 'rt', encoding='utf-8') as file:
    data_input = file.read()

# get the frebquency (in %) for unique characters
lenght = len(data_input)
freq_chars = sorted([[100 * data_input.count(character)/lenght, character] for character in list(set(data_input))])

print('Frequency for each character:')
print(*[f'{str(round(freq, 5)).ljust(7, "0")}%\t "{char}"' for freq, char in freq_chars], sep='\n')

# compute the groups of characters (leaves) and groups of the nodes combining them (branch) until we get one group with all characters (the trunk)
allgroups = []
while freq_chars:
    if len(freq_chars) >= 2:
        old0, old1 = [freq_chars.pop(0) for _ in range(2)]
        allgroups.extend([old0, old1])
        freq_chars = sorted(freq_chars + [[old0[0] + old1[0], old0[1] + old1[1]]])
    else:
        old = freq_chars.pop(0)
        allgroups.append(old)

allgroups = sorted(allgroups, key=lambda x: [-len(x[1]), -x[0]])

# process the bits for each pair (left + right = above node)
left_right = {char: '' for _, char in allgroups}
for freq1, char1 in allgroups:
        for freq2, char2 in allgroups:
            for freq3, char3 in allgroups:
                if char2 + char3 == char1:
                    if char1.startswith(char2):
                        if char1 in left_right:
                            above_bit = left_right[char1]
                            left_right[char2], left_right[char3] = [above_bit, above_bit]
                        left_right[char2] += '0'
                        left_right[char3] += '1'

                            
# sorting bits by lenght, then ascending
left_right = sorted(left_right.items(), key=lambda x: [len(x[1]), x[1]])

# filter the single characters in left_right
conversion_table = {char: binary for char, binary in left_right if len(char) == 1}
print('\nConversion_table: (From the most to the least frequent character')


printables = [f'{binary.ljust(30)}\t{char.ljust(10)}' for char, binary in conversion_table.items() if char.isprintable()]
print('\nPrintables')
print(*printables, sep='\n')

non_printables = [f'{binary.ljust(30)}\t{char.ljust(10)}' for char, binary in conversion_table.items() if not char.isprintable()]
if non_printables:
    print('\nNon printables:\n')
    print(*non_printables, sep='\n')


# compute the converted (encripted) and the binary version for data_input
def encrypt_bin(string, conversion_table):
    return ''.join([bin(ord(char))[2:].rjust(8, '0') for char in string])


def encrypt_cry(string, conversion_table):
    return ''.join([conversion_table[char] for char in string])


# decoding bits
def decrypt(bits, conversion_table):
    temp, decrypted = '', []  # temp, decrypted = '', []: 12,0s | temp, decrypted = [], []:15.0s | temp, decrypted = '', '': 21.9s
    decode_table = {binary_code: character for character, binary_code in conversion_table.items()}
    for bit in bits:
        temp = temp + bit
        if temp in decode_table:
            decrypted.append(decode_table[temp])
            temp = ''
    return ''.join(decrypted)

print('-' * 100)
# process and finish analysis using data_input
print('Encoding to standard 8 bits...')
binary = encrypt_bin(data_input, conversion_table)

print('Encoding binary tree (encryption)...')
crypto = encrypt_cry(data_input, conversion_table)

print('Decoding encrypted bits...')
decrypted = decrypt(binary, conversion_table)
len_cry, len_bin = len(crypto), len(binary)

print('_' * 100, '\nANALYSIS FOR data_input:')
print(f'\nFile name:       {file_name}\n')
print(f'\ndata_input (100 first characters):\n{data_input[:100]}\n')

print(f'data_input type:   {type(data_input)}')
print(f'data_input size:   {lenght:,}b (bytes or characters)')
print(f'Binary size:       {len_bin:,} bits ({round(100 * len_bin / len_bin, 1)}%)\t8.00 bits per character.')
print(f'Cryptography size: {len_cry:,} bits ( {round(100 * len_cry / len_bin, 1)}%)\t{round(len_cry/len(data_input), 2)} bits (average) per character.')

# the real benefit for storage or processing:
print('_' * 100, '\nCONCLUSION:')
print(f'You saved {round((len_bin - len_cry)/8/1024/1024, 5)}MB from {round(len_bin/8/1024/1024, 5)}MB using this encryption method!')
