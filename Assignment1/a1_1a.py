# Open file given in assignement
f = open("q1-mobydick.txt", "r")
# Store the content in a variable
text = f.read()

def index_of_coincidence(input_text: str) -> int:
    # Numerator of formula
    summation = 0
    # Length of text given
    n = len(input_text)
    # Iterate for all letter A-Z
    for i in range(ord("A"), ord("Z") + 1):
        # Count number of occurrences of current letter
        ocurrences = input_text.count(chr(i))
        if ocurrences > 2:
            # Add to the summation the binomial of occurrences over 2
            summation += (ocurrences * (ocurrences-1) / 2)
    # Divide summation by binomial of length of given text over 2 and return result
    return summation / (n * (n-1) / 2)

print(index_of_coincidence(text))
f.close()
