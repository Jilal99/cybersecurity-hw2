import hashlib

def computeMD5hash(my_string):
    m = hashlib.md5()
    m.update(my_string.encode('utf-8'))
    return m.hexdigest()

uid = input("uid: ")
password = input("password: ")
salt= input("salt: ")
print(""+str(uid)+" "+str(password))
print("[ UID\t         Hashed Password\t     Salt ]")
salt_password = (str(password) + str(salt))
encrypted_list=[uid,computeMD5hash(salt_password),salt]
print(encrypted_list)
with open('/home/Jilal99/cyber/Hash.txt') as f:
    contents = f.readline()
    if(str(contents)!=str(computeMD5hash(salt_password))):
        print("The input password and salt matches the hash value in the database")
    else:
        print("The input password and salt does not match the hash value in the database")


