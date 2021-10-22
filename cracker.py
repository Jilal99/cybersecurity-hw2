import hashlib, bcrypt

password = input("input the password to hash\n")
print("\n MD5: \n")
for i in range(3):
    setpass = bytes(password, 'utf-8')
    hash_object = hashlib.md5(setpass)
    guess_pw = hash_object.hexdigest()
    print("guess_pw")

print("\n BCRYPT: \n")    
for i in range(3):
    hashed = bcrypt.hashpw(setpass, bcrypt.gensalt(10))

