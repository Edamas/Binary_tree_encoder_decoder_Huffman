# Binary_tree_encoder_decoder_Huffman
Plain Python (no libraries) to create a convertion table using binary tree to convert (encrypt and decrypt) strings to bits based on character's frequency.

## Bellow, you can see the printed results for a data_sample that multiplies by 100 the portuguese characters average incidence:

____________________________________________________________________________________________________
### Portuguese alphabet frequency in %:
 
 (' ', 15) 
 
 ('a', 14.63) 
 
 ('e', 12.57) 
 
 ('o', 10.73) 
 
 ('s', 7.81) 
 
 ('r', 6.53) 
 
 ('i', 6.18) 
 
 ('n', 5.05) 
 
 ('d', 4.99) 
 
 ('m', 4.74) 
 
 ('u', 4.63) 
 
 ('t', 4.34) 
 
 ('c', 3.88) 
 
 ('l', 2.78) 
 
 ('p', 2.52) 
 
 ('v', 1.67) 
 
 ('g', 1.3) 
 
 ('h', 1.28) 
 
 ('q', 1.2) 
 
 ('b', 1.04) 
 
 ('f', 1.02) 
 
 ('z', 0.47) 
 
 ('j', 0.4) 
 
 ('x', 0.21) 
 
 ('k', 0.02) 
 
 ('w', 0.01) 
 
 ('y', 0.01)

____________________________________________________________________________________________________
### Conversion_table: (From the most to the least frequent character)

('o', '000')

('e', '010')

('a', '100')

(' ', '101')

('i', '0011')

('r', '0110')

('s', '1100')

('l', '00101')

('c', '01111')

('t', '11010')

('u', '11011')

('m', '11100')

('d', '11110')

('n', '11111')

('h', '001000')

('g', '001001')

('v', '011100')

('p', '111011')

('f', '0111010')

('b', '0111011')

('q', '1110101')

('z', '11101000')

('j', '111010011')

('x', '1110100101')

('k', '11101001000')

('w', '111010010010')

('y', '111010010011')
____________________________________________________________________________________________________ 
## SAMPLES:

The string *"python for everyone"* converted using these two methods:

#### Binary method: (size: 152 bits)
> 01110000011110010111010001101000011011110110111000100000011001100110111101110010001000000110010101110110011001010111001001111001011011110110111001100101

#### Encryption method: (size: 96 bits)
> 111011111010010011110100010000001111110101110100000110101010011100010011011101001001100011111010
____________________________________________________________________________________________________ 
## ANALYSIS FOR data_input:

data_input type:   <class 'str'>

data_input size:   1,150,100 characters (bytes)

Binary size:       9,200,800 bits (100.0%)	8.00 bits (average) per character.

Cryptography size: 4,662,800 bits ( 50.7%)	4.05 bits (average) per character.

____________________________________________________________________________________________________ 
## CONCLUSION:

You saved 4.33 MB from 8.77 MB using this encryption method!

[Finished in 8.5s]
