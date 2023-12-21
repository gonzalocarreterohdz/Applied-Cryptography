import matplotlib.pyplot as plt
# Open file with ciphertext
f0 = open("a1q2ciphertexts/ctxt0.txt", "r")
# Read content in file
c0 = f0.read()
f1 = open("a1q2ciphertexts/ctxt1.txt", "r")
c1 = f1.read()
f2 = open("a1q2ciphertexts/ctxt2.txt", "r")
c2 = f2.read()
f3 = open("a1q2ciphertexts/ctxt3.txt", "r")
c3 = f3.read()


# Creating the dataset
letters = [chr(i) for i in range(ord("A"), ord("Z") + 1)]
values = []

# Count the frequency of each character
for i in range(ord("A"), ord("Z") + 1):
  values.append(c3.count(chr(i)))

# Chart size
fig = plt.figure(figsize = (8, 5))
 
# Creating the bar plot
plt.bar(letters, values, color ='darkred',
        width = 0.4)

# Labels 
plt.xlabel("Letters")
plt.ylabel("Frequency")
plt.title("Letter Frequency Analysis ctxt3")
# Show the chart
plt.show()

# Close files
f0.close()
f1.close()
f2.close()
f3.close()