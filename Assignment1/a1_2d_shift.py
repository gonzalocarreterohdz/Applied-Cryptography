from collections import defaultdict
# Open file with ciphertext
f0 = open("ctxt3.txt", "r")
# Read content in file
c = f0.read()

letter_mapping = defaultdict(int)
reverse_letter_mapping = defaultdict(int)

for i in range(ord("A"), ord("Z") + 1):
  letter_mapping[chr(i)] = i - 65
  reverse_letter_mapping[i - 65] = chr(i)

# Open file with "normal" English
f1 = open("q1-mobydick.txt", "r")
# Read content in file
eng = f1.read()

# Creating the dataset
letters = [chr(i) for i in range(ord("A"), ord("Z") + 1)]
values_ctxt = []
values_eng = []

# Count the frequency of each character
for i in range(ord("A"), ord("Z") + 1):
  values_ctxt.append((c.count(chr(i)), i))
  values_eng.append((eng.count(chr(i)), i))

# Sort the lists in descending order
values_ctxt.sort(reverse=True)
values_eng.sort(reverse=True)

"""
# This code is in case you want to check for most common distance, not necessary to get this plaintext
distances = defaultdict(int)
for j in range(len(values_eng)):
  dist = abs(values_ctxt[j][1] - values_eng[j][1])
  distances[dist] += 1
"""

# Let's do it for distance between most frequent letter in both texts
# Seems a good option looking at the graphs
k = abs(values_ctxt[0][1] - values_eng[0][1])
plaintext = ""
for letter in c:
  # k = 12 in this case
  plaintext += reverse_letter_mapping[(letter_mapping[letter] - k) % 26]

print(plaintext)
# print(letter_mapping.items())
# Close files
f0.close()
f1.close()