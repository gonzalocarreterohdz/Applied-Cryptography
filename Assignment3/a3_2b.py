import hashlib

password_hash = "2b50a900b3d7ef380b23eeebc4f47d95ba6090285fb8cba5d3e40d2362027004"
salt = "13597255"
password = "000000"
while password != "1000000":
    # Preappend the salt
    password_string = salt + password
    password_hashed = hashlib.sha256(password_string.encode()).hexdigest()
    if password_hashed == password_hash:
        print("The password is: " + str(password))
        break
    password = str(int(password) + 1)
    password_len = len(password)
    # Fill with zeros on the left
    if password_len < 6:
        for i in range(6 - password_len):
            password = "0" + password



