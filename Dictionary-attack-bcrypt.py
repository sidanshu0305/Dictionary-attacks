import bcrypt
def hash():
plaintext = str(input("Enter the string to be hashed:"))
b = bytes(plaintext, 'utf-8')
b = plaintext.encode('utf-8')
my_hashed_password = bcrypt.hashpw(b, bcrypt.gensalt())
print(my_hashed_password)
n=int(input("Enter the number of strings to be hashed:"))
for i in range (0,n):
hash()