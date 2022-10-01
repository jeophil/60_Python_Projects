import random
password_len = int(input("Enter the number of required length for the password"))
s = "qwertyuuuuiopasdfghjkklzzxcvbnm"

password = "".join(random.sample(s,password_len))
print(password)
