import hashlib
f = open("word_list.txt", "r")
words = [line.rstrip() for line in f]
special_char = "!?*$#&"
pasword_hash = "cc87353107853c0042aad6cb7762bfc09bc88530198f7dfe679ae9c872a92a26"
counter_num_hashes = 0
salt = "51054097"

for p in words:
    # Upper case the first letter
    password = p[0].upper() + p[1:]
    # Number of digits to add
    num_len = 11 - len(password)
    numbers = ""
    for i in range(num_len):
        numbers += "0"
    # Brute force the numbers
    for j in range(10**num_len):
        password_string = password + numbers
        # Try all special characters at the end
        for k in range(6):
            password_string += special_char[k]
            # Preappend the salt
            password_string = salt + password_string
            print(password_string)
            password_hashed = hashlib.sha256(password_string.encode()).hexdigest()
            counter_num_hashes += 1
            if password_hashed == pasword_hash:
                print("The password is: " + password_string[8:])
                break
            password_string = password_string[8:-1]
        # Increment the numbers
        numbers = str(int(numbers) + 1)
        # Fill with zeros on the left
        numbers_len = len(numbers)
        if numbers_len < num_len:
            for i in range(num_len - numbers_len):
                numbers = "0" + numbers
        # Check if the password is found
        if password_hashed == pasword_hash:
            break
    # Check if the password is found
    if password_hashed == pasword_hash:
        break


print("Number of hashes: " + str(counter_num_hashes))

f.close()