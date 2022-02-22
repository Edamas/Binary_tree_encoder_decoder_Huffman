# data_input is the character, symbol, numbers sequence (as input text)

data_input = 100 * ''.join(key * int(100 * value) for key, value in {' ': 15, 'a': 14.63, 'e': 12.57, 'o': 10.73, 's': 7.81, 'r': 6.53, 'i': 6.18, 'n': 5.05, 'd': 4.99, 'm': 4.74, 'u': 4.63, 't': 4.34, 'c': 3.88, 'l': 2.78, 'p': 2.52, 'v': 1.67, 'g': 1.3, 'h': 1.28, 'q': 1.2, 'b': 1.04, 'f': 1.02, 'z': 0.47, 'j': 0.4, 'x': 0.21, 'k': 0.02, 'w': 0.01, 'y': 0.01}.items()) 

# this is the base of our data_input, but you can change it above and print it bellow
print('Portuguese alphabet frequency in %:\n', *{' ': 15, 'a': 14.63, 'e': 12.57, 'o': 10.73, 's': 7.81, 'r': 6.53, 'i': 6.18, 'n': 5.05, 'd': 4.99, 'm': 4.74, 'u': 4.63, 't': 4.34, 'c': 3.88, 'l': 2.78, 'p': 2.52, 'v': 1.67, 'g': 1.3, 'h': 1.28, 'q': 1.2, 'b': 1.04, 'f': 1.02, 'z': 0.47, 'j': 0.4, 'x': 0.21, 'k': 0.02, 'w': 0.01, 'y': 0.01}.items())

print('_' * 100)

# get the frequency (in %) for unique characters
lenght = len(data_input)
frequencies, characters = [], []
for character in data_input:
    if character not in characters:
        characters.append(character)
        count = data_input.count(character)
        frequencies.append(100 * count/lenght)

# always using the ascending frequency of characters order
freq_chars = [[frequencies[index], characters[index]] for index in range(len(characters))]
freq_chars = sorted(freq_chars)

# compute the groups of characters (leaves) and groups of the nodes combining them (branch) until we get one group with all characters (the trunk)
allgroups = []
while freq_chars:
    if len(freq_chars) >= 2:
        old0, old1 = freq_chars.pop(0), freq_chars.pop(0)
        allgroups.extend([old0, old1])
        freq_chars = sorted(freq_chars + [[old0[0] + old1[0], old0[1] + old1[1]]])
    else:
        old = freq_chars.pop(0)
        allgroups.append(old)

# allchars is the combination of all chars in the computed sequence
allchars = [group for group in allgroups if len(group[1]) == max([len(x) for _, x in allgroups])][0][1]

# process the bits for each pair (left, right = above node)
left_right = {}
for freq1, char1 in sorted(allgroups, key=lambda x: [-len(x[1]), -x[0]]):
        for freq2, char2 in sorted(allgroups, key=lambda x: [-len(x[1]), -x[0]]):
            for freq3, char3 in sorted(allgroups, key=lambda x: [-len(x[1]), -x[0]]):
                if char2 + char3 == char1:
                    if char1.startswith(char2):
                        if char1 in left_right:
                            left_right[char2] = left_right[char1] + '0'
                            left_right[char3] = left_right[char1] + '1'
                        else:
                            left_right[char2] = '0'
                            left_right[char3] = '1'

# filter the single characters in left_right
conversion_table = {char: binary for char, binary in sorted(left_right.items(), key=lambda x: [len(x[1]), x[1]]) if len(char) == 1}
print('Conversion_table: (From the most to the least frequent character)\n', *conversion_table.items(), sep ='\t')

# compute the binary and converted (encripted) version of data_input
def encrypt(string, conversion_table):
    binary, crypto = '', ''
    for char in string:
        bin_prefix = '0' * (8-len(bin(ord(char))[2:]))
        binary += bin_prefix + bin(ord(char))[2:]
        crypto += conversion_table[char]
    return binary, crypto

# try to decrypt the encripted bits
def decrypt(bits, conversion_table):
    temp, decrypted = '', ''
    for bit in bits:
        temp += bit
        if temp in conversion_table.values():
            decrypted += [key for key, value in conversion_table.items() if value == temp][0]
            temp = ''
    return decrypted

print('_' * 100, '\nSAMPLES:')
sample = 'python for everyone'
sample_bin, sample_enc = encrypt(sample, conversion_table)
print(f'''The string "{sample}" converted using these two methods:
    Binary method: ({len(sample_bin)} bits)
        {sample_bin}
    Encryption method: ( {len(sample_enc)} bits)
        {sample_enc}''')

# process and finish analysis using data_input
binary, crypto = encrypt(data_input, conversion_table)
decrypted = decrypt(binary, conversion_table)
len_cry, len_bin = len(crypto), len(binary)

print('_' * 100, '\nANALYSIS FOR data_input:')
print(f'data_input type:   {type(data_input)}')
print(f'data_input size:   {lenght:,} characters (bytes)')
print(f'Binary size:       {len_bin:,} bits ({round(100 * len_bin / len_bin, 1)}%)\t8.00 bits (average) per character.')
print(f'Cryptography size: {len_cry:,} bits ( {round(100 * len_cry / len_bin, 1)}%)\t{round(len_cry/len(data_input), 2)} bits (average) per character.')

# the real benefit for storage or processing:
print('_' * 100, '\nCONCLUSION:')
print('You saved', round((len_bin - len_cry)/1024/1024, 2), 'MB from', round(len_bin/1024/1024, 2), 'MB using this encryption method!')
