from collections import defaultdict
# Open file given in assignement
f = open("q1-ciphertext.txt", "r")
# Store the content in a variable
ciphertext = f.read()
# Length of ciphertext given
n = len(ciphertext)

# Function made in section "a)" of the exercise 
def index_of_coincidence(input_text: str) -> int:
    summation = 0
    n = len(input_text)
    for i in range(ord("A"), ord("Z") + 1):
        ocurrences = input_text.count(chr(i))
        if ocurrences > 2:
            summation += (ocurrences * (ocurrences-1) / 2)
    return summation / (n * (n-1) / 2)

# We will check all possible block lengths (between 1 and 100)
for m in range(1, 101):
    # Dictionary to store all strings (y1, y2, ..., ym)
    y_dict = defaultdict(str)
    # We loop through all the letters of ciphertext
    for i in range(n):
        # Calculate to which string belongs current letter given current block length 
        i_mod_m = i % m
        # Add ciphertext letter to corresponding string
        y_dict[i_mod_m] += ciphertext[i]
    # To store index of coincidence values for all strings
    ind_of_coinc_list = []
    # To count how many strings are close to expected
    # index of coincidence value for current block length
    count = 0
    # Loop through every string in dictionary
    for y in y_dict.values():
        # Calculate index of coincidence
        i_o_c = index_of_coincidence(y)
        ind_of_coinc_list.append(i_o_c)
        # Increase counter if computed value close to expected
        if abs(i_o_c - 0.06592077212956918) < 0.007:
            count += 1
    
    """This part is to only print the desired result"""
    found = False
    # If all strings have an index of coincidence value close to the expected one
    if abs(m - count) == 0:
        found = True
    
    if found:
        # To see the index of coincidence of the strings
        print(ind_of_coinc_list)
        # This is the result, the block length 
        print(m)

f.close()
