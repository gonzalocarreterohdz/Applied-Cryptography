# Open file with ciphertext
f = open("ctxt1.txt", "r")
# Read content in file
c = f.read()
# Key
k = {}
# Obtained in https://www.dcode.fr/monoalphabetic-substitution
substitution = ["D", "V", "M", "F", "I", "Q", "W", "T", "N", "S", "Z", "B", "L", "E", "C", "X",\
                "R", "Y", "J", "U", "O", "P", "G", "A", "K", "H"]

counter = 0
# Mapping
for i in range(ord("A"), ord("Z") + 1):
    k[chr(i)] = substitution[counter]
    counter += 1

# Recovering original message
plaintext = ""
for letter in c:
    plaintext += k[letter]

print(plaintext)
f.close()
