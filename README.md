# One-Time-Pad
A Python system for encoding and decoding messages using the one time pad encyrption method.

## How To Use

### Encodeing 
These scripts are simple to use, to encode a message you can run the script along with putting the message to be encoded as an argument. 

Example 
`python3 encode.py "helloworld"`

this will then convert the letters to decimal asii and count how many digits you need to input from your one time pad this will then perform modulo additon between the ascii decimalisation and the numbers from your one time pad to give you an output for transmission to your recipiant.

### Decoding
This is essentially the reverse of the first script. you run the script using the encryted message along with the number from the one time pad to perform a modulo subtraction to get the ascii decimal then converts this back into text. 
Make sure to put the arguments in the following order. Encrypted message then one time pad 


Example
`python3 decode.py "365560695353682673795591991804" "261469597255571564684487893704"`


and its simple as that no more long winded wrting out of messages and working out the code mannually. 
