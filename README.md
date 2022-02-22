# Binary_tree_encoder_decoder_Huffman
Plain Python (no libraries) to create a convertion table using binary tree to convert (encrypt and decrypt) strings to bits based on character's frequency.

## Bellow, you can see the printed results for a data_sample based on average letter occurrence in brazilian portuguese (with the least common letters "w" and "y" appearing 1000 times):


## Frequency for each character:

- 0.00869%	 "w"
- 0.00869%	 "y"
- 0.01739%	 "k"
- 0.18259%	 "x"
- 0.34780%	 "j"
- 0.40866%	 "z"
- 0.88688%	 "f"
- 0.90427%	 "b"
- 1.04339%	 "q"
- 1.11295%	 "h"
- 1.13034%	 "g"
- 1.45205%	 "v"
- 2.19111%	 "p"
- 2.41718%	 "l"
- 3.37362%	 "c"
- 3.77358%	 "t"
- 4.02574%	 "u"
- 4.12138%	 "m"
- 4.33875%	 "d"
- 4.39092%	 "n"
- 5.37345%	 "i"
- 5.67777%	 "r"
- 6.79071%	 "s"
- 9.32962%	 "o"
- 10.92948%	 "e"
- 12.72063%	 "a"
- 13.04234%	 " "

## Conversion_table: (From the most to the least frequent character

### Printables
- 000                           	o         
- 010                           	e         
- 100                           	a         
- 101                           	          
- 0011                          	i         
- 0110                          	r         
- 1100                          	s         
- 00101                         	l         
- 01111                         	c         
- 11010                         	t         
- 11011                         	u         
- 11100                         	m         
- 11110                         	d         
- 11111                         	n         
- 001000                        	h         
- 001001                        	g         
- 011100                        	v         
- 111011                        	p         
- 0111010                       	f         
- 0111011                       	b         
- 1110101                       	q         
- 11101000                      	z         
- 111010011                     	j         
- 1110100101                    	x         
- 11101001000                   	k         
- 111010010010                  	w         
- 111010010011                  	y         
----------------------------------------------------------------------------------------------------
> Encoding to standard 8 bits...

> Encoding binary tree (encryption)...

> Decoding encrypted bits...
____________________________________________________________________________________________________ 
## ANALYSIS FOR data_input:

#### data_input:
                                                                                                    

- data_input type:   <class 'str'>
- data_input size:   11,501,000b (bytes or characters)
- Binary size:       92,008,000 bits (100.0%)	8.00 bits per character.
- Cryptography size: 46,628,000 bits ( 50.7%)	4.05 bits (average) per character.
____________________________________________________________________________________________________ 
## CONCLUSION:

> You saved 5.40972MB from 10.96821MB using this encryption method!
[Finished in 11.3s]
