Allowed_Message ="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
Number = "0123456789"

while True:
    Type = input("Masukan Message yang mau di Encrypt / Decrypt : ")
    if Type.lower() == "encrypt" or Type.lower() == "decrypt":
        break

while True:
    Message = input("Masukan Message : ")
    if Message in Allowed_Message:
        break

while True:
    key = input("Masukkan Key [angka] Untuk pesan : ")
    if key in Number and len(key) < 2 and len(key) >= 0:
        break

Key = int(key)
Length = len(Message)

if Type.lower() == "encrypt":
    for msg in range (Length):
        encrypt = ""
        Data = Message[msg]
        if Data.isupper():
            encrypt += chr((ord(Data) + Key - 65 ) % 26 + 65)
        elif Data.islower():
            encrypt += chr((ord(Data) + Key - 97 ) % 26 + 97)
        else:
            encrypt += Data
    print(encrypt)
else:
    for msg in range (Length):
        decrypt = ""
        Data = Message[msg]
        if Data.isupper():
            decrypt += chr(((ord(Data) - Key - 65 ) + 26)% 26 + 65)
        elif Data.islower():
            decrypt += chr(((ord(Data) - Key - 97 ) + 26)% 26 + 97)
        else:
            decrypt += Data
    print(decrypt)