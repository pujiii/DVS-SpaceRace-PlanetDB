from pycipher import Beaufort

ciphered_text = Beaufort('A').encipher('Helloooo')
print(ciphered_text)

deciphered_text = Beaufort('A').decipher('TWPPMMMM')
print(deciphered_text)